import mysql.connector

# global variable for sql connection
# please change host, user and password accordingly, only then it will run into your system.
sql_attributes = {
    "host": "localhost", 
    "user": "root", 
    "password": "kriger", 
    "database": "Atm"
}

# connecting to sql database
def connect_to_db():
    try:
        mydb = mysql.connector.connect(
            host = sql_attributes["host"],
            user = sql_attributes["user"],
            password = sql_attributes["password"]
        )

        cur = mydb.cursor()
        query = "show databases"
        cur.execute(query)
        response = cur.fetchall()                # fetching all the db to check if the required db exist or not
        if ("Atm",) not in response:             # checking if the db exist in response
            query = "CREATE DATABASE Atm"    
            cur.execute(query)                   # creating db named Atm, if not exist using execute method

    except Exception as er:
        print(er)

    try:
        mydb = mysql.connector.connect(
            host = sql_attributes["host"],
            user = sql_attributes["user"],
            password = sql_attributes["password"],
            database = sql_attributes["database"]
        )

        cur = mydb.cursor()
        cur.execute("show tables")
        response = cur.fetchall()                  # fetching all the tables in Atm db
        if ('Customer_data',) not in response:     # checking whether required table exist or not
            query = "CREATE TABLE Customer_data(ac_number integer(4), Name varchar(20), Balance integer(4))"
            cur.execute(query)                     # creating table named Customer_data, if not exist using execute method

    except Exception as er:
        print(er) 