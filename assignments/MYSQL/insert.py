import mysql.connector

conn = mysql.connector.connect(user="root", password="sunset96", host="127.0.0.1", database="sample_db")
cursor = conn.cursor()


sql = (
        "INSERT INTO EMPLOYEE2(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)"
        "VALUES (%s, %s, %s, %s, %s)"
       )
# firstName = input("What is your first name")
# lastName = input("What is your last name")
# age = int(input("How old are you"))
# sex = input("enter m for male f for female")
# income = float(input("how much you make"))
# data =f"('{firstName}', '{lastName}', {age}, '{sex}', {income})"
data = ('Sam', 'Urso', 30, 'M', 200)
print(data)
try:
    cursor.execute(sql, data)
    conn.commit()
except:
    conn.rollback()

conn.close()
