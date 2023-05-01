import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="pass123"
)
cur = conn.cursor()


def update(name, number):  # 2
    check_user = ("SELECT 1 FROM list WHERE user_name = '%s'" % (name,))
    cur.execute(check_user)
    row = cur.fetchone()
    if row != None:
        cur.execute('CALL update_user(%s, %s)', (name, number))
    else:
        cur.execute('CALL insert_user(%s, %s)', (name, number))
    conn.commit()


def delete(name):  # 5
    cur.execute('CALL delete_user(%s)', (name,))
    conn.commit()


number = input("Enter number: ")
cur.callproc("get_info", (number,))  # 1
row = cur.fetchall()
print(row)
cur.execute("SELECT * from list order by id limit 3 offset 2;")  # 4
cur.execute("CALL get_many()",)  # 3

cur.close()
conn.close()
