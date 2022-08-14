import sqlite3


def create_db():
    con = sqlite3.connect(database=r"ims.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS attendance(aid INTEGER PRIMARY KEY AUTOINCREMENT,date text,astatus text,status text,remark text,eid text,FOREIGN KEY(eid) REFERENCES employee(eid))"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS rating(rid INTEGER PRIMARY KEY AUTOINCREMENT,rdate text,rstatus text,eid integer,ratedby integer,rate float,FOREIGN KEY(eid) REFERENCES employee(eid))"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS tasks(tid INTEGER PRIMARY KEY AUTOINCREMENT,adate text,cdate text,tstatus text,task text,tremark text,eid integer,aby integer,FOREIGN KEY(eid) REFERENCES employee(eid))"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS rtasks(trid INTEGER PRIMARY KEY AUTOINCREMENT,tid integer,trdate text,rejectby integer,eid integer,FOREIGN KEY(eid) REFERENCES employee(eid),FOREIGN KEY(tid) REFERENCES tasks(tid))"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS salary(sid INTEGER PRIMARY KEY AUTOINCREMENT,fsalary int,sdate text,sstatus text,eid integer,holiday integer,bonus integer,sremark text,FOREIGN KEY(eid) REFERENCES employee(eid))"
    )
    con.commit()


create_db()
