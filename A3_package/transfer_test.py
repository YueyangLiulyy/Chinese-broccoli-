import tempfile
import os
import io
import sys
import FrontEnd as fn


#transfer test case 

# transfer with valid information in ATM mode
def test1_0(capsys):
    user_input = ["login", "atm", "transfer", "1000327", "1000328", "001", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "Enter the amount of money you want to transfer: " +
                                "<--  Your transaction has been successfully made!  -->",
                                "==" * 34,
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t1.0out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t1.0in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing transfer with valid information in ATM mode

# transfer with valid information in agent mode
def test1_1(capsys):
    user_input = ["login", "agent", "transfer", "1000327", "1000328", "001", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "Enter the amount of money you want to transfer: " +
                                "<--  Your transaction has been successfully made!  -->",
                                "==" * 34,
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t1.1out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t1.1in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing transfer with valid information in agent mode


# transfer with incorrect sender's number in ATM mode
def test1_2(capsys):
    user_input = ["login", "atm", "transfer", "0000327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account cannot start with '0'",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t1.2out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t1.2in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test1_3(capsys):
    user_input = ["login", "atm", "transfer", "100327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account has to be exactly 7 digits",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t1.3out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t1.3in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test1_4(capsys):
    user_input = ["login", "atm", "transfer", "10003278", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account has to be exactly 7 digits",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t1.4out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t1.4in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test1_5(capsys):
    user_input = ["login", "atm", "transfer", "237@abc", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account cannot contain other characters",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t1.5out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t1.5in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing transfer with incorrect sender's number in ATM mode


# transfer with incorrect sender's number in agent mode
def test1_6(capsys):
    user_input = ["login", "agent", "transfer", "0000327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account cannot start with '0'",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t1.6out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t1.6in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test1_7(capsys):
    user_input = ["login", "agent", "transfer", "100327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account has to be exactly 7 digits",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t1.7out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t1.7in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test1_8(capsys):
    user_input = ["login", "agent", "transfer", "10003278", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account has to be exactly 7 digits",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t1.8out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t1.8in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test1_9(capsys):
    user_input = ["login", "agent", "transfer", "237@abc", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "The account cannot contain other characters",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t1.9out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t1.9in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing transfer with incorrect sender's number in agent mode


# transfer with incorrect receiver's number in ATM mode
def test2_0(capsys):
    user_input = ["login", "atm", "transfer", "1000327", "0008298", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " + 
                                "The account cannot start with '0'",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t2.0out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t2.0in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test2_1(capsys):
    user_input = ["login", "atm", "transfer", "1000327", "8298", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " + 
                                "The account has to be exactly 7 digits",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t2.1out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t2.1in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test2_2(capsys):
    user_input = ["login", "atm", "transfer", "1000327", "10000327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " + 
                                "The account has to be exactly 7 digits",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t2.2out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t2.2in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test2_3(capsys):
    user_input = ["login", "atm", "transfer", "1000327", "237@abc", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " + 
                                "The account cannot contain other characters",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t2.3out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t2.3in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing transfer with incorrect sender's number in ATM mode


# transfer with incorrect receiver's number in agent mode
def test2_4(capsys):
    user_input = ["login", "agent", "transfer", "1000327", "0008298", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " + 
                                "The account cannot start with '0'",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t2.4out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t2.4in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
    

def test2_5(capsys):
    user_input = ["login", "agent", "transfer", "1000327", "8298", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " + 
                                "The account has to be exactly 7 digits",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t2.5out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t2.5in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test2_6(capsys):
    user_input = ["login", "agent", "transfer", "1000327", "10000327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " + 
                                "The account has to be exactly 7 digits",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t2.6out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t2.6in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test2_7(capsys):
    user_input = ["login", "agent", "transfer", "1000327", "237@abc", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " + 
                                "The account cannot contain other characters",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t2.7out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t2.7in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing transfer with incorrect sender's number in agent mode


# transfer with non-exist sender's account in ATM mode 
def test2_8(capsys):
    user_input = ["login", "atm", "transfer", "1000327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "No matching account found!", 
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t2.8out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t2.8in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing transfer with non-exist sender's account in ATM mode

# transfer with non-exist receiver's account in ATM mode 
def test2_9(capsys):
    user_input = ["login", "atm", "transfer", "1000327", "1000328", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "No matching account found!", 
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t2.9out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t2.9in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing transfer with non-exist receiver's account in ATM mode

# transfer with non-exist sender's account in agent mode 
def test3_0(capsys):
    user_input = ["login", "agent", "transfer", "1000327", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "No matching account found!", 
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t3.0out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t3.0in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing transfer with non-exist sender's account in agent mode

# transfer with non-exist receiver's account in agent mode 
def test3_1(capsys):
    user_input = ["login", "agent", "transfer", "1000327", "1000328", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "No matching account found!", 
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t3.1out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t3.1in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing transfer with non-exist receiver's account in agent mode


# transfer with invalid amount in ATM mode
def test3_2(capsys):
    user_input = ["login", "atm", "transfer", "1000327", "1000328", "1", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "Enter the amount of money you want to transfer: " + 
                                "Invalid amount, please try again!",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t3.2out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t3.2in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test3_3(capsys):
    user_input = ["login", "atm", "transfer", "1000327", "1000328", "100000000", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "Enter the amount of money you want to transfer: " + 
                                "Invalid amount, please try again!",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t3.3out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t3.3in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test3_4(capsys):
    user_input = ["login", "atm", "transfer", "1000327", "1000328", "100@abc", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "Enter the amount of money you want to transfer: " + 
                                "Invalid amount, please try again!",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t3.4out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t3.4in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing transfer with invalid amount in ATM mode

# transfer with invalid amount in agent mode
def test3_5(capsys):
    user_input = ["login", "agent", "transfer", "1000327", "1000328", "1", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "Enter the amount of money you want to transfer: " + 
                                "Invalid amount, please try again!",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t3.5out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t3.5in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test3_6(capsys):
    user_input = ["login", "agent", "transfer", "1000327", "1000328", "100000000", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "Enter the amount of money you want to transfer: " + 
                                "Invalid amount, please try again!",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t3.6out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t3.6in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )

def test3_7(capsys):
    user_input = ["login", "agent", "transfer", "1000327", "1000328", "100@abc", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered agent mode.",
                                "Hello, welcome to the agent mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "Enter the amount of money you want to transfer: " + 
                                "Invalid amount, please try again!",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t3.7out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t3.7in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing transfer with invalid amount in agent mode


# test the limit of each transfer 
def test3_8(capsys):
    user_input = ["login", "atm", "transfer", "1000327", "1000328", "1000001", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "Enter the amount of money you want to transfer: " +
                                "The limit of each transfer is $10,000, please retype: ",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t3.8out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t3.8in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing for the limit of each transfer 


# test the daily limit of transfer 
def test3_9(capsys):
    user_input = ["login", "atm", "transfer", "1000327", "1000328", "500000", 
                  "transfer", "1000327", "1000328", "500001", "logout"]
    expected_terminal_output = ["Welcome to the front end: ",
                                "Successfully login.",
                                "Select mode to enter: ",
                                "Successfully entered ATM mode.",
                                "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "Enter the amount of money you want to transfer: " +
                                "<--  Your transaction has been successfully made!  -->",
                                "=="*34,
                                 "Hello, welcome to the ATM mode, please type the transaction you want to make: ",
                                "Enter your account please: " +
                                "Enter the payee account please: " +
                                "Enter the amount of money you want to transfer: " +
                                "The daliy limit of transfer is $10,000, " + 
                                "you have transferred $5000.00, please try again.",
                                "--> " + 
                                "Successfully logout.",
                                "Welcome to the front end: "
    ]
    expected_outputFile = "testCase/transfer/output/t3.9out.txt"
    run_app(
        capsys = capsys,
        accountList= "testCase/transfer/input/t3.9in.txt",
        terminal_input = user_input,
        expected_terminal_tails = expected_terminal_output,
        expected_output_file = expected_outputFile
    )
# finish testing for the daily limit of transfer 


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
    # print(result)
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