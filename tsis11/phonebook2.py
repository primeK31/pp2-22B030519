import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="pass123"
)
cur = conn.cursor()


def info():  # 1
    word = input("Enter word: ")
    word += '%'
    cur.execute("SELECT * from get_info(%s);", (word,))  # 1
    row = cur.fetchall()
    print(row)
    conn.commit()


def update(name, number):  # 2
    check_user = ("SELECT 1 FROM list WHERE user_name = '%s'" % (name,))
    cur.execute(check_user)
    row = cur.fetchone()
    if row != None:
        cur.execute('CALL update_user(%s, %s)', (name, number))
    else:
        cur.execute('CALL insert_user(%s, %s)', (name, number))
    conn.commit()


def many1():
    l = [['Lolter', '+77018260248'], ['Kyle', '+9213890484'], ['Bot', '21930344'], ['Proos', '23847853']]
    for i in l:
        cur.execute("CALL insert_user(%s, %s)", (i[0], i[1],))



def offset():  # 4
    cur.execute("select * from get_info1();")
    row = cur.fetchall()
    print(row)


def delete(name):  # 5
    cur.execute('CALL delete_user(%s)', (name,))
    conn.commit()

many1()
conn.commit()
cur.close()
conn.close()
