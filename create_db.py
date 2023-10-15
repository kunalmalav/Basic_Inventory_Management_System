import sqlite3      # sqlite3:inbuild library of python to create an inbuild database
def create_db():
    con=sqlite3.connect(database=r'ims.db')    #connection for our database in 'con' variable
    cur=con.cursor()                                #cur:cursor to execute our queries

    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")                 #creating a table, TABLE NAME:employee        
   # eid: unique key (primary key) type integer ,name type text...
    con.commit()
     
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")                 #creating a table, TABLE NAME:employee        
   # eid: unique key (primary key) type integer ,name type text...
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text )")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier text,Category text,name text,price text,qty text,status text)")                 #creating a table, TABLE NAME:employee        
   # eid: unique key (primary key) type integer ,name type text...
    con.commit()



create_db()