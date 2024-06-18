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

# Subscriptions' routes
@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    conn = get_db_conn()
    subscriptions = conn.execute('SELECT * FROM Subscriptions').fetchall()
    conn.close()
    return jsonify([dict(subscription) for subscription in subscriptions])

@app.route('/subscriptions/<int:Sub_ID>', methods=['GET'])
def get_subscription(Sub_ID):
    conn = get_db_conn()
    subscription = conn.execute('SELECT * FROM Subscriptions WHERE Sub_ID = ?', (Sub_ID,)).fetchone()
    conn.close()
    if subscription is None:
        return jsonify({'error': 'Subscription not found'}), 404
    return jsonify(dict(subscription))

@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    new_subscription = request.get_json()
    Sub_ID = new_subscription['Sub_ID']
    Price = new_subscription['Price']
    Duration = new_subscription['Duration']
    conn = get_db_conn()
    conn.execute('INSERT INTO Subscriptions (Sub_ID, Price, Duration) VALUES (?, ?, ?)', (Sub_ID, Price, Duration))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Subscription created'}), 201

@app.route('/subscriptions/<int:Sub_ID>', methods=['PUT'])
def update_subscription(Sub_ID):
    update_data = request.get_json()
    Price = update_data['Price']
    Duration = update_data['Duration']
    conn = get_db_conn()
    conn.execute('UPDATE Subscriptions SET Price = ?, Duration = ? WHERE Sub_ID = ?', (Price, Duration, Sub_ID))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Subscription updated'})

@app.route('/subscriptions/<int:Sub_ID>', methods=['DELETE'])
def delete_subscription(Sub_ID):
    conn = get_db_conn()
    conn.execute('DELETE FROM Subscriptions WHERE Sub_ID = ?', (Sub_ID,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Subscription deleted'})

# Equipments' routes
@app.route('/equipments', methods=['GET'])
def get_equipments():
    conn = get_db_conn()
    equipments = conn.execute('SELECT * FROM Equipments').fetchall()
    conn.close()
    return jsonify([dict(equipment) for equipment in equipments])

@app.route('/equipments/<int:Eq_ID>', methods=['GET'])
def get_equipment(Eq_ID):
    conn = get_db_conn()
    equipment = conn.execute('SELECT * FROM Equipments WHERE Eq_ID = ?', (Eq_ID,)).fetchone()
    conn.close()
    if equipment is None:
        return jsonify({'error': 'Equipment not found'}), 404
    return jsonify(dict(equipment))

@app.route('/equipments', methods=['POST'])
def create_equipment():
    new_equipment = request.get_json()
    Eq_ID = new_equipment['Eq_ID']
    Name = new_equipment['Name']
    Quantity = new_equipment['Quantity']
    Cost = new_equipment['Cost']
    conn = get_db_conn()
    conn.execute('INSERT INTO Equipments (Eq_ID, Name, Quantity, Cost) VALUES (?, ?, ?, ?)', (Eq_ID, Name, Quantity, Cost))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Equipment created'}), 201

@app.route('/equipments/<int:Eq_ID>', methods=['PUT'])
def update_equipment(Eq_ID):
    update_data = request.get_json()
    Name = update_data['Name']
    Quantity = update_data['Quantity']
    Cost = update_data['Cost']
    conn = get_db_conn()
    conn.execute('UPDATE Equipments SET Name = ?, Quantity = ?, Cost = ? WHERE Eq_ID = ?', (Name, Quantity, Cost, Eq_ID))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Equipment updated'})

@app.route('/equipments/<int:Eq_ID>', methods=['DELETE'])
def delete_equipment(Eq_ID):
    conn = get_db_conn()
    conn.execute('DELETE FROM Equipments WHERE Eq_ID = ?', (Eq_ID,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Equipment deleted'})

# Exercises' routes
@app.route('/exercises', methods=['GET'])
def get_exercises():
    conn = get_db_conn()
    exercises = conn.execute('SELECT * FROM Exercises').fetchall()
    conn.close()
    return jsonify([dict(exercise) for exercise in exercises])

@app.route('/exercises/<int:Ex_ID>', methods=['GET'])
def get_exercise(Ex_ID):
    conn = get_db_conn()
    exercise = conn.execute('SELECT * FROM Exercises WHERE Ex_ID = ?', (Ex_ID,)).fetchone()
    conn.close()
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404
    return jsonify(dict(exercise))

@app.route('/exercises', methods=['POST'])
def create_exercise():
    new_exercise = request.get_json()
    Ex_ID = new_exercise['Ex_ID']
    Ex_Name = new_exercise['Ex_Name']
    Type = new_exercise['Type']
    Time_Slot = new_exercise['Time_Slot']
    Frequency = new_exercise['Frequency']
    conn = get_db_conn()
    conn.execute('INSERT INTO Exercises (Ex_ID, Ex_Name, Type, Time_Slot, Frequency) VALUES (?, ?, ?, ?, ?)', (Ex_ID, Ex_Name, Type, Time_Slot, Frequency))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Exercise created'}), 201

@app.route('/exercises/<int:Ex_ID>', methods=['PUT'])
def update_exercise(Ex_ID):
    update_data = request.get_json()
    Ex_Name = update_data['Ex_Name']
    Type = update_data['Type']
    Time_Slot = update_data['Time_Slot']
    Frequency = update_data['Frequency']
    conn = get_db_conn()
    conn.execute('UPDATE Equipments SET Ex_Name = ?, Type = ?, Time_Slot = ?, Frequency = ? WHERE Ex_ID = ?', (Ex_Name, Type, Time_Slot, Frequency, Ex_ID))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Exercise updated'})

@app.route('/exercises/<int:Ex_ID>', methods=['DELETE'])
def delete_exercise(Ex_ID):
    conn = get_db_conn()
    conn.execute('DELETE FROM Exercises WHERE Ex_ID = ?', (Ex_ID,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Exercise deleted'})

if __name__ == '__main__':
    app.run(debug=True)
