import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    cur.execute("CREATE TABLE IF NOT EXISTS attendance(aid INTEGER PRIMARY KEY AUTOINCREMENT,date text,astatus text,status text,remark text,eid text,FOREIGN KEY(eid) REFERENCES employee(eid))")
    con.commit()
    
create_db()