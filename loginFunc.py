import psycopg2
import pgSQLconfig

def login(login, psw):
    conn = None
    cursor = None

    import_script = ("SELECT * FROM loginbase")

    try:
        conn = psycopg2.connect(
            host=pgSQLconfig.hostname,
            dbname=pgSQLconfig.database,
            user=pgSQLconfig.username,
            password=pgSQLconfig.pwd,
            port=pgSQLconfig.port_id)  # connection to SQL function

        cursor = conn.cursor()

        cursor.execute(import_script)
        database = cursor.fetchall()

        for record in database:
           if login == record [0]:
               if psw == record[1]:
                   return 1

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

