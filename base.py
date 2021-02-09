import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   surname TEXT,
   name TEXT,
   patronymic TEXT,
   gender TEXT,
   birthday TEXT,
   adress TEXT,
   phone TEXT, 
   email TEXT,
   image BLOB);
""")
conn.commit()
conn.close()


def ins(lis):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", lis)
    conn.commit()
    conn.close()

def get_last_id():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    ans = -1
    for i in cur.execute("SELECT userid FROM users"):
        ans = i[0]
    conn.commit()
    conn.close()
    return ans+1

def get_peop(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    ans = ()
    for i in cur.execute(f"SELECT * FROM users WHERE userid = {int(id)}"):
        ans = i
    conn.commit()
    conn.close()
    return ans

def get_families():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    ans = []
    for i in cur.execute(f"SELECT surname FROM users"):
        ans.append(i[0])
    conn.commit()
    conn.close()
    return ans

def get_people():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    ans = []
    for i in cur.execute(f"SELECT * FROM users"):
        ans.append(i)
    conn.commit()
    conn.close()
    return ans