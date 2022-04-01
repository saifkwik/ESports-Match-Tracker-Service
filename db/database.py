import mysql.connector

# import database from sql
mydb = mysql.connector.connect(  # if you are running in docker change values below
    host="localhost",
    user="root",
    password="rango6",
    database='game_database'
)

mycursor = mydb.cursor()
