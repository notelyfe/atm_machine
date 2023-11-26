import mysql.connector 
from db_connect import sql_attributes

def withdraw_cash(account_number, balance):

    mydb = mysql.connector.connect(
        host = sql_attributes["host"],
        user = sql_attributes["user"],
        password = sql_attributes["password"],
        database = sql_attributes["database"],
    )
    amount = int(input("Enter Amount to withdrwal : "))

    # reject withdraw if withdrwal amount is greater then available balance
    if amount > balance:
        print("Insufficient Balance")
    # making withdrwal process if sufficient balance is present into the account
    else:
        cur = mydb.cursor()
        query = f"UPDATE Customer_data Set Balance = Balance-{amount} where ac_number = {account_number}"
        cur.execute(query)
        mydb.commit()
        print("Withdrawl successful!!")
        print("Remaining Balance : ", balance-amount)