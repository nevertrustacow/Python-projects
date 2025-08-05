#____________________________________________________________________
#
'''
Date:        2023 November 17
Autor:       Zenande Khoza
File:        Python Programming Project 
Description:
the creation of every table in the database
Utilizing MYSQL (installed Python Connector)
Python coding to execute MYSQL statements
'''
#____________________________________________________________________
#
# import the connector to MySQL
import mysql.connector
print("Python - MySql connector found")

######################################
# Link MySQL
#establish the connection 
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Enter password",

)
print("Connection to local MySQL database server successfully established")

# using the cursor class 
#using the cursor object
#in order to use some sql commands in python
mysql_commands_cursor = conn.cursor()
print("Cursor object instantinated")

######################################
# creating my database 
#taking similar steps as in pure mysql script
mysql_commands_cursor.execute ("USE MYSQL")
print("MYSQL has been selected")

#delete the database to allow quick corrections of errors during coding
mysql_commands_cursor.execute("DROP DATABASE IF EXISTS PY_Videostore_db")
print ("Database has been dropped")

#create the PY_Videostore_db database 
mysql_commands_cursor.execute ("CREATE DATABASE PY_Videostore_db")
print("A new PY_Videostore_db database has been successfully created")

# Selecting the database so that every command is directed to it
mysql_commands_cursor.execute("USE PY_Videostore_db")
print("PY_Videostore_db is being used")

######################################
# Creating the tables 
# Creating tables inside of the database 
######################################

# creating the customers table 
create_table_query = """
    CREATE TABLE customers (
        custID INT AUTO_INCREMENT PRIMARY KEY,
        fname VARCHAR(40) NOT NULL,
        sname VARCHAR(40) NOT NULL, 
        address VARCHAR(40) NOT NULL,
        phone VARCHAR(10) NOT NULL UNIQUE
    ) ENGINE=InnoDB AUTO_INCREMENT=100
"""

# Execute the query
mysql_commands_cursor.execute(create_table_query)

print("Customers table has been created ")

# crating the videos table 
create_table_query = """
    CREATE TABLE videos (
        videoID INT NOT NULL,
        videoVer INT NOT NULL,
        Vname VARCHAR(15) NOT NULL, 
        Vtype VARCHAR(1) NOT NULL,
        dateAdded DATE NOT NULL
    ) ENGINE=InnoDB 
"""

# Execute the query
mysql_commands_cursor.execute(create_table_query)
print("videos table has been created ")

# creating the Hire table which will 
# keep record of all the transactions

create_table_query = """
    CREATE TABLE hire_table (
        custID INT NOT NULL,
        videoID INT NOT NULL,
        videoVer INT NOT NULL, 
        dateHired DATE NOT NULL,
        dateReturned DATE,
        FOREIGN KEY (custID) REFERENCES customers(custID) ON DELETE RESTRICT ON UPDATE RESTRICT
    )
"""
# Execute the query
mysql_commands_cursor.execute(create_table_query)
print("hire_table table has been created ")

######################################
# Insertimg values into the tables  
######################################

# insert query 
mysql_commands_cursor = conn.cursor()

insert_into_table = """
    INSERT INTO customers 
    (fname, sname, address, phone)
    VALUES 
    ('Olivia','Mitchell','123 Willow St','5551234567'), 
    ('Ethan','Reynolds','456 Elm Ave','0721234567'), 
    ('Mary','Gallagher','12 David Mabusa Dr','0715551234'), 
    ('Noah','Dawson','101 Maple Court','5553219876'), 
    ('Sophia','Parker','202 Cedar Dr','0763219876')
"""

# Execute the INSERT query
mysql_commands_cursor.execute(insert_into_table)
print("Default values have been successfully added into customers table")
# to save the work that has been done 
conn.commit()
print("Work is saved")

# inserting values into the videos table 

mysql_commands_cursor = conn.cursor()

insert_into_table = """
    INSERT INTO videos 
    (videoID, videoVer, vname, vtype, dateAdded)
    VALUES 
    ('01','1','Spider Man','R','2022-06-15'), 
    ('02','3','Dracula','B','2023-02-14'), 
    ('03','2','Interstellar','R','2022-12-22'), 
    ('04','4','Black Sabbeth','B','2023-04-20'), 
    ('05','5','The Sadness','R','2022-09-28')
"""
# Execute the INSERT query
mysql_commands_cursor.execute(insert_into_table)
print("Default values have been successfully added into videos table")
# to save the work that has been done 
conn.commit()
print("Work is saved")



insert_into_table = """
    INSERT INTO hire_table 
    (custID, videoID, videoVer, dateHired, dateReturned)
    VALUES 
    ('101','01','1','2022-07-20','2022-07-26'), 
    ('102','02','3','2023-04-09','2023-04-15'), 
    ('100','03','2','2023-01-28','2023-02-03'), 
    ('103','04','4','2023-05-16','2023-05-22'), 
    ('104','05','5','2023-04-20','2023-04-26')
"""
# Execute the INSERT query
mysql_commands_cursor.execute(insert_into_table)
print("Default values have been successfully added into hire_table table")
# to save the work that has been done 
conn.commit()
print("Work is saved")

# releasing all resources that are held by the cursor object 
mysql_commands_cursor.close()
print("Flush off the cursor object")

#closing the connection to the database 

conn.close()
