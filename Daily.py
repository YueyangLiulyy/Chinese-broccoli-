import frontEnd as fn
import backEnd as bn
import sys
import os

class daily:
    def __init__(self, day):
        self.day = "day" + str(day)                                             # processing day corresponding to a directory 
        self.rootDir = os.path.join(os.path.dirname(__file__), self.day)        # all files read and written within the directory
        self.merge_file_from = os.path.join(self.rootDir, "frontend_out")       # merge files from frontend output
        self.merge_file_to = os.path.join(self.rootDir, "backend_in")           # merged file as backend input
        name = "mergedSummaryFile.txt"                                          # the merged file name
        self.open_frontend()
        self.write_file(name)
        self.pass_backend(name)

    # run the fronted end
    def open_frontend(self):
        write_to = os.path.join(self.merge_file_from, "transaction.txt")        # frontend ouput file write to 
        trans = os.path.join(self.rootDir, "frontend_in/trans.txt")             # user input come from the file 
        account_list = os.path.join(self.rootDir, "frontend_in/account.txt")    # same day, the same account list 
        for i in range(1,4):                                                    # 1, 2, 3 sessions 
            write_to_temp = os.path.splitext(write_to)[0] + str(i) + ".txt"
            trans_temp = os.path.splitext(trans)[0] + str(i) + ".txt"
            sys.argv = ["frontEnd.py", account_list, write_to_temp]
            f= open(trans_temp, "r")
            sys.stdin = f
            fn.main()
            f.close()

    # run the backend
    def pass_backend(self, name):
        backend_inputDir = self.merge_file_to
        masterAcc = os.path.join(backend_inputDir, "masterAccount.txt")
        mergeTrans = os.path.join(backend_inputDir, name)                      
        sys.argv = ['backEnd.py', mergeTrans, masterAcc]
        bn.main()

    # write the merged file
    def write_file(self, name):
        mergered_file = self.read_merge_file(self.merge_file_from)
        targetFile = os.path.join(self.merge_file_to, name)
        if not os.path.exists(self.merge_file_to):
            os.makedirs(self.merge_file_to)
        with open(targetFile, "w") as f:
            f.writelines(mergered_file)
        
    # Read files and merge them 
    def read_merge_file(self, targetDir):
        flist = []
        for filename in os.listdir(targetDir):
            if filename.endswith('.txt'):
                with open(os.path.join(targetDir,filename)) as f:
                    flist += f.readlines()[:-1]
        flist.append("EOS")
        return flist

def main():
    daily(1)
    
if __name__ == "__main__":
    main()