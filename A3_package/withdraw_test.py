import tempfile
import os
import io
import sys
import FrontEnd as fn


# withdraw test case 

# successfully withdraw in ATM mode 
def test1_0(capsys):
    user_input = ["login", "atm", "withdraw", "1000327", "100000", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "<--  Your transaction has been successfully made!  -->",
                                "=="*34,
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t1.0out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t1.0in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing successfuly withdraw in ATM mode 

# successfully withdraw in agent mode
def test1_1(capsys):
    user_input = ["login", "agent", "withdraw", "1000327", "100000", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "<--  Your transaction has been successfully made!  -->",
                                "=="*34,
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t1.1out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t1.1in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing successfuly withdraw in agent mode


# test withdraw with invalid acccount in ATM mode
def test1_2(capsys):
    user_input = ["login", "atm", "withdraw", "0000327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account cannot start with '0'" ,
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t1.2out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t1.2in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test1_3(capsys):
    user_input = ["login", "atm", "withdraw", "327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account has to be exactly 7 digits" ,
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t1.3out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t1.3in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test1_4(capsys):
    user_input = ["login", "atm", "withdraw", "10003278", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account has to be exactly 7 digits" ,
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t1.4out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t1.4in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test1_5(capsys):
    user_input = ["login", "atm", "withdraw", "321@abc", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account cannot contain other characters" ,
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t1.5out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t1.5in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing with invalid account in ATM mode


# test withdraw with invalid acccount in agent mode
def test1_6(capsys):
    user_input = ["login", "agent", "withdraw", "0000327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account cannot start with '0'" ,
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t1.6out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t1.6in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test1_7(capsys):
    user_input = ["login", "agent", "withdraw", "327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account has to be exactly 7 digits" ,
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t1.7out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t1.7in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test1_8(capsys):
    user_input = ["login", "agent", "withdraw", "10003278", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account has to be exactly 7 digits" ,
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t1.8out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t1.8in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test1_9(capsys):
    user_input = ["login", "agent", "withdraw", "321@abc", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account cannot contain other characters" ,
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t1.9out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t1.9in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing with invalid account in agent mode


# test withdraw with non-exist account in ATM mode 
def test2_0(capsys):
    user_input = ["login", "atm", "withdraw", "1000327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "No matching account found!" ,
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t2.0out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t2.0in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing withdraw with non-exist account in ATM mode

# test withdraw with non-exist account in agnet mode 
def test2_1(capsys):
    user_input = ["login", "agent", "withdraw", "1000327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "No matching account found!" ,
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t2.1out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t2.1in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing withdraw with non-exist account in agent mode 


# test withdraw with invalid amount in ATM mode
def test2_2(capsys):
    user_input = ["login", "atm", "withdraw", "1000327", "0", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "Invalid amount, please try again!",
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t2.2out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t2.2in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test2_3(capsys):
    user_input = ["login", "atm", "withdraw", "1000327", "100000000", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "Invalid amount, please try again!",
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t2.3out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t2.3in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test2_4(capsys):
    user_input = ["login", "atm", "withdraw", "1000327", "jk520@", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "Invalid amount, please try again!",
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t2.4out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t2.4in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing withdraw with invalid amount in ATM mode

# test withdraw with invalid amount in agent mode
def test2_5(capsys):
    user_input = ["login", "agent", "withdraw", "1000327", "0", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "Invalid amount, please try again!",
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t2.5out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t2.5in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test2_6(capsys):
    user_input = ["login", "agent", "withdraw", "1000327", "100000000", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "Invalid amount, please try again!",
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t2.6out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t2.6in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test2_7(capsys):
    user_input = ["login", "agent", "withdraw", "1000327", "jk520@", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "Invalid amount, please try again!",
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t2.7out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t2.7in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing withdraw with invalid amount in agent mode


# test the each withdraw limit
def test2_8(capsys):
    user_input = ["login", "atm", "withdraw", "1000327", "100001", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "The limit of each withdraw is $1,000, please retype: ",
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t2.8out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t2.8in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing for each withdraw limit 


# test the daily limit in ATM 
def test2_9(capsys):
    user_input = ["login", "atm", "withdraw", "1000327", "100000", 
                  "withdraw", "1000327", "100000",  
                  "withdraw", "1000327", "100000",  
                  "withdraw", "1000327", "100000",  
                  "withdraw", "1000327", "100000",  
                  "withdraw", "1000327", "001",  "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",           # 1st repeated
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "<--  Your transaction has been successfully made!  -->",
                                "=="*34,                                                                                    
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",           # 2nd repeated 
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "<--  Your transaction has been successfully made!  -->",
                                "=="*34,
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",           # 3rd repeated 
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "<--  Your transaction has been successfully made!  -->",
                                "=="*34,
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",           # 4th repeated 
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "<--  Your transaction has been successfully made!  -->",
                                "=="*34,
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",           # 5th repeated 
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "<--  Your transaction has been successfully made!  -->",
                                "=="*34,
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",           # 6th exceed limit 
                                "Enter your account please: " +
                                "Enter the amount of money you want to withdraw: " +
                                "The daliy limit of withdraw is $5,000, "+
                                "you have withdrawn $5000.00, please try again.",
                                "--> " +
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/withdraw/output/t2.9out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/withdraw/input/t2.9in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing the daily limit in ATM mode 

def run_app(
    capsys,
    accountList,
    terminal_input,
    expected_terminal_tails,
    expected_output_file=None):

    temp_fd, temp_file = tempfile.mkstemp()
    sys.argv=['FrontEnd.py', accountList, temp_file]

    # set input
    result = "\n".join(terminal_input)
    sys.stdin = io.StringIO(result)

    # run the FrontEnd.py
    fn.main()

    #capture terminal output / errors
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # compare terminal outputs 
    for i in range(0, len(expected_terminal_tails)):
        assert expected_terminal_tails[i] == out_lines[i]

    # compare output file to teh expected output file
    if expected_output_file is not None:
        with open(temp_file, 'r') as temp_file_of:
            content = temp_file_of.read()
            with open(expected_output_file, 'r') as exp_file_of:
                exp_content = exp_file_of.read()
                assert content == exp_content
    
    # clean up
    os.close(temp_fd)
    os.remove(temp_file)