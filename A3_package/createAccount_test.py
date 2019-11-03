import tempfile
import os
import io
import sys
import FrontEnd as fn
import filecmp

# createaccount test case

# createaccount with valid information
def test1_0(capsys):
    user_input = ["login", "agent", "createacct", "1000666", "TheCreatedAccount01", "logout"]
    expected_terminal_output = ['Welcome to the front end: ',
                   'Successfully login.',
                   'Select mode to enter: ',
                   'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ',
                   'Enter the new account number you want to create please: '+
                   'Enter the account name for the new account: '+
                   '<--  Your transaction has been successfully made!  -->',
                   '==' * 34,
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ',
                   'Successfully logout.',
                   'Welcome to the front end: ']
    expected_outputFile = "testCase/createacct/output/T1.0 out.txt"
    run_app(
        capsys=capsys,
        accountList="testCase/createacct/input/T1.0 in.txt",
        terminal_input=user_input,
        expected_terminal_tails=expected_terminal_output,
        expected_output_file=expected_outputFile
    )

# createaccount command, failed case with the same account
def test1_1(capsys):
    user_input = ["login", "agent", "createacct", "1000600", "logout"]
    expected_terminal_output = ['Welcome to the front end: ',
                   'Successfully login.',
                   'Select mode to enter: ',
                   'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ',
                   'Enter the new account number you want to create please: '+
                   'The account already exist.',
                   '--> '+ 
                   'Successfully logout.',
                   'Welcome to the front end: ']
    expected_outputFile = "testCase/createacct/output/T1.1 out.txt"
    run_app(
        capsys=capsys,
        accountList="testCase/createacct/input/T1.1 in.txt",
        terminal_input=user_input,
        expected_terminal_tails=expected_terminal_output,
        expected_output_file=expected_outputFile
    )

# createaccount command, failed case with the account number which is more than seven decimal digits
def test1_2(capsys):
    user_input = ["login", "agent", "createacct", "100060100000", "logout"]
    expected_terminal_output = ['Welcome to the front end: ',
                   'Successfully login.',
                   'Select mode to enter: ',
                   'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ',
                   'Enter the new account number you want to create please: '+
                   'The account has to be exactly 7 digits',
                   '--> '+
                   'Successfully logout.',
                   'Welcome to the front end: ']
    expected_outputFile = "testCase/createacct/output/T1.2 out.txt"
    run_app(
        capsys=capsys,
        accountList="testCase/createacct/input/T1.2 in.txt",
        terminal_input=user_input,
        expected_terminal_tails=expected_terminal_output,
        expected_output_file=expected_outputFile
    )

# createaccount command, failed case with the account number which is less than seven decimal digits
def test1_3(capsys):
    user_input = ["login", "agent", "createacct", "1000", "logout"]
    expected_terminal_output = ['Welcome to the front end: ',
                   'Successfully login.',
                   'Select mode to enter: ',
                   'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ',
                   'Enter the new account number you want to create please: '+
                   'The account has to be exactly 7 digits',
                   '--> '+
                   'Successfully logout.',
                   'Welcome to the front end: ']
    expected_outputFile = "testCase/createacct/output/T1.3 out.txt"
    run_app(
        capsys=capsys,
        accountList="testCase/createacct/input/T1.3 in.txt",
        terminal_input=user_input,
        expected_terminal_tails=expected_terminal_output,
        expected_output_file=expected_outputFile
    )

# createaccount command, failed case with the account number which beginning with 0
def test1_4(capsys):
    user_input = ["login", "agent", "createacct", "0000601", "logout"]
    expected_terminal_output = ['Welcome to the front end: ',
                   'Successfully login.',
                   'Select mode to enter: ',
                   'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ',
                   'Enter the new account number you want to create please: '+
                   'The account cannot start with \'0\'',
                   '--> '+
                   'Successfully logout.',
                   'Welcome to the front end: ']
    expected_outputFile = "testCase/createacct/output/T1.4 out.txt"
    run_app(
        capsys=capsys,
        accountList="testCase/createacct/input/T1.4 in.txt",
        terminal_input=user_input,
        expected_terminal_tails=expected_terminal_output,
        expected_output_file=expected_outputFile
    )

# createaccount command, failed case with the account number which includes the alphanumeric characters
def test1_5(capsys):
    user_input = ["login", "agent", "createacct", "1aaaaa1", "logout"]
    expected_terminal_output = ['Welcome to the front end: ',
                   'Successfully login.',
                   'Select mode to enter: ',
                   'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ',
                   'Enter the new account number you want to create please: '+
                   'The account cannot contain other characters',
                   '--> '+
                   'Successfully logout.',
                   'Welcome to the front end: ']
    expected_outputFile = "testCase/createacct/output/T1.5 out.txt"
    run_app(
        capsys=capsys,
        accountList="testCase/createacct/input/T1.5 in.txt",
        terminal_input=user_input,
        expected_terminal_tails=expected_terminal_output,
        expected_output_file=expected_outputFile
    )

# createaccount command, failed case with the account name which is more than 30 alphanumeric characters
def test1_6(capsys):
    user_input = ["login", "agent", "createacct", "1000601", "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT", "logout"]
    expected_terminal_output = ['Welcome to the front end: ',
                   'Successfully login.',
                   'Select mode to enter: ',
                   'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ',
                   'Enter the new account number you want to create please: '+
                   'Enter the account name for the new account: '+
                   'the account name should between 3 and 30 alphanumeric characters: ',
                   'Enter the account name for the new account: '+
                   'Successfully logout.',
                   'Welcome to the front end: ']
    expected_outputFile = "testCase/createacct/output/T1.6 out.txt"
    run_app(
        capsys=capsys,
        accountList="testCase/createacct/input/T1.6 in.txt",
        terminal_input=user_input,
        expected_terminal_tails=expected_terminal_output,
        expected_output_file=expected_outputFile
    )

# createaccount command, failed case with the account name which is less than 3 alphanumeric characters
def test1_7(capsys):
    user_input = ["login", "agent", "createacct", "1000601", "TT", "logout"]
    expected_terminal_output = ['Welcome to the front end: ',
                   'Successfully login.',
                   'Select mode to enter: ',
                   'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ',
                   'Enter the new account number you want to create please: '+
                   'Enter the account name for the new account: '+
                   'the account name should between 3 and 30 alphanumeric characters: ',
                   'Enter the account name for the new account: '+
                   'Successfully logout.',
                   'Welcome to the front end: ']
    expected_outputFile = "testCase/createacct/output/T1.7 out.txt"
    run_app(
        capsys=capsys,
        accountList="testCase/createacct/input/T1.7 in.txt",
        terminal_input=user_input,
        expected_terminal_tails=expected_terminal_output,
        expected_output_file=expected_outputFile
    )

# createaccount command, failed case with the account name which beginning with a space
def test1_8(capsys):
    user_input = ["login", "agent", "createacct", "1000601", "   CreatedAccount01", "logout"]
    expected_terminal_output = ['Welcome to the front end: ',
                   'Successfully login.',
                   'Select mode to enter: ',
                   'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ',
                   'Enter the new account number you want to create please: '+
                   'Enter the account name for the new account: '+
                   'the account name should not beginning or ending with a space: ',
                   'Enter the account name for the new account: '+
                   'Successfully logout.',
                   'Welcome to the front end: ']
    expected_outputFile = "testCase/createacct/output/T1.8 out.txt"
    run_app(
        capsys=capsys,
        accountList="testCase/createacct/input/T1.8 in.txt",
        terminal_input=user_input,
        expected_terminal_tails=expected_terminal_output,
        expected_output_file=expected_outputFile
    )

# createaccount command, failed case with the account name which ending with a space
def test1_9(capsys):
    user_input = ["login", "agent", "createacct", "1000601", "TheCreatedAccount ", "logout"]
    expected_terminal_output = ['Welcome to the front end: ',
                   'Successfully login.',
                   'Select mode to enter: ',
                   'Successfully entered agent mode.',
                   'Hello, welcome to the agent mode, please type the transaction you want to make: ',
                   'Enter the new account number you want to create please: '+
                   'Enter the account name for the new account: '+
                   'the account name should not beginning or ending with a space: ',
                   'Enter the account name for the new account: '+
                   'Successfully logout.',
                   'Welcome to the front end: ']
    expected_outputFile = "testCase/createacct/output/T1.9 out.txt"
    run_app(
        capsys=capsys,
        accountList="testCase/createacct/input/T1.9 in.txt",
        terminal_input=user_input,
        expected_terminal_tails=expected_terminal_output,
        expected_output_file=expected_outputFile
    )

def run_app(
        capsys,
        accountList,
        terminal_input,
        expected_terminal_tails,
        expected_output_file=None):

    temp_fd, temp_file = tempfile.mkstemp()
    sys.argv = ['FrontEnd.py', accountList, temp_file]

    # set input

    result = "\n".join(terminal_input)
    # print(result)
    sys.stdin = io.StringIO(result)

    # run the FrontEnd.py
    fn.main()

    # capture terminal output / errors
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




