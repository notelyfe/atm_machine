import mysql.connector
from db_connect import sql_attributes
import random

def create_account():

    mydb = mysql.connector.connect(
        host = sql_attributes["host"],
        user = sql_attributes["user"],
        password = sql_attributes["password"],
        database = sql_attributes["database"],
    )
    ac_number = random.randint(1000, 10000)          # generating random account number b/w 1000 and 10000.
    cur = mydb.cursor()
    query = f"SELECT * From Customer_data where ac_number={ac_number}"
    cur.execute(query)
    # fetching the data against generated account number to check, whether generated account number already exist or not
    customer_data = cur.fetchone()

    # checking whether generated account number is already exist or not. If exist then generating and check account number again.
    while customer_data != None:
        ac_number = random.randint(1000, 10000)
        cur = mydb.cursor()
        query = f"SELECT * From Customer_data where ac_number={ac_number}"
        cur.execute(query)
        customer_data = cur.fetchone()

    name = input("Enter Your Name : ")

    # validation for Name. If length of name is smaller then 5 character then take input again.
    while len(name) < 5:
        print("Invalid Name!!, Name should be more than 5 character long")
        name = input("Enter Your Name : ")
    name = name.capitalize()

    balance = int(input("Please Add minimum ₹1000 to open your account : "))
    # validation for balance. If balance is less then 1000 then taking input again
    while balance < 1000:
        print("Minimum ₹1000 is required!!")
        balance = int(input("Please Add minimum ₹1000 to open your account : "))

    cur = mydb.cursor()
    query = "INSERT INTO Customer_data(ac_number, Name, Balance) VALUES (%s,%s,%s )"
    b1 = (ac_number, name, balance)
    # inserting the newly generated account into the sql database.
    cur.execute(query, b1)
    mydb.commit()
    print("Account Opened Successfully!!")
    print("Your Account Number is : ", ac_number)