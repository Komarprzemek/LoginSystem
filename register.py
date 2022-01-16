import registerFunc
import stdiomask

def register():
    ifnewuser = 0  # checking if user is in base
    goodLogin = 1  # until login got good syntax => 1
    goodEmail = 1  # until login got good syntax => 1

    while goodEmail:  # until tested good with chkEmail
        email = input("Enter your email:")
        goodEmail = registerFunc.chkEmail(email)
        if goodEmail:
            print("Email got syntax error try again: ")

    while goodLogin:  # until tested good with chkLogin
        login = input("Enter the login:")
        goodLogin = registerFunc.chkLogin(login)
        if goodLogin:
            print("Login got syntax error try again: ")

    psw1 = stdiomask.getpass()  # taking password from user
    psw2 = stdiomask.getpass("Re-enter password for verification: ")  # taking password to test

    properInput = registerFunc.chkInput(login, psw1, psw2, email)  # testing all inputted data

    while True:
        try:
            reg_confirm = int(input("Press 0 cancel, press 1 to accept data:"))
            if reg_confirm == 0:
                print("You cancel registration")
                return 1

            elif reg_confirm == 1:
                if properInput == 1:
                    print("Login exist in database")

                elif properInput == 2:
                    print("Email exist in database")

                elif properInput == 3:
                    print("Password do not match")

                elif ifnewuser == 0:
                    registerFunc.newAccount(login, psw1, email)

                break
            else:
                print("Wrong command try again")

        except ValueError:  # Wrong command given by user
            print("Wrong command try again")

    return 0