import mysql.connector

# import database from sql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rango6",
    database='game_database'
)

mycursor = mydb.cursor()