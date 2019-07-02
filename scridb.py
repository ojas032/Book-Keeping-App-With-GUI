import sqlite3


def conn():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(items TEXT,quantity INTEGER,price REAL)")
    conn.commit()
    conn.close()

def insert():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(items TEXT,quantity INTEGER,price REAL)")
    cur.execute("INSERT INTO store VALUES('glass',10,8.5)")
    conn.commit()
    conn.close()

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(items TEXT,quantity INTEGER,price REAL)")
    cur.execute("DELETE FROM store WHERE items=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=? WHERE items=?",(quantity,"glass"))
    conn.commit()
    conn.close()

update(12,"glass")


def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    row=cur.fetchall()
    conn.commit()
    conn.close()
    return row;

print(view())
