import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="C361"
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS C361")
cursor.execute("USE C361")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),roll_no INT)''')

details = [
    ("Student1", 1),
    ("Student2", 2),
    ("Student3", 3)
]

cursor.executemany("INSERT INTO items (name, roll_no) VALUES (%s, %s)", details)

connection.commit()
cursor.close()
connection.close()


from flask import Flask
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="C361"
)

cursor = connection.cursor()

@app.route('/')
def display_details():
    cursor.execute('SELECT * FROM details')
    details = cursor.fetchall()
    i = ""
    for detail in details:
        i += f"{detail[1]} - {detail[2]}\n"
    return i

if __name__ == '__main__':
    app.run()
