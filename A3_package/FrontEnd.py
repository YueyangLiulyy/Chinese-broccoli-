import sys
from atm import ATM
from agent import AGENT



def login(accountListFile, transactionSummary):
    try:
        choice = input("Welcome to the front end: \n")
        if choice == 'login':                                                               # use correctly input login
            print("Successfully login.")     
            status = False                                                                  # check the validation of input
            while status == False:                                                          # loop if user input invalid command 
                mode = input("Select mode to enter: \n")                                      # select mode
                if mode == "atm":                                                           # user correctly input atm
                    print("Successfully entered ATM mode.")
                    newAtm = ATM(accountListFile, transactionSummary)                                           # create new atm object
                    status = True                                                           
                elif mode == "agent":                                                       # user correctly input agent
                    print("Successfully entered agent mode.")
                    newAgent = AGENT(accountListFile, transactionSummary)                                       # create new agent object
                    status = True
                elif mode == "logout":
                    status = True
                    f = open(transactionSummary, "w")
                    f.writelines("EOS")
                    f.close()
                else:                                                                       # error for anything else
                    print("Error:Invalid mode choice, please input a valid mode choice!")
            print("Successfully logout.")
            login(accountListFile, transactionSummary)
        else:                                                                               # invalid input
            print("Error:Please login first!")
            login(accountListFile, transactionSummary)
    except:
        quit                                                                            # exit program
        

    

def main():
    accountListFile = sys.argv[1]
    transactionSummary = sys.argv[2]
    login(accountListFile, transactionSummary)
    
    

if __name__ == "__main__":
    main()
