# Inherit the ATM class from the atm file
from atm import ATM

# The AGENT class which is the child class of the ATM class
class AGENT(ATM):

    # Inherit the variables
    def __init__(self, accountListFile, transactionSummary):
        # get parents variables
        super().__init__(accountListFile, transactionSummary)


    # The function for create account
    # overridden
    def functionCreateAccount(self):
        # Check account number
        accountNumber = input("Enter the new account number you want to create please: ")
        if accountNumber == "logout":
            return 0
        while (not super().verifyAccount(accountNumber)) or (self.sameAccount(accountNumber)):
            accountNumber = input("--> ")
            if accountNumber == "logout":
                return 0
        # Check account name
        accountName = input("Enter the account name for the new account: ")
        if accountName == "logout":
            return 0
        while not self.verifyAccountName(accountName):
            accountName = input("Enter the account name for the new account: ")
            if accountName == "logout":
                return 0
        # Add transaction to transactionList
        transaction = "NEW {} 000 0000000 {}\n".format(accountNumber, accountName)
        self.transactionList.append(transaction)
        print("<--  Your transaction has been successfully made!  -->")
        print("=="*34)
        return 1

    # The function for delete account
    # overridden
    def functionDeleteAccount(self):
        # Check account number
        accountNumber = input("Enter the new account number you want to delete please: ")
        if accountNumber == "logout":
            return 0
        while (not super().verifyAccount(accountNumber)) or (not super().existAccount(accountNumber)):
            accountNumber = input("--> ")
            if accountNumber == "logout":
                return 0
        # Check account name
        accountName = input("Enter the account name you want to delete: ")
        if accountName == "logout":
            return 0
        while not self.verifyAccountName(accountName):
            accountName = input("Enter the account name you want to delete: ")
            if accountName == "logout":
                return 0
        # Delete the account from account list
        self.accountList.remove(accountNumber)
        # Add transaction to transactionList
        transaction = "DEL {} 000 0000000 {}\n".format(accountNumber, accountName)
        self.transactionList.append(transaction)
        print("<--  Your transaction has been successfully made!  -->")
        print("=="*34)
        return 1

    # Check if the account number is in the account list
    def sameAccount(self, account):
        for currentAccount in self.accountList:
            if currentAccount == account:
                print("The account already exist.")
                return True
        return False

    # Check the new account name should between 3 and 30 alphanumeric characters, 
    # and not beginning or ending with a space
    def verifyAccountName(self, accountName):
        if len(accountName) < 3 or len(accountName) > 30:
            print("the new account name should between 3 and 30 alphanumeric characters: ")
            return False
        elif accountName[0] == ' ' or accountName[-1] == ' ':
            print( "the new account name should not beginning or ending with a space: ")
            return False
        else:
            return True
    
    # overridden greeting in atm
    def greeting(self):
        print("Hello, welcome to the agent mode, please type the transaction you want to make: ", end="")

