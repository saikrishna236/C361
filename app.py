from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="C361"
)
cursor = conn.cursor()

@app.route('/')
def display_students():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    return render_template('students.html', students=students)

@app.route('/student/<int:student_id>')
def fetch_student(student_id):
    cursor.execute('SELECT * FROM students WHERE id=%s', (student_id,))
    student = cursor.fetchone()
    return str(student)

@app.route('/student/update', methods=['POST'])
def update_student():
    student_id = request.form.get('student_id')
    new_name = request.form.get('new_name')
    new_age = request.form.get('new_age')
    cursor.execute('UPDATE students SET name=%s, age=%s WHERE id=%s', (new_name, new_age, student_id))
    conn.commit()
    return redirect('/')

@app.route('/student/insert', methods=['POST'])
def insert_student():
    name = request.form.get('name')
    age = request.form.get('age')
    cursor.execute('INSERT INTO students (name, age) VALUES (%s, %s)', (name, age))
    conn.commit()

@app.route('/search', methods=['GET'])
def search_students():
    search_query = request.args.get('q')
    cursor.execute("SELECT * FROM students WHERE name LIKE %s", ('%' + search_query + '%',))
    search_results = cursor.fetchall()
    return render_template('search.html', search_results=search_results)

if __name__ == '__main__':
    app.run()
