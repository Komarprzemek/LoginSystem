import loginFunc
import stdiomask

def login():

    login_access = 0  # return from checking password

    login = input("Enter the login:")  # entering login
    psw = stdiomask.getpass()  # entering password
    login_access = loginFunc.login(login, psw)  # checking access from db 1 -> fail 0 -> good login and psw

    if login_access == 1:  # if user put proper login and password
        print("Login successful")
        return 1

    elif login_access == 0:
        print("Login failed")
        return 0