import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="pass123"
)

cur = conn.cursor()
name = input("name: ")
phone = input("phone: ")
add_user = """INSERT into list (user_name, phone)
                VALUES (%s, %s);"""
update = """ UPDATE list
                SET phone = %s
                WHERE id = %s"""

query = """SELECT user_name, phone from list where user_name = %s"""

delete_user = """DELETE from list where user_name = %s"""

cur.execute(add_user, (name, phone, ))
cur.execute("""COPY list(user_name, phone) FROM 'D://python_labs//pp2-22B030519//tsis10//Book (1).csv'
               DELIMITER ',' CSV HEADER;""")
#  cur.execute(query)
#  row = cur.fetchall()
#  print(row)
conn.commit()

cur.close()
conn.close()
