def verifyAccount(account):
    if len(account) != 7:
        return False
    elif account[0] == '0':
        return False
    elif not account.isdigit():
        return False
    else:
        return True

def verifyAmount(amount):
    if len(amount) < 3 or len(amount) > 8:
        return False
    elif not amount.isdigit():
        return False
    else:
        return True


def main():
    verifyAccount("1102345")

main()


    
