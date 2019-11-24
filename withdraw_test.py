import pytest
import os
import io
import sys
import backend as bn


# successfully withdraw from targeted account 
# targeted account is at the bottom of master file
def test1_0(capsys):
    expected_outputFile1 = "testCase/withdraw_decision_coverage/output/master1.0.txt"
    expected_outputFile2 = "testCase/withdraw_decision_coverage/output/account1.0.txt"
    run_app(
        capsys = capsys,
        masterFile= "testCase/withdraw_decision_coverage/input/master1.0.txt",
        transactionFile = "testCase/withdraw_decision_coverage/input/summary1.0.txt",
        expected_terminal_tails = None,
        expected_output_file1 = expected_outputFile1,
        expected_output_file2 = expected_outputFile2
    )
# end test1_0


# successfully withdraw from targeted account 
# targeted account is at the top of master file
def test1_1(capsys):
    expected_outputFile1 = "testCase/withdraw_decision_coverage/output/master1.1.txt"
    expected_outputFile2 = "testCase/withdraw_decision_coverage/output/account1.1.txt"
    run_app(
        capsys = capsys,
        masterFile= "testCase/withdraw_decision_coverage/input/master1.1.txt",
        transactionFile = "testCase/withdraw_decision_coverage/input/summary1.1.txt",
        expected_terminal_tails = None,
        expected_output_file1 = expected_outputFile1,
        expected_output_file2 = expected_outputFile2
    )
# end test1_1


# Unsuccessfully withdraw, due to no matching account found 
def test1_2(capsys):
    terminal_tails = ["Transaction: WDR 0000000 10000 1000330 *** is invalid!", "Due to: no matching account found!", "program terminated!"]
    expected_outputFile1 = None
    expected_outputFile2 = None
    run_app(
        capsys = capsys,
        masterFile= "testCase/withdraw_decision_coverage/input/master1.2.txt",
        transactionFile = "testCase/withdraw_decision_coverage/input/summary1.2.txt",
        expected_terminal_tails = terminal_tails,
        expected_output_file1 = expected_outputFile1,
        expected_output_file2 = expected_outputFile2
    )
# end test1_2

# Unsuccessfully withdraw, due to insufficient balances  
def test1_3(capsys):
    terminal_tails = ["Transaction: WDR 0000000 100000 1000328 *** is invalid!", "Due to: insufficient balance!", "program terminated!"]
    expected_outputFile1 = None
    expected_outputFile2 = None
    run_app(
        capsys = capsys,
        masterFile= "testCase/withdraw_decision_coverage/input/master1.3.txt",
        transactionFile = "testCase/withdraw_decision_coverage/input/summary1.3.txt",
        expected_terminal_tails = terminal_tails,
        expected_output_file1 = expected_outputFile1,
        expected_output_file2 = expected_outputFile2
    )
# end test1_3


# Unsuccessfully withdraw, due to the account information is longer than 46 characters.
def test1_4(capsys):
    terminal_tails = ["Transaction: WDR 0000000 10000 1000328 *** is invalid!", "Due to: Invalid length!", "program terminated!"]
    expected_outputFile1 = None
    expected_outputFile2 = None
    run_app(
        capsys = capsys,
        masterFile= "testCase/withdraw_decision_coverage/input/master1.4.txt",
        transactionFile = "testCase/withdraw_decision_coverage/input/summary1.4.txt",
        expected_terminal_tails = terminal_tails,
        expected_output_file1 = expected_outputFile1,
        expected_output_file2 = expected_outputFile2
    )
# end test1_4

def run_app(
    capsys,
    masterFile,
    transactionFile,
    expected_terminal_tails=None,
    expected_output_file1=None,
    expected_output_file2=None):

    sys.argv=['backend.py', transactionFile, masterFile]

    # run the FrontEnd.py
    bn.main()

    #capture terminal output / errors
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # compare terminal outputs 
    if expected_terminal_tails is not None:
        for i in range(0, len(expected_terminal_tails)):
            print(len(expected_terminal_tails))
            assert expected_terminal_tails[i] == out_lines[i]

    # compare output file to the expected output file
    if expected_output_file1 is not None and expected_output_file2 is not None:
        targetDir1 = os.path.dirname(__file__) + "/out/" + "masterAccount.txt"
        targetDir2 = os.path.dirname(__file__) + "/out/" + "accountList.txt"
        with open(targetDir1, 'r') as temp_file_of:
            content = temp_file_of.read()
        with open(expected_output_file1, 'r') as exp_file_of:
            exp_content = exp_file_of.read()
            assert content == exp_content
        
        with open(targetDir2, 'r') as temp_file_of:
            content = temp_file_of.read()
        with open(expected_output_file2, 'r') as exp_file_of:
            exp_content = exp_file_of.read()
            assert content == exp_content
    
