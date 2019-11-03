import tempfile
import os
import io
import sys
import FrontEnd as fn


def test1_0(capsys):
    user_input = ["login", "atm", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered ATM mode.',
                   'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)
    
    
def test1_1(capsys):
    user_input = ["login", "agent", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)
    
    
def test1_2(capsys):
    user_input = ["login", "atm", "deposit", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered ATM mode.',
                   'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Enter your account please: Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)
    
    
def test1_3(capsys):
    user_input = ["login", "atm", "transfer", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered ATM mode.',
                   'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Enter your account please: Successfully logout.', 'Welcome to the front end: ']    
    helper(capsys, user_input, user_output)
    
    
def test1_4(capsys):
    user_input = ["login", "atm", "withdraw", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered ATM mode.',
                   'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Enter your account please: Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test1_5(capsys):
    user_input = ["login", "atm","createacct", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered ATM mode.',
                   'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'The operation is not supported in ATM mode',
                   'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test1_6(capsys):
    user_input = ["login", "atm","deleteacct", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered ATM mode.',
                   'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'The operation is not supported in ATM mode',
                   'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test1_7(capsys):
    user_input = ["login", "agent","deposit", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ', 'Enter your account please: Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)
    
def test1_8(capsys):
    user_input = ["login", "agent", "withdraw", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ', 'Enter your account please: Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test1_9(capsys):
    user_input = ["login", "agent", "transfer", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ', 'Enter your account please: Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test2_0(capsys):
    user_input = ["login", "agent", "deleteacct", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ', 'Enter the account number you want to delete please: Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test2_1(capsys):
    user_input = ["login", "agent", "createacct", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ', 'Enter the new account number you want to create please: Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test2_2(capsys):
    user_input = ["login", "atm","login", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Successfully entered ATM mode.',
                   'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Check your input, and try again!', 'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test2_3(capsys):
    user_input = ["login", "login", "atm", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ', 'Error:Invalid mode choice, please input a valid mode choice!',
                   'Select mode to enter: ', 'Successfully entered ATM mode.', 'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test2_4(capsys):
    user_input = ["transfer", "login", "atm", "logout"]
    user_output = ['Welcome to the front end: ', 'Error:Please login first!', 'Welcome to the front end: ', 'Successfully login.',
                   'Select mode to enter: ', 'Successfully entered ATM mode.', 'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test2_5(capsys):
    user_input = ["deposit", "login", "atm", "logout"]
    user_output = ['Welcome to the front end: ', 'Error:Please login first!', 'Welcome to the front end: ', 'Successfully login.',
                   'Select mode to enter: ', 'Successfully entered ATM mode.', 'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test2_6(capsys):
    user_input = ["withdraw", "login", "atm", "logout"]
    user_output = ['Welcome to the front end: ', 'Error:Please login first!', 'Welcome to the front end: ', 'Successfully login.',
                   'Select mode to enter: ', 'Successfully entered ATM mode.', 'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test2_7(capsys):
    user_input = ["createacct", "login", "atm", "logout"]
    user_output = ['Welcome to the front end: ', 'Error:Please login first!', 'Welcome to the front end: ', 'Successfully login.',
                   'Select mode to enter: ', 'Successfully entered ATM mode.', 'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test2_8(capsys):
    user_input = ["deleteacct", "login", "atm", "logout"]
    user_output = ['Welcome to the front end: ', 'Error:Please login first!', 'Welcome to the front end: ',
                   'Successfully login.', 'Select mode to enter: ', 'Successfully entered ATM mode.', 'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test2_9(capsys):
    user_input = ["deposssit","login", "atm", "logout"]
    user_output = ['Welcome to the front end: ', 'Error:Please login first!', 'Welcome to the front end: ',
                   'Successfully login.', 'Select mode to enter: ', 'Successfully entered ATM mode.', 'Hello, welcome to the ATM mode, please type the transaction you want to make: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test3_0(capsys):
    user_input = ["loginn", "atm", "logout"]
    user_output = ['Welcome to the front end: ', 'Error:Please login first!', 'Welcome to the front end: ',
                   'Error:Please login first!', 'Welcome to the front end: ', 'Error:Please login first!', 'Welcome to the front end: ']
    run_app(
        capsys,
        accountList= "testCase/login/input/t1.0in.txt",
        terminal_input = user_input,
        expected_terminal_tails = user_output,
        expected_output_file = None
    )

    
def test3_1(capsys):
    user_input = ["login", "atma", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ',
                   'Error:Invalid mode choice, please input a valid mode choice!', 'Select mode to enter: ', 'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)

    
def test3_2(capsys):
    user_input = ["login", "logout"]
    user_output = ['Welcome to the front end: ', 'Successfully login.', 'Select mode to enter: ',
                   'Successfully logout.', 'Welcome to the front end: ']
    helper(capsys, user_input, user_output)


def helper(capsys, inputList, outputList):
    run_app(
        capsys,
        accountList= "testCase/login/input/t1.0in.txt",
        terminal_input = inputList,
        expected_terminal_tails = outputList,
        expected_output_file = "testCase/login/output/t1.0out.txt"
    )


def run_app(
    capsys,
    accountList,
    terminal_input,
    expected_terminal_tails,
    expected_output_file,
    ):


    # set input
    temp_fd, temp_file = tempfile.mkstemp()
    sys.argv=['FrontEnd.py', accountList, temp_file]
    

    result = os.linesep.join(terminal_input)
    sys.stdin = io.StringIO("\n".join(terminal_input))

    # run the FrontEnd.py
    fn.main()

    #capture terminal output / errors
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()
    # compare terminal outputs
    for i in range(1, len(expected_terminal_tails)):
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

