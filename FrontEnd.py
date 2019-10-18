import sys
from atm import ATM
from agent import AGENT

def login(accountListFile, transactionSummary):
    choice = input("Welcome to the front end: ")                                        
    if choice == 'login':                                                               # use correctly input login
        print("Sucessfully login.")     
        status = False                                                                  # check the validation of input
        while status == False:                                                          # loop if user input invalid command 
            mode = input("Select mode to enter: ")                                      # select mode
            if mode == "atm":                                                           # user correctly input atm
                print("Sucessfully entered atm mode.")
                newAtm = ATM(accountListFile, transactionSummary)                                           # create new atm object
                status = True                                                           
            elif mode == "agent":                                                       # user correctly input agent
                print("Sucessfully entered agent mode.")
                newAgent = AGENT(accountListFile, transactionSummary)                                       # create new agent object
                status = True                                                           
            else:                                                                       # error for anything else
                print("Error:Invalid mode choice, please input a valid mode choice!")     
    else:                                                                               # invalid input
        print("Error:Please login first!")
        login(accountListFile, transactionSummary)

def main():
    accountListFile = sys.argv[1]
    transactionSummary = sys.argv[2]
    login(accountListFile, transactionSummary)
    
    

if __name__ == "__main__":
    main()
