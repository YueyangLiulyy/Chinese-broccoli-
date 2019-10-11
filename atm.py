class ATM:
    accountList = []
    transactionList = []

    def __init__(self, accountListFile):
        self.readList(accountListFile)
        self.interface()
    


    def readList(self,fileName):
        with open(fileName, 'r') as f:
            line = f.readline()
            while line:
                self.accountList.append(line.strip())
                line = f.readline()


    def interface(self):
        function = input("Welcome to ATM mode, please type in your choice: ")
        if function == "deposit":
            self.functionDeposit()
        elif function == "withdraw":
            self.functionWithdraw()
        elif function == "transfer":
            self.functionTransfer()
        elif function == "logout":
            return 0
        while function == "creataccount" or function == "deleteaccount":
            print("Invalid operation in ATM mode, choose again: ")                                    # throw error message 
            function = input("choice: ")

    
    def functionDeposit(self):
        toAccount = input("Enter your account please: ")
        while not self.verifyAccount(toAccount):
            toAccount = input("Check your account number, and input again: ")
        amount = input("Enter the amount of money you want to deposit: ")
        while not self.verifyAmount(amount):
            amount = input("Check the amount again, and input again: ")                 
        transaction = "DEP {} {} 0000000 ***\n".format(toAccount, amount)
        transactionList.append(transaction)
        

    def functionWithdraw(self):
        fromAccount = input("Enter your account please: ")
        while not self.verifyAccount(fromAccount):
            fromAccount = input("Check your account number, and input again: ")
        amount = input("Enter the amount of money you want to withdraw: ")
        while not self.verifyAmount(amount):
            amount = input("Check the amount again, and input again: ")
        transaction = "WDR 0000000 {} {} ***\n".format(amount, fromAccount)
        transactionList.append(transaction)

    
    def functionTransfer(self):
        fromAccount = input("Enter your account please: ")
        while not self.verifyAccount(fromAccount):
            fromAccount = input("Check your account number, and input again: ")
        toAccount = input("Enter the payee account please: ")
        while not self.verifyAccount(toAccount):
            toAccount = input("Check the payee account number, and input again: ")
        amount = input("Enter the amount of money you want to transfer: ")
        while not self.verifyAmount(amount):
            amount = input("Check the amount again, and input again: ")  
        transaction = "XFR {} {} {} ***\n".format(toAccount, amount, fromAccount )
        transactionList.append(transaction)


    def functionLogout(self):
        f = open("transactionSummary.txt", "w+")
        transactionList.append("EOF")
        f.writelines(transactionList)
        return 0
        



    def verifyAccount(self,account):
        if len(account) != 7:
            return False
        elif account[0] == '0':
            return False
        elif not account.isdigit():
            return False
        else:
            return True

    def verifyAmount(self, amount):
        if len(amount) < 3 or len(amount) > 8:
            return False
        elif not amount.isdigit():
            return False
        else:
            return True

def main():
    fn = "D:/f1.txt"
    myAtm = ATM(fn)
    
    print(myAtm.accountList)

main()
