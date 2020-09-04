import mysql.connector 
from mysql.connector import errorcode


def create_user(first_name, last_name):
    try:
        conn = mysql.connector.connect(user='root',
                                       password='sunset96',
                                       host='127.0.0.1',
                                       database='test')
        cursor = conn.cursor()
        add_user = (
            'INSERT into users'
            '(firsName, lastName)'
            'VALUES (%s, %s)'
        )
        user_data = (first_name, last_name)

        cursor.execute(add_user, user_data)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        conn.commit()
        conn.close()


# def cursor_helper(func_name, sqlcomm):
#     try:
#         conn = mysql.connector.connect(user='root',
#                                        password='sunset96',
#                                        host='127.0.0.1',
#                                        database='test')
#         cursor = conn.cursor()
#         code = sqlcomm

#         cursor.execute(code)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Something is wrong with your user name or password")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("Database does not exist")
#         else:
#             print(err)
#     else:
#         conn.commit()
#         conn.close()


    

print("hello")
