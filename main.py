import login  # login function
import register  # register function

menu = 0  # start menu == 0

while menu == 0:  # Login / Register screen

    chkpsw = None  # checking psw for registration
    properInput = None  # checking the user input
    login_access = None

    try:
        func = int(input(
            "Do you want to register new account (type: 0), login (type: 1), cancel (type:2) "))  # asking user to
                                                                                                  # define what to do

        if func == 0:  # Register function
            register.register() # entering register function


        elif func == 1:  # log in function
            login_access = login.login()  # entering login function

        elif func == 2:  # break from main loop
            break

        else:  # user enter wrong command
            print("Wrong command try again")

        if login_access == 1:
            print("asd")
            menu = 1


    except ValueError:  # Wrong command given by user
        print("Wrong command try again")

