# ATM MACHINE PROJECT
import mysql.connector
from db_connect import connect_to_db, sql_attributes
from withdraw import withdraw_cash
from deposit import deposit_cash
from create_new_account import create_account

# connecting to db
connect_to_db()

# code starts from here
print("           Welcome to Metaverse Atm             ")
print("************************************************")
account_number = int(input("Please Enter You Account Number to Proceed : "))

mydb = mysql.connector.connect(
    host = sql_attributes["host"],
    user = sql_attributes["user"],
    password = sql_attributes["password"],
    database = sql_attributes["database"]
)

cur = mydb.cursor()

# fetching the customer data on the basis of account number
query = f"select Name, Balance from Customer_data where ac_number={account_number}"
cur.execute(query)
customer_data = cur.fetchone()    # fetching data

# checking whether account number exist or not.
if customer_data != None:
    customer_data = list(customer_data)    # converting the fetched data from tuple to list.
    ch = input(f"Hello! {customer_data[0]} please select one [w, d, c] for [withdrawl, deposit, check balance] : ")[0]

    # asking user whether he/she want to withdraw cash, deposit cash or just want to check the balance
    while ch.lower() != "w" and ch.lower() != "d" and ch.lower() != "c":
        print("Invalid input, Please try again")
        ch = input("please select one [w, d, c] for [withdrawl, deposit, check balance] : ")[0]

    if ch.lower() == "w":
        withdraw_cash(account_number, customer_data[1])    # calling withdraw function
    elif ch.lower() == "d":
        deposit_cash(account_number, customer_data[1])     # calling deposit function
    elif ch.lower() == "c":
        print("Available Balance : ", customer_data[1])

# if no account found then either create a new account or get exit
else:
    print(f"No account found!! with account number : {account_number}") 
    ch = input("Press c to Open a new account or press e to exit : ")[0]
    if ch == 'c':
        create_account()      # calling create_account function for creating a new account
    else:
        print("Exit...")