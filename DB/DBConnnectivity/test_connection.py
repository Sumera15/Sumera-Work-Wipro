import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="pass@word1",
    database="employeedb"
)
print("Connected successfully!")
conn.close()