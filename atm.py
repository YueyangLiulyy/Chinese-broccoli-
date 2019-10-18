class ATM:
    def __init__(self, accountListFile, transactionSummary):
        self.accountList = []
        self.transactionList = []
        self.depositRecord = {}                                                 # key: account, value: depositted amount
        self.withdrawRecord = {}                                                # key: account, value: withdrawn amount
        self.transferRecord = {}                                                # key: account, value: transferred amount 
        self.readList(accountListFile)                                          # read account list to accountList
        self.writeTarget = transactionSummary 
        self.interface()

    # read account list and append it to accountList
    def readList(self,fileName):
        with open(fileName, 'r') as f:
            line = f.readline()
            while line:
                self.accountList.append(line.strip())
                line = f.readline()


    # takes amount in cent such as "001"
    # convert it to float, such as 0.01
    def inputConvert(self, amount):
        return float(amount[:-2] + "." + amount[-2:])


    # main interface 
    def interface(self):
        while True:                                                             # loop until accept 'logout' command 
            self.greeting()
            function = input()
            if function == "deposit":
                signal = self.functionDeposit()
                if signal == 0: break
            elif function == "withdraw":
                signal = self.functionWithdraw()
                if signal == 0: break
            elif function == "transfer":
                signal = self.functionTransfer()
                if signal == 0: break
            elif function == "createacct":
                signal = self.functionCreateAccount()
                if signal == 0: break
            elif function == "deleteacct":
                signal = self.functionDeleteAccount()
                if signal == 0: break
            elif function == "logout":
                break
            else:
                print("Check your input, and try again!")
        self.functionLogout()
    
    # deposit logic frame
    # get valid toAccount and amount, 
    # then append the transaction to transactionList
    def functionDeposit(self):
        toAccount = input("Enter your account please: ")
        if toAccount == "logout":
            return 0
        while (not self.verifyAccount(toAccount) or not self.existAccount(toAccount)):          # invalid format or non-exist 
            toAccount = input("--> ")
            if toAccount == "logout":
                return 0
        amount = input("Enter the amount of money you want to deposit: ")
        if amount == "logout":
            return 0
        while not self.verifyDepositAmount(toAccount,amount):                                   # invalid amount                                 
            amount = input("--> ")
            if amount == "logout":
                return 0
        transaction = "DEP {} {} 0000000 ***\n".format(toAccount, amount)
        self.transactionList.append(transaction)                                                # append transaction info to the transactionList 
        self.recordTransaction("deposit", toAccount, self.inputConvert(amount))                 # record transaction 
        print("<--  Your transaction has been successfully made!  -->")
        print("=="*34)
        return 1  
        
    # withdraw logic frame 
    # get valid fromAccount and amount,
    # then append the transaction to the transactionList.
    def functionWithdraw(self):
        fromAccount = input("Enter your account please: ")
        if fromAccount == "logout":
            return 0
        while (not self.verifyAccount(fromAccount) or not self.existAccount(fromAccount)):      # invalid format or non-exist 
            fromAccount = input("--> ")
            if fromAccount == "logout":
                return 0
        amount = input("Enter the amount of money you want to withdraw: ")
        if amount == "logout":
            return 0
        while not self.verifyWithdrawAmount(fromAccount, amount):                               # invalid amount 
            amount = input("--> ")
            if amount == "logout":
                return 0
        transaction = "WDR 0000000 {} {} ***\n".format(amount, fromAccount)
        self.transactionList.append(transaction)                                                # append transaction info to the transactionList
        self.recordTransaction("withdraw", fromAccount, self.inputConvert(amount))              # record transaction 
        print("<--  Your transaction has been successfully made!  -->")
        print("=="*34)
        return 1
    
    # transfer logic frame 
    # get valid fromAccount, toAccount, and amount,
    # then append the transaction to the transactionList.
    def functionTransfer(self):
        fromAccount = input("Enter your account please: ")
        if fromAccount == "logout":
            return 0
        while (not self.verifyAccount(fromAccount) or not self.existAccount(fromAccount)):      # invalid format or non-exist 
            fromAccount = input("--> ")
            if fromAccount == "logout":
                return 0
        toAccount = input("Enter the payee account please: ")
        if toAccount == "logout":
            return 0
        while (not self.verifyAccount(toAccount) or not self.existAccount(toAccount)):          # invalid format or non-exist 
            toAccount = input("--> ")
            if toAccount == "logout":
                return 0
        amount = input("Enter the amount of money you want to transfer: ")                     
        if amount == "logout":
            return 0
        while not self.verifyTransferAmount(fromAccount, amount):                               # invalid amount 
            amount = input("--> ")  
            if amount == "logout":
                return 0
        transaction = "XFR {} {} {} ***\n".format(toAccount, amount, fromAccount )
        self.transactionList.append(transaction)                                                # append transaction info to transactionList
        self.recordTransaction("transfer", fromAccount, self.inputConvert(amount))              # record transaction
        print("<--  Your transaction has been successfully made!  -->")
        print("=="*34)
        return 1
    
    # createacct (not supported in ATM mode)
    # overriden in agent.py
    def functionCreateAccount(self):
        print("The operation is not supported in ATM mode")
        print("=="*34)
        return 1
    
    # deleteacct (not supported in ATM mode)
    # overriden in agent.py 
    def functionDeleteAccount(self):
        print("The operation is not supported in ATM mode")
        print("=="*34)
        return 1

    # logout
    # write transaction summary file here 
    def functionLogout(self):
        f = open(self.writeTarget, "w")   
        self.transactionList.append("EOF")                                              # transaction summary file end with "EOF"
        print(self.transactionList)
        f.writelines(self.transactionList)                                              # write transaction summary file 
        f.close()
        return 0

    # record transaction in corresponding dict
    # @transaction: type of transaction 
    # @account:     account number
    # @amount:      the amount of the type of transaction 
    def recordTransaction(self, transaction, account, amount):
        if transaction == "deposit":
            currentAmount = self.depositRecord.get(account)
            if currentAmount is None:                                                  # uninitialized amount will be None
                currentAmount = 0
            updatedAmount = currentAmount + amount
            self.depositRecord[account] = updatedAmount
        elif transaction == "withdraw":
            currentAmount = self.withdrawRecord.get(account)
            if currentAmount is None:                                                  # uninitialized amount will be None
                currentAmount = 0
            updatedAmount = currentAmount + amount
            self.withdrawRecord[account] = updatedAmount
        elif transaction == "transfer":
            currentAmount = self.transferRecord.get(account)
            if currentAmount is None:                                                  # uninitialized amount will be None
                currentAmount = 0
            updatedAmount = currentAmount + amount
            self.transferRecord[account] = updatedAmount

    # verify the account if is valid or not
    # length exactly 7 digits and can not start with '0'
    def verifyAccount(self,account):
        if len(account) != 7:
            print("The account has to be exactly 7 digits")
            return False
        elif account[0] == '0':
            print("the account cannot start with '0'")
            return False
        elif not account.isdigit():
            print("The account cannot contain other characters")
            return False
        return True


    # verify the amount is valid 
    # length is valid and only contain number
    # todo: hadle when input is such as"01111"
    def verifyAmount(self, amount):
        if len(amount) < 3 or len(amount) > 8:
            print("Invalid amount, please try agian!")
            return False
        elif not amount.isdigit():
            print("Invalid amount, please try again!")
            return False
        else:
            return True
    

    # further verfiy the deposit amount
    # each deposit within $2,000
    # daily deposit limit is $5,000
    def verifyDepositAmount(self, account, amount):
        if self.verifyAmount(amount):
            if self.inputConvert(amount) > 2000:                                                            # each time deposit should <= $2,000
                print("The limit of each depoist is $2,000, please retype: ", end="")
                return False
            currentAmount = self.depositRecord.get(account)
            if currentAmount is None or 5000 >= currentAmount + self.inputConvert(amount):                  # total deposit should <= $5,000 
                return True
            else:
                print("The daily limit of deposit is $5,000, ", end="")
                print("you have used ${}, please try again.".format(self.depositRecord.get(account)))
                return False
        return False

    # further verify the withdraw amount
    # each withdraw within $1,000
    # daily withdraw limit is $5,000
    def verifyWithdrawAmount(self, account, amount):
        if self.verifyAmount(amount):
            if self.inputConvert(amount) > 1000:                                                            # each time withdraw should <= $1,000
                print("The limit of each withdraw is $1,000, please retype: ", end="")
                return False
            currentAmount = self.withdrawRecord.get(account)
            if currentAmount is None or 5000 >= currentAmount + self.inputConvert(amount):                  # total withdraw amount should <= $5,000 
                return True
            else:
                print("The daliy limit of withdraw is $5,000, ", end="")
                print("you have withdrawn ${}, please try again.".format(self.withdrawRecord.get(account)))
                return False
        return False
    
    # further verify the transfer amount
    # each transfer within $10,000
    # daily transfer limit is $10,000
    def verifyTransferAmount(self, fromAccount, amount):
        if self.verifyAmount(amount):
            if self.inputConvert(amount) > 10000:                                                       # each transfer should <= $10,000
                print("The limit of each transfer is $10,000, please retype: ", end="")
                return False
            currentAmount = self.transferRecord.get(fromAccount)
            if currentAmount is None or 10000 >= currentAmount + self.inputConvert(amount):             # total transfer should <= $10,000
                return True
            else:
                print("The daliy limit of transfer is $10,000, ", end="")
                print("you have transferred ${}, please try again.".format(self.transferRecord.get(fromAccount))) 
        return False

    # binary search see if a account in the account list 
    def existAccount(self,account):
        start = 0
        end = len(self.accountList) - 2
        while start <= end:
            middle = (start + end) // 2
            if self.accountList[middle] < account:
                start = middle + 1 
            elif self.accountList[middle] > account:
                end = middle - 1
            else:
                return True
        print("No matching account found!")
        return False

    # print greeting when login to ATM mode
    # overriden in agent.py
    def greeting(self):
        print("Helo, welcome to the ATM mode, please type the transaction you want to make: ",end="")

 
