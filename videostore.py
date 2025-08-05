#____________________________________________________________________
#
'''
Date:        2023 November 17
Autor:       Zenande Khoza
File:        Python Programming Project  
Description:
Keeping an organised record of customers is essential for smooth operations in the video store. 
I created a user-friendly system to enable the video store to keep track of both current and potential customers in order to address this. 
Customers can register on this system, which also guarantees that every video—whether it is rented, 
registered, or returned—is carefully logged.
'''
#____________________________________________________________________
#

from datetime import datetime
import mysql.connector #I am using this module's function to connect Python and mySQL
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Enter password",
  database="PY_Videostore_db"
)
cur = conn.cursor()
cur.execute("USE PY_Videostore_db") #selecting PY_Videostore_db as my database of choice 

# Creating the menu 
# defining our lists 
videostore_customers = []

def displaymenu():
    lines = [
        '============================',
        '|     VIDEO STORE          |',
        '============================',
        '| 1. Register Customer     |',
        '| 2. Register Movie        |',
        '============================',
        '| 3. Hire Out Movie        |',
        '| 4. Return Movie          |',
        '============================',
        '| x. Exit                  |',
        '============================'
    ]

    for line in lines:
        print(line)

def registercustomer():  # this function will allow for user input for choice nr 1
    print("Register Customer:")
    fname = input("Please enter your name: ")
    sname = input("Please enter your surname: ")
    address = input("Please enter your address: ")
    phone = int(input("Please enter your number: "))

    # This checks if the customers information is registered
    select_query = "SELECT * FROM customers WHERE fname = %s AND sname = %s AND phone = %s"
    select_values = (fname, sname, phone)

    cur.execute(select_query, select_values)
    existing_customer = cur.fetchone()

    if existing_customer:
        print("Customer already exists. Details:")
        print(f"Name: {existing_customer[1]}")
        print(f"Surname: {existing_customer[2]}")
        print(f"Address: {existing_customer[3]}")
        print(f"Phone: {existing_customer[4]}")
    else:
        # If the customer does not exist, 
        # this then tells they by displaying 
        # that they should register first
        insert_query = "INSERT INTO customers (fname, sname, address, phone) VALUES (%s, %s, %s, %s)"
        insert_values = (fname, sname, address, phone)

        cur.execute(insert_query, insert_values)
        conn.commit()  
        # make sure that it added to the database

        print("Customer Successfully Registered")



def register_movie():  # this function will allow users to input the necessary information
    print("Register Movie:")
    videoID = int(input("Please enter the video ID: "))
    videoVer = int(input("Please enter the version: "))
    vname = input("Please enter movie name: ")
    vtype = input("Please enter movie type. Enter 'R' for new movie or enter 'B' for old movie: ")

    # this validate the movie type and 
    # if it is not correct it displays the message 
    if vtype not in ['R', 'B']:
        print("Invalid movie type. Please enter 'R' for new movie or 'B' for old movie.")
        return

    # Check if the movie/video 
    # already exists in the database 
    select_query = "SELECT * FROM videos WHERE vname = %s AND videoVer = %s"
    select_values = (vname, videoVer)

    cur.execute(select_query, select_values)
    existing_movie = cur.fetchone()
    # if the movie already exists it will display a message
    #  as well as the details of the movie
    if existing_movie:
        print("Movie already exists. Details:")
        print(f"Name: {existing_movie[2]}")
        print(f"Type: {existing_movie[3]}")
    else:
        # If the movie does not exist, the user will register it
        insert_query = "INSERT INTO videos (videoID, videoVer, vname, vtype, dateAdded) VALUES (%s, %s, %s, %s, CURDATE())"
        insert_values = (videoID, videoVer, vname, vtype)

        cur.execute(insert_query, insert_values) # it will execute the INSERT query with the provided values
        conn.commit()  #using .commit to save any and all changes I have made in my database 

        print("Movie Successfully Registered") # an idicator that it was successful

def hireoutmovie():  # this function will allow for user input for choice nr 3
    print("Hire Out Movie")
    phone_number = input("Please Enter the customer's phone number: ") # user input

    # Retrieves customer details from the database
    select_customer_query = "SELECT * FROM customers WHERE phone = %s"
    cur.execute(select_customer_query, (phone_number,))
    customer = cur.fetchone() # Fetch the first (in this case, the only) row of the result set

    # if the customer does not exist, 
    # the customer will be asked to register first
    if not customer:
        print("Customer not found. Please register the customer first.")
        return

    videoID = int(input("Please Enter the video ID: ")) 
    videoVer = int(input("Enter the video version: "))
    
    # displays on the databse the current date and time
    date_hire = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #the date returned is not provided by the user 
    date_return = None

    print("Hire Successful")

    # Insert the details into hire_table 
    insert_query = "INSERT INTO hire_table (custID, videoID, videoVer, dateHired, dateReturned) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(insert_query, (customer[0], videoID, videoVer, date_hire, date_return))
    conn.commit() #using .commit to save any and all changes I have made in my database

def returnmovie():
    print("Return Movie")
    videoID = int(input("Please Enter the video ID: "))

    # Update the hire_table table to indicate 
    # that the movie has been returned on this current date
    update_query = "UPDATE hire_table SET dateReturned = %s WHERE videoID = %s"
    cur.execute(update_query, (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), videoID))
    conn.commit() #using .commit to save any and all changes I have made in my database
    print("Movie Returned")



# Main logic of the program that will enable users to choose their needed choice
while True:
    displaymenu()
    choice = input("Enter your choice: ")

    if choice == '1':
        registercustomer()

    elif choice == '2':
        register_movie()
    
    elif choice == '3':
        hireoutmovie()

    elif choice == '4':
        returnmovie()

    elif choice.lower() == 'x':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")




