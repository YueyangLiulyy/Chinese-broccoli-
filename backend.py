import os
import sys
class backEnd:
    def __init__(self, masterFile, transactionsFile):
        self.transactionsList = self.readFile(transactionsFile)                 
        self.masterList = self.readFile(masterFile)
        if self.masterList is False or self.transactionsList is False:
            print("program terminated!") 
        else:
            self.length = len(self.masterList)
            if not self.combine():
                print("program terminated!") 
            else:
                self.validAccountsList = self.updateValidAccList()
                self.masterList[-1] = self.masterList[-1].strip()
                self.writeFile(masterFile, "accountList.txt", self.validAccountsList)
                self.writeFile(masterFile, "masterAccount.txt", self.masterList)

    # Read the targeted file
    def readFile(self, target):
        flist = []
        try:
            with open (target) as f:
                line = f.readline()
                while line and line != "EOS":
                    flist.append(line)
                    line = f.readline()
            return flist
        except FileNotFoundError:
            print("Can not find the targeted file! ")
            return False
        return True
            

    # write file with given content, directory, and name
    def writeFile(self, directory, name, content):
        targetDir = os.path.dirname(__file__) + "/out/"
        targetFile = targetDir + name
        # new master account file
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)
        with open(targetFile, "w") as f:
            f.writelines(content)
    
    
    # update the valid account list 
    def updateValidAccList(self):
        validAccountsList = []                              # reset the valid account list
        for master in self.masterList:
            acctNum = master[:7] + "\n"                     # first 7 digits are account number
            validAccountsList.append(acctNum)               # add account number in order with master list
        validAccountsList.append("0000000")
        return validAccountsList
        

    # combine transaction summary file with old master account file 
    def combine(self):
        for trans in self.transactionsList:
            if not self.preProcessing(trans):
                return False
        return True

     # classify different transaction, and send them to corresponding function
    # @transact a line of transaction 
    def preProcessing(self, transact):
        transaction = transact.split(' ')
        opreation = transaction[0]
        toAccount = transaction[1]
        amount = transaction[2]
        fromAccount = transaction[3]
        name = transaction[4]
        if opreation == "DEP":
            return self.processDeposit(toAccount, amount, fromAccount)
        elif opreation == "WDR":
            return self.processWithdraw(toAccount, amount, fromAccount)
        elif opreation == "XFR":
            return self.processTransfer(toAccount, amount, fromAccount)
        elif opreation == "NEW":
            return self.processCreate(toAccount, amount, fromAccount, name)
        elif opreation == "DEL":
            return self.processDelete(toAccount, amount, fromAccount, name)
        else:
            print(f"Transaction: ${opreation} ${toAccount} ${amount} ${fromAccount} *** is invalid!")
            return False


    # search for target account by binary search
    # @ targetAccount target account
    # @ return (found or not, closest index) 
    def binarySearch(self,targetAccount):
        targetAccount = int(targetAccount)
        start = 0
        end = self.length - 1
        # prepare for the return when not find the account number
        middle = (start + end) // 2
        while start <= end:
            middle = (start + end) // 2
            account = self.masterList[middle][:7]
            if targetAccount == int(account):
                return True, middle
            elif targetAccount > int(account):
                end = middle - 1
            else:
                start = middle + 1
        return False, middle


    # insert the new line to the correct position in master list 
    # @newClient string of new client information 
    # @startIdx the closest index start to 
    def insertToList(self, newClient, startIdx):
        newAccount = newClient[:7]                      # first 7 digits are account number                  
        account = self.masterList[startIdx][:7]
        if newAccount < account:
            self.masterList.insert(startIdx+1, newClient)
        else:
            self.masterList.insert(startIdx, newClient)
                
    # line of information in master account file should < 47 characters 
    def checkUpdateInfo(self, updateInfo):
        return len(updateInfo) <= 47


    # The process for deposit transcription
    def processDeposit(self, toAccount, amount, fromAccount):
        match, idx = self.binarySearch(toAccount)
        if match:
            increaseAccount = self.masterList[idx].split(' ')
            name = increaseAccount[2].strip()
            oldAmount = increaseAccount[1]
            newAmount = int(oldAmount) + int(amount)
            updateInfo = f"{toAccount} {newAmount} {name}"
            if self.checkUpdateInfo(updateInfo):
                self.masterList[idx] = updateInfo
            else:
                print(f"Transaction: DEP {toAccount} {amount} {fromAccount} *** is invalid!")
                print("Due to: invalid length!")
                return False
        else:
            print(f"Transaction: DEP {toAccount} {amount} {fromAccount} *** is invalid!")
            print("Due to: no matching account found!")
            return  False
        return True


    # The process for withDraw transcription
    def processWithdraw(self, toAccount, amount, fromAccount):
        match, idx = self.binarySearch(fromAccount)
        if match:
            decreaseAccount = self.masterList[idx].split(' ')
            name = decreaseAccount[2].strip()
            oldAmount = decreaseAccount[1]
            newAmount = int(oldAmount) - int(amount)
            if newAmount < 0 :
                print(f"Transaction: WDR {toAccount} {amount} {fromAccount} *** is invalid!")
                print("Due to: insufficient balance!")
                return False
            else:
                updateInfo = f"{fromAccount} {newAmount} {name}\n"
                if self.checkUpdateInfo(updateInfo):
                    self.masterList[idx] = updateInfo
                else:
                    print(f"Transaction: WDR {toAccount} {amount} {fromAccount} *** is invalid!")
                    print("Due to: Invalid length!")
                    return  False
        else:
            print(f"Transaction: WDR {toAccount} {amount} {fromAccount} *** is invalid!")
            print("Due to: no matching account found!")
            return False
        return True


    # The process for transfer transcription
    def processTransfer(self, toAccount, amount, fromAccount):
        match, idx = self.binarySearch(fromAccount)
        match2, idx2 = self.binarySearch(toAccount)
        if match and match2:
            decreaseAccount = self.masterList[idx].split(' ')
            increaseAccount = self.masterList[idx2].split(' ')
            oldAmount = decreaseAccount[1]
            oldAmount2 = increaseAccount[1]
            newAmount = int(oldAmount) - int(amount)
            newAmount2 = int(oldAmount2) + int(amount)
            name = decreaseAccount[2].strip()
            name2 = increaseAccount[2].strip()
            if newAmount < 0 :
                print(f"Transaction: XFR {toAccount} {amount} {fromAccount} *** is invalid!")
                print("Due to: insufficient balance!")
                return False
            else:
                updateInfo = f"{fromAccount} {newAmount} {name}\n"
                updateInfo2 = f"{toAccount} {newAmount2} {name2}\n"
                if self.checkUpdateInfo(updateInfo) and self.checkUpdateInfo(updateInfo2):
                    self.masterList[idx] = updateInfo
                    self.masterList[idx2] = updateInfo2
                else:
                    print(f"Transaction: XFR {toAccount} {amount} {fromAccount} *** is invalid!")
                    print("Due to: invalid length!")
                    return False
        else:       # it should never come to here 
            print(f"Transaction: XFR {toAccount} {amount} {fromAccount} *** is invalid!")
            print("Due to: no matching account found!")
            return False
        return True
            

    # The process for create account transactions to master list
    def processCreate(self, toAccount, amount, fromAccount, name):
        name = name.strip()
        match, idx = self.binarySearch(toAccount)
        if match:       # account already exist 
                print(f"Transaction: NEW {toAccount} {amount} {fromAccount} {name} is invalid!")
                print("Due to: account already exists!")
                return False
        else:
            updateInfo = f"{toAccount} 000 {name}\n"
            if self.checkUpdateInfo(updateInfo):
                self.insertToList(updateInfo, idx)
                self.length += 1
            else:
                print(f"Transaction: NEW {toAccount} {amount} {fromAccount} {name} is invalid!")
                print("Due to: invalid length!")
                return False
        return True
            

    # The process for delete account transactions to master list
    def processDelete(self, toAccount, amount, fromAccount, name):
        name = name.strip()
        match, idx = self.binarySearch(toAccount)
        if not match:
            pass
        else:
            deleteAccount = self.masterList[idx].split(' ')
            if deleteAccount[1] != "000":
                print(f"Transaction: DEL {toAccount} {amount} {fromAccount} {name} is invalid!")
                print("Due to: A deleted account must have a zero balance!")
                return  False
            elif deleteAccount[2].strip() != name:
                print(f"Transaction: DEL {toAccount} {amount} {fromAccount} {name} is invalid!")
                print("Due to: No matching name!")
                return  False
            else:
                # delete the master line by the index
                self.masterList.pop(idx)
                self.length -= 1
        return  True
    



def main():
    # summaryDir= "D:/CISC327/project/backEnd/testCase/withdraw_decision_coverage/input/summary1.1.txt"
    # masterFile= "D:/CISC327/project/backEnd/testCase/withdraw_decision_coverage/input/master1.1.txt"
    summaryDir = sys.argv[1]
    masterFile = sys.argv[2]
    back = backEnd(masterFile, summaryDir)
    # print(back.masterList)
    # print(back.validAccountsList)


if __name__ == "__main__":
    main()