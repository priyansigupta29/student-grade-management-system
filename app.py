from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
db_path = 'student_grades.db'

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            grade INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    search_query = request.args.get('q')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    if search_query:
        cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + search_query + '%',))
    else:
        cursor.execute("SELECT * FROM students")
        
    students = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (name, grade) VALUES (?, ?)', (name, grade))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        cursor.execute('UPDATE students SET name = ?, grade = ? WHERE id = ?', (name, grade, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    cursor.execute('SELECT * FROM students WHERE id = ?', (id,))
    student = cursor.fetchone()
    conn.close()
    return render_template('update_student.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
