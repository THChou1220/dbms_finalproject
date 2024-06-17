from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_conn():
    conn = sqlite3.connect('gym.db')
    conn.execute('PRAGMA foreign_keys = ON')
    conn.row_factory = sqlite3.Row
    return conn

# Default route
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

# Members' routes
@app.route('/members', methods=['GET'])
def get_members():
    conn = get_db_conn()
    members = conn.execute('SELECT * FROM Members').fetchall()
    conn.close()
    return jsonify([dict(member) for member in members])

@app.route('/members/<int:Mem_ID>', methods=['GET'])
def get_member(Mem_ID):
    conn = get_db_conn()
    member = conn.execute('SELECT * FROM Members WHERE Mem_ID = ?', (Mem_ID,)).fetchone()
    conn.close()
    if member is None:
        return jsonify({'error': 'Member not found'}), 404
    return jsonify(dict(member))

@app.route('/members', methods=['POST'])
def create_member():
    new_member = request.get_json()
    Mem_ID = new_member['Mem_ID']
    M_Name = new_member['M_Name']
    Phone = new_member['Phone']
    Start_Date = new_member['Start_Date']
    Gender = new_member['Gender']
    Subs = new_member['Subs']
    Height = new_member['Height']
    Weight = new_member['Weight']
    Age = new_member['Age']
    Email_ID = new_member['Email_ID']
    Trainer_ID = new_member['Trainer_ID']
    conn = get_db_conn()
    conn.execute('INSERT INTO Members (Mem_ID, M_Name, Phone, Start_Date, Gender, Subs, Height, Weight, Age, Email_ID, Trainer_ID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (Mem_ID, M_Name, Phone, Start_Date, Gender, Subs, Height, Weight, Age, Email_ID, Trainer_ID))
    conn.execute('UPDATE Subscriptions SET Sub_Num = Sub_Num + 1 WHERE Sub_ID = ?', (Subs,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Member created'}), 201

@app.route('/members/<int:Mem_ID>', methods=['PUT'])
def update_member(Mem_ID):
    update_data = request.get_json()
    M_Name = update_data['M_Name']
    Phone = update_data['Phone']
    Start_Date = update_data['Start_Date']
    Gender = update_data['Gender']
    Subs = update_data['Subs']
    Height = update_data['Height']
    Weight = update_data['Weight']
    Age = update_data['Age']
    Email_ID = update_data['Email_ID']
    Trainer_ID = update_data['Trainer_ID']
    conn = get_db_conn()
    oldSubs = conn.execute('SELECT Subs FROM Members WHERE Mem_ID = ?', (Mem_ID,))
    conn.execute('UPDATE Members SET M_Name = ?, Phone = ?, Start_Date = ?, Gender = ?, Subs = ?, Height = ?, Weight = ?, Age = ?, Email_ID = ?, Trainer_ID = ? WHERE Mem_ID = ?', (M_Name, Phone, Start_Date, Gender, Subs, Height, Weight, Age, Email_ID, Trainer_ID, Mem_ID))
    if oldSubs != Subs:
        conn.execute('UPDATE Subscriptions SET Sub_Num = Sub_Num - 1 WHERE Sub_ID = ?', (oldSubs,))
        conn.execute('UPDATE Subscriptions SET Sub_Num = Sub_Num + 1 WHERE Sub_ID = (SELECT Subs FROM Members WHERE Mem_ID = ?)', (Mem_ID,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Member updated'})

@app.route('/members/<int:Mem_ID>', methods=['DELETE'])
def delete_member(Mem_ID):
    conn = get_db_conn()
    conn.execute('UPDATE Subscriptions SET Sub_Num = Sub_Num - 1 WHERE Sub_ID = (SELECT Subs FROM Members WHERE Mem_ID = ?)', (Mem_ID,))
    conn.execute('DELETE FROM Members WHERE Mem_ID = ?', (Mem_ID,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Member deleted'})


if __name__ == '__main__':
    app.run(debug=True)
