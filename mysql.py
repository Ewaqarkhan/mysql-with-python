import mysql.connector
onnection = mysql.connector.connect(host='localhost',
                                         database='student',
                                         user='root',
                                         password='yourpassword',
                                    )
print(connection.connection_id)    """ we want to print the connection id """   
mycursor=connection.cursor()    """ creat a cursor"""
mycursor.execute("SHOW DATABASES")
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)
mycursor.execute("create table GIKI (id int auto_increment primary key,name varchar(255),address nvarchar(255))")
sql='insert into GIKI(name,address) values(%s,%s)'
val=[('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')]
mycursor.executemany(sql,val)
connection.commit()
print(mycursor.rowcount,"was inserted.") 
mycursor.execute("select *from GIKI")
result=mycursor.fetchall()
for i in result:
    print(i)
khan="select *from GIKI where address = 'Green Grass 1'"
mycursor.execute(khan)
myresult=mycursor.fetchall()
for i in myresult:
    print(i)    
