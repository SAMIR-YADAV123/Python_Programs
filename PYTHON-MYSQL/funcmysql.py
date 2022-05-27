import mysql.connector
#from mysql.connector import errorcode  //for creating the table at there used
from database import cur,db

#db_name = 'acme'
#TABLES = {}
#TABLES['logs'] = (
 #    "CREATE TABLE  'logs' ("
  #   "'id'  int(11) NOT NULL AUTO_INCREMENT,"
   #  "'text' varchar(250) NOT NULL,"
    # " 'user' varchar(250) NOT NULL,"
     # " 'created' datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    # "PRIMARY KEY('id)"
     #") ENGINE=InnoDB"
   #)

#def create_tables():
 #    cur.execute("USE {}".format(db_name))
  #   for table_name in TABLES:
   #      table_description = TABLES[table_name]
  #       try:
   #           print("Creating tables ({}) ".format(table_name))
    #          cur.execute(table_description)
     #    except mysql.connector.Error as err:
      #        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
       #             print("Already Exists")
        #      else:
         #        print("err.msg")

#def create_database():
 #    cur.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8' ".format(db_name))
  #   print("Database {} created!".format(db_name))

#create_database()
#create_tables()

def add_log(name,age):
    sql = "INSERT INTO logs (name, age) VALUES (%s, %s)"
    cur.execute(sql, (name, age,))
    db.commit()

def update(name,age):
    sql = "UPDATE logs SET name=%s WHERE age = %s"
    cur.execute(sql, (name, age,))
    db.commit()

def show():
   cur.execute("SELECT * FROM logs")
   log_id = cur.fetchall()
   for i in log_id:
      print(i)

def delet(age):
    sql = "DELETE  FROM logs WHERE age = %s"
    cur.execute(sql, (age,))
    db.commit()


add_log('samir',11)
add_log('sagar',22)
add_log('sonu',33)
add_log('guddu',44)
#update('sam',11)
#delet(44)
delet(11)
show()