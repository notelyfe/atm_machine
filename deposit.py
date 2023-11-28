import mysql.connector
from db_connect import sql_attributes

def deposit_cash(account_number, balance):

    mydb = mysql.connector.connect(
        host = sql_attributes["host"],
        user = sql_attributes["user"],
        password = sql_attributes["password"],
        database = sql_attributes["database"],
    )

    amount = int(input("Enter Amount to Add : "))
    cur = mydb.cursor()
    query = f"UPDATE Customer_data Set Balance = Balance+{amount} where ac_number = {account_number}"
    cur.execute(query)
    mydb.commit()
    print("Amount Successfully Deposited!!")
    print("Updated Balance : ", balance+amount)