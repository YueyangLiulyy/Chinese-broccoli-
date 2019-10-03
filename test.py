import sys


def test():
    for liner in sys.stdin:
        line = liner.strip()
        print("this is" + line)
        if line == "2":
            return "nihao"

def main():
    test()


main()

