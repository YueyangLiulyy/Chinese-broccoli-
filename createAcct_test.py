import pytest
import os
import io
import sys
import backend as bn


# account creation test case

# Unsuccessfully account creation, due to account already exists
def test1_0(capsys):
    expected_outputFile1 = None
    expected_outputFile2 = None
    run_app(
        capsys=capsys,
        masterFile="testCase/createAcct_Basic_Block_coverage/input/master1.0.txt",
        transactionFile="testCase/createAcct_Basic_Block_coverage/input/summary1.0.txt",
        expected_terminal_tails=['Transaction: NEW 1000500 000 0000000 Account02 is invalid!', 'Due to: account already exists!', 'program terminated!'],
        expected_output_file1=expected_outputFile1,
        expected_output_file2=expected_outputFile2
    )

# Successfully account creation, the created account is in the second line of the new master file
def test1_1(capsys):
    expected_outputFile1 = "testCase/createAcct_Basic_Block_coverage/output/master1.1.txt"
    expected_outputFile2 = "testCase/createAcct_Basic_Block_coverage/output/account1.1.txt"
    run_app(
        capsys=capsys,
        masterFile="testCase/createAcct_Basic_Block_coverage/input/master1.1.txt",
        transactionFile="testCase/createAcct_Basic_Block_coverage/input/summary1.1.txt",
        expected_terminal_tails=[],
        expected_output_file1=expected_outputFile1,
        expected_output_file2=expected_outputFile2
    )

# Successfully account creation, the created account is in the first line of the new master file
def test1_2(capsys):
    expected_outputFile1 = "testCase/createAcct_Basic_Block_coverage/output/master1.2.txt"
    expected_outputFile2 = "testCase/createAcct_Basic_Block_coverage/output/account1.2.txt"
    run_app(
        capsys=capsys,
        masterFile="testCase/createAcct_Basic_Block_coverage/input/master1.2.txt",
        transactionFile="testCase/createAcct_Basic_Block_coverage/input/summary1.2.txt",
        expected_terminal_tails=[],
        expected_output_file1=expected_outputFile1,
        expected_output_file2=expected_outputFile2
    )

# Unsuccessfully account creation, due to invalid length
def test1_3(capsys):
    expected_outputFile1 = None
    expected_outputFile2 = None
    run_app(
        capsys=capsys,
        masterFile="testCase/createAcct_Basic_Block_coverage/input/master1.3.txt",
        transactionFile="testCase/createAcct_Basic_Block_coverage/input/summary1.3.txt",
        expected_terminal_tails=['Transaction: NEW 1000550 000 0000000 Account04aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa is invalid!', 'Due to: invalid length!', 'program terminated!'],
        expected_output_file1=expected_outputFile1,
        expected_output_file2=expected_outputFile2
    )

def run_app(
        capsys,
        masterFile,
        transactionFile,
        expected_terminal_tails,
        expected_output_file1=None,
        expected_output_file2=None):
    sys.argv = ['backend.py', transactionFile, masterFile]

    # run the FrontEnd.py
    bn.main()

    # capture terminal output / errors
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()
    print(out_lines)
    # compare terminal outputs
    if expected_terminal_tails is not None:
        for i in range(0, len(expected_terminal_tails)):
            assert expected_terminal_tails[i] == out_lines[i]

    # compare output file to teh expected output file

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
