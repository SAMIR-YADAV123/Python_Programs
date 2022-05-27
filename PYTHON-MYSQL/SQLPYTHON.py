import  mysql.connector
db=mysql.connector.connect(
      host="localhost",
      user="root",
      password="samir*yadav12",
      database="mydatabase"
      )

mycur=db.cursor()


#mycur.execute("CREATE DATABASE mydatabase")    FOR CREATING DATABASE
#mycur.execute("SHOW DATABASES")
#for d in mycur:
 #     print(d)

#mycur.execute("CREATE TABLE customer(name VARCHAR(50), age INTEGER(10))")
#mycur.execute("SHOW TABLES")
#for d in mycur:
 #     print(d)

#giving  data in tables*****

sqlFormula = "insert into students(name,age) values(%s,%s)"
student1 = [('Laltu', 27),
            ('Tejashwi', 31),
            ("sahil", 18),
            ("anurag", 21),]
mycur.executemany(sqlFormula, student1)
db.commit()

#TO SHOW ALL DATA IN TABLES

#mycur.execute("SELECT * FROM students")
#myresult=mycur.fetchall()
#for i in myresult:
 #     print(i)

#show the detail by cindition only

#sql="SELECT * FROM students WHERE name like '%a%' "
#mycur.execute(sql)
#myres=mycur.fetchall()
#for i in myres:
 #      print(i)

 #UPDATION OF DATA IN TABLE

#sql="UPDATE students SET name='laxman' WHERE name = 'aditya'"
#mycur.execute(sql)
#db.commit()

#apply limin while showing the table data

#mycur.execute("SELECT * FROM students LIMIT 3 OFFSET 1") #here offset means from where data are selected for printing
#myres=mycur.fetchall()
#for i in myres:
 #     print(i)

#TO SHOW THE RESULT IN ORDER
#sql="SELECT * FROM students ORDER BY age ASC"  # and for asc just delete the desc or add at the place of desc,asc
#mycur.execute(sql)
#myres=mycur.fetchall()
#for i in myres:
 #     print(i)

#sql="DELETE FROM students WHERE name='shiv'"
#mycur.execute(sql)
#db.commit()
#mycur.execute("SELECT * FROM students")
#myres=mycur.fetchall()
#for i in myres:
 #     print(i)


# for delete the table itself

#sql="DROP TABLE IF EXISTS customer"
#mycur.execute(sql)