import Daily as dy
import os


class Weekly:
    def __init__(self):
        for i in range(1,6):
            print('Welcome to DAY ' + str(i))
            dy.daily(i)
            if i != 5:
                self.updateFile(i)
                print('\n' * 5)
    
    # prepare next day's account list and master account 
    def updateFile(self, d):
        f1 = open("day"+ str(d) +"/backend_out/masterAccount.txt", 'r')     # today's back end output is next
        f2 = open("day"+ str(d+1) + "/backend_in/masterAccount.txt", 'w')   # day back end input
        m = f1.readlines()
        for item in m:
            f2.write(item)
        f1.close()
        f2.close()
        f1 = open("day"+ str(d) +"/backend_out/accountList.txt", 'r')
        f2 = open("day"+ str(d+1) + "/frontend_in/account.txt", 'w')
        m = f1.readlines()
        for item in m:
            f2.write(item)
        f1.close()
        f2.close()

def main():
    Weekly()
    
if __name__ == "__main__":
    main()
