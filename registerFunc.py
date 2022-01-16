import psycopg2

import pgSQLconfig



def newAccount(login, psw, email):
    conn = None
    cursor = None

    create_script = '''CREATE TABLE IF NOT EXISTS loginbase(
                                    login varchar(40) PRIMARY KEY,
                                    password varchar(40) NOT NULL,
                                    email varchar(40) NOT NULL)'''

    insert_script = "INSERT INTO loginbase(login, password, email) VALUES(%s, %s, %s)"
    insert_value = (login, psw, email)

    try:
        conn = psycopg2.connect(
            host=pgSQLconfig.hostname,
            dbname=pgSQLconfig.database,
            user=pgSQLconfig.username,
            password=pgSQLconfig.pwd,
            port=pgSQLconfig.port_id) #connection to SQL function

        cursor = conn.cursor()
        cursor.execute(create_script)
        cursor.execute(insert_script, insert_value)


        conn.commit()

    except Exception as error:
        print("Connection Error: ")
        print(error)

    finally:
        if cursor is not None:
            cursor.close()

        if cursor is not None:
            conn.close()

    return 0

def chkInput (login, psw1, psw2, email):
    conn = None
    cursor = None

    import_script = ("SELECT * FROM loginbase")

    try:
        conn = psycopg2.connect(
            host=pgSQLconfig.hostname,
            dbname=pgSQLconfig.database,
            user=pgSQLconfig.username,
            password=pgSQLconfig.pwd,
            port=pgSQLconfig.port_id) #connection to SQL function

        cursor = conn.cursor()

        cursor.execute(import_script)
        database = cursor.fetchall()

        for record in database:
            if record[0] == login:
                return 1
            elif record[2] == email:
                return 2

        conn.commit()

    except Exception as error:
        print("Connection Error: ")
        print(error)

    finally:
        if cursor is not None:
            cursor.close()

        if cursor is not None:
            conn.close()

    if psw1==psw2:
        return 0
    else:
        return 3

def chkLogin(login):
    char = ["{","[","}","]",";",":","'",",","<",".",">","?","/","!","@","$","%","&","*","(",")","-","=","+"]
    for place in char:
        if place in login:
            return 1

    return 0

def chkEmail(email):

    if "@" and "." in email:
        if not " " in email:
            return 0

    return 1
