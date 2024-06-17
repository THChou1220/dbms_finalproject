from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_conn():
    conn = sqlite3.connect('gym.db')
    conn.row_factory = sqlite3.Row
    return conn

# Default
@app.route('/', methods=['GET'])
def default():
    return "Hello World"

# Trainers' routes
@app.route('/trainers', methods=['GET'])
def get_trainers():
    conn = get_db_conn()
    trainers = conn.execute('SELECT * FROM Trainers').fetchall()
    conn.close()
    return jsonify([dict(trainer) for trainer in trainers])

@app.route('/trainers/<int:T_ID>', methods=['GET'])
def get_trainer(T_ID):
    conn = get_db_conn()
    trainer = conn.execute('SELECT * FROM Trainers WHERE T_ID = ?', (T_ID,)).fetchone()
    conn.close()
    if trainer is None:
        return jsonify({'error': 'Trainer not found'}), 404
    return jsonify(dict(trainer))

@app.route('/trainers', methods=['POST'])
def create_trainer():
    new_trainer = request.get_json()
    T_ID = new_trainer['T_ID']
    T_Name = new_trainer['T_Name']
    Email_ID = new_trainer['Email_ID']
    Phone = new_trainer['Phone']
    Gender = new_trainer['Gender']
    Hire_Date = new_trainer['Hire_Date']
    Salary = new_trainer['Salary']
    conn = get_db_conn()
    conn.execute('INSERT INTO Trainers (T_ID, T_Name, Email_ID, Phone, Gender, Hire_Date, Salary) VALUES (?, ?, ?, ?, ?, ?, ?)', (T_ID, T_Name, Email_ID, Phone, Gender, Hire_Date, Salary))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Trainer created'}), 201

@app.route('/trainers/<int:T_ID>', methods=['PUT'])
def update_trainer(T_ID):
    update_data = request.get_json()
    T_Name = update_data['T_Name']
    Email_ID = update_data['Email_ID']
    Phone = update_data['Phone']
    Gender = update_data['Gender']
    Hire_Date = update_data['Hire_Date']
    Salary = update_data['Salary']
    conn = get_db_conn()
    conn.execute('UPDATE Trainers SET T_Name = ?, Email_ID = ?, Phone = ?, Gender = ?, Hire_Date = ?, Salary = ? WHERE T_ID = ?', (T_Name, Email_ID, Phone, Gender, Hire_Date, Salary, T_ID))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Trainer updated'})

@app.route('/trainers/<int:T_ID>', methods=['DELETE'])
def delete_trainer(T_ID):
    conn = get_db_conn()
    conn.execute('DELETE FROM Trainers WHERE T_ID = ?', (T_ID,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Trainer deleted'})

if __name__ == '__main__':
    app.run(debug=True)
