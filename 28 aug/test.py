import mysql.connector
mydb =mysql.connector.connect(host="127.0.0.1",user ="root",password="9833",database="techno")
print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("create database techno")
# mycursor.execute("show databases") 
# for x in mycursor:
#     print(x) 
# mycursor.execute("create table student2(fname varchar(25),lname varchar(25),rollno int(5))")
# mycursor.execute("insert into student values(\"Rohan\",\"Mane\",5)")
# # mycursor.execute("")
# sql="insert into student2 values(%s,%s,%s)"
# m=[("Rohan","Mane",21),("Amar","Patil",1),("Satish","Battalwar",2),("Yogesh","More",3),("Shoobham","Chide",4),("Sharad","Barote",5)]

# mycursor.executemany(sql,m)
# mydb.commit()
# print(mycursor.rowcount)
mycursor.execute("update student2 set rollno = 11 where fname='Rohan' ")
mydb.commit()
for x in mycursor:
    print(x)