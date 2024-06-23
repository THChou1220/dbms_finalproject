from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import random, string, re

import os
database_path = os.path.join(os.path.dirname(__file__), 'gym.db')

app = Flask(__name__)
CORS(app)

def get_db_conn():
    conn = sqlite3.connect(database_path)
    conn.execute('PRAGMA foreign_keys = ON')
    conn.row_factory = sqlite3.Row
    return conn

from datetime import datetime
import pytz

def get_cur_Taiwan_date():
    now = datetime.now()
    tz = pytz.timezone('Asia/Taipei')
    taiwan_time = now.astimezone(tz)
    formatted_date = taiwan_time.strftime('%Y-%m-%d')
    return formatted_date

phone_pattern = re.compile(r'^\d{4}-\d{3}-\d{3}$')
email_pattern = re.compile(r'^[^@]+@[^@]+\.[^@]+$')

# Default route
@app.route('/', methods=['GET'])
def default():
    return "Hello World"


# Trainers' routes
@app.route('/trainers', methods=['POST'])
def create_trainer():
    new_trainer = request.get_json()
    T_ID = generate_T_ID()
    T_Name = new_trainer['T_Name']
    Email_ID = new_trainer.get('Email_ID', '')
    Phone = new_trainer.get('Phone', '')
    Gender = new_trainer['Gender']
    Hire_Date = get_cur_Taiwan_date()
    Salary = new_trainer['Salary']
    
    if not new_trainer['T_Name'] or new_trainer['T_Name'] == "":
        return jsonify({'error': 'T_Name cannot be empty'}), 400
    
    if Email_ID:
        if not email_pattern.match(Email_ID):
            return jsonify({'error': 'Email_ID must be in format example@example.com'}), 400
    
    if Phone:
        if not phone_pattern.match(Phone):
            return jsonify({'error': 'Phone must be in format xxxx-xxx-xxx'}), 400
    
    if Gender not in ["Male", "Female", "Others"]:
        return jsonify({'error': 'Gender must be Male, Female, Others'}), 400
    
    try:
        Salary = float(Salary)
        if Salary < 50000:
            return jsonify({'error': 'Salary must be at least 50000'}), 400
    except ValueError:
        return jsonify({'error': 'Salary must be numeric'}), 400
    
    conn = get_db_conn()
    conn.execute('INSERT INTO Trainers (T_ID, T_Name, Email_ID, Phone, Gender, Hire_Date, Salary) VALUES (?, ?, ?, ?, ?, ?, ?)', (T_ID, T_Name, Email_ID, Phone, Gender, Hire_Date, Salary))
    conn.commit()
    conn.close()
    
    return jsonify({'T_id': T_ID, 'T_Name': T_Name}), 201

def generate_T_ID():
    conn = get_db_conn()
    cursor = conn.cursor()
    while True:
        T_ID = 'Tr' + ''.join(random.choice(string.digits) for _ in range(8))
        cursor.execute('SELECT 1 FROM Trainers WHERE T_ID = ?', (T_ID,))
        if cursor.fetchone() is None:
            conn.close()
            return T_ID

@app.route('/trainers', methods=['GET'])
def get_trainers():
    conn = get_db_conn()
    trainers = conn.execute('SELECT * FROM Trainers').fetchall()
    conn.close()
    
    trainers_list = []
    for trainer in trainers:
        trainer_dict = dict(trainer)
        trainer_dict['T_id'] = trainer_dict.pop('T_ID')
        trainers_list.append(trainer_dict)
    trainers = trainers_list
    
    return jsonify([dict(trainer) for trainer in trainers])

@app.route('/trainers/<T_ID>', methods=['GET'])
def get_trainer(T_ID):
    conn = get_db_conn()
    trainer = conn.execute('SELECT * FROM Trainers WHERE T_ID = ?', (T_ID,)).fetchone()
    conn.close()
    if trainer is None:
        return jsonify({'error': 'Trainer not found'}), 404
    
    trainer_dict = dict(trainer)
    trainer_dict['T_id'] = trainer_dict.pop('T_ID')
    trainer = trainer_dict
    
    return jsonify(dict(trainer))

@app.route('/trainers/<T_ID>/members', methods=['GET'])
def get_members_of_trainer(T_ID):
    conn = get_db_conn()
    trainer = conn.execute('SELECT * FROM Trainers WHERE T_ID = ?', (T_ID,)).fetchone()
    conn.close()
    if trainer is None:
        return jsonify({'error': 'Trainer not found'}), 404
    
    conn = get_db_conn()
    members = conn.execute('SELECT Members.Mem_ID as Member_ID, Members.M_Name as Member_Name FROM Trainers JOIN Members ON Trainers.T_ID = Members.Trainer_ID WHERE T_ID = ?', (T_ID,)).fetchall()
    conn.close()
    
    return jsonify([dict(member) for member in members])

@app.route('/trainers/<T_ID>', methods=['PATCH'])
def update_trainer(T_ID):
    conn = get_db_conn()
    trainer = conn.execute('SELECT * FROM Trainers WHERE T_ID = ?', (T_ID,)).fetchone()
    conn.close()
    if trainer is None:
        return jsonify({'error': 'Trainer not found'}), 404
    
    update_data = request.get_json()
    T_Name = update_data['T_Name']
    Email_ID = update_data['Email_ID']
    Phone = update_data['Phone']
    Gender = update_data['Gender']
    Salary = update_data['Salary']
    
    if not update_data['T_Name'] or update_data['T_Name'] == "":
        return jsonify({'error': 'T_Name cannot be empty'}), 400
    
    if Gender not in ["Male", "Female", "Others"]:
        return jsonify({'error': 'Gender must be Male, Female, Others'}), 400
    
    try:
        Salary = float(Salary)
        if Salary < 50000:
            return jsonify({'error': 'Salary must be at least 50000'}), 400
    except ValueError:
        return jsonify({'error': 'Salary must be numeric'}), 400
    
    conn = get_db_conn()
    conn.execute('UPDATE Trainers SET T_Name = ?, Email_ID = ?, Phone = ?, Gender = ?, Salary = ? WHERE T_ID = ?', (T_Name, Email_ID, Phone, Gender, Salary, T_ID))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Trainer updated'})

@app.route('/trainers/<T_ID>', methods=['DELETE'])
def delete_trainer(T_ID):
    conn = get_db_conn()
    trainer = conn.execute('SELECT * FROM Trainers WHERE T_ID = ?', (T_ID,)).fetchone()
    conn.close()
    if trainer is None:
        return jsonify({'error': 'Trainer not found'}), 404
    
    conn = get_db_conn()
    conn.execute('DELETE FROM Trainers WHERE T_ID = ?', (T_ID,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Trainer deleted'})


# Members' routes
@app.route('/members', methods=['POST'])
def create_member():
    new_member = request.get_json()
    Mem_ID = generate_Mem_ID()
    M_Name = new_member['M_Name']
    Phone = new_member.get('Phone', '')
    Start_Date = get_cur_Taiwan_date()
    Gender = new_member['Gender']
    Subs = new_member['Subs']
    Height = new_member['Height']
    Weight = new_member['Weight']
    Age = new_member['Age']
    Email_ID = new_member.get('Email_ID', '')
    Trainer_ID = new_member['Trainer_ID']
    
    if not new_member['M_Name'] or new_member['M_Name'] == "":
        return jsonify({'error': 'M_Name cannot be empty'}), 400
    
    if Phone:
        if not phone_pattern.match(Phone):
            return jsonify({'error': 'Phone must be in format xxxx-xxx-xxx'}), 400
    
    if Gender not in ["Male", "Female", "Others"]:
        return jsonify({'error': 'Gender must be Male, Female, Others'}), 400
    
    conn = get_db_conn()
    subscription = conn.execute('SELECT * FROM Subscriptions WHERE Sub_ID = ?', (Subs,)).fetchone()
    conn.close()
    if subscription is None:
        return jsonify({'error': 'Subscription not found'}), 404
    
    if Email_ID:
        if not email_pattern.match(Email_ID):
            return jsonify({'error': 'Email_ID must be in format example@example.com'}), 400
    
    conn = get_db_conn()
    trainer = conn.execute('SELECT * FROM Trainers WHERE T_ID = ?', (Trainer_ID,)).fetchone()
    conn.close()
    if trainer is None:
        return jsonify({'error': 'Trainer not found'}), 404
    
    conn = get_db_conn()
    conn.execute('INSERT INTO Members (Mem_ID, M_Name, Phone, Start_Date, Gender, Subs, Height, Weight, Age, Email_ID, Trainer_ID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (Mem_ID, M_Name, Phone, Start_Date, Gender, Subs, Height, Weight, Age, Email_ID, Trainer_ID))
    conn.execute('UPDATE Subscriptions SET Sub_Num = Sub_Num + 1 WHERE Sub_ID = ?', (Subs,))
    conn.commit()
    conn.close()
    
    return jsonify({'Mem_ID': Mem_ID, 'M_Name': M_Name}), 201

def generate_Mem_ID():
    conn = get_db_conn()
    cursor = conn.cursor()
    while True:
        Mem_ID = 'Me' + ''.join(random.choice(string.digits) for _ in range(8))
        cursor.execute('SELECT 1 FROM Members WHERE Mem_ID = ?', (Mem_ID,))
        if cursor.fetchone() is None:
            conn.close()
            return Mem_ID

@app.route('/members', methods=['GET'])
def get_members():
    conn = get_db_conn()
    members = conn.execute('SELECT * FROM Members').fetchall()
    conn.close()
    
    return jsonify([dict(member) for member in members])

@app.route('/members/<Mem_ID>', methods=['GET'])
def get_member(Mem_ID):
    conn = get_db_conn()
    member = conn.execute('SELECT * FROM Members WHERE Mem_ID = ?', (Mem_ID,)).fetchone()
    conn.close()
    if member is None:
        return jsonify({'error': 'Member not found'}), 404
    
    return jsonify(dict(member))

@app.route('/members/<Mem_ID>', methods=['PATCH'])
def update_member(Mem_ID):
    conn = get_db_conn()
    member = conn.execute('SELECT * FROM Members WHERE Mem_ID = ?', (Mem_ID,)).fetchone()
    conn.close()
    if member is None:
        return jsonify({'error': 'Member not found'}), 404
    
    update_data = request.get_json()
    M_Name = update_data['M_Name']
    Phone = update_data['Phone']
    Gender = update_data['Gender']
    Subs = update_data['Subs']
    Height = update_data['Height']
    Weight = update_data['Weight']
    Age = update_data['Age']
    Email_ID = update_data['Email_ID']
    Trainer_ID = update_data['Trainer_ID']
    
    if not update_data['M_Name'] or update_data['M_Name'] == "":
        return jsonify({'error': 'M_Name cannot be empty'}), 400
    
    if Gender not in ["Male", "Female", "Others"]:
        return jsonify({'error': 'Gender must be Male, Female, Others'}), 400
    
    conn = get_db_conn()
    subscription = conn.execute('SELECT * FROM Subscriptions WHERE Sub_ID = ?', (Subs,)).fetchone()
    conn.close()
    if subscription is None:
        return jsonify({'error': 'Subscription not found'}), 404
    
    conn = get_db_conn()
    trainer = conn.execute('SELECT * FROM Trainers WHERE T_ID = ?', (Trainer_ID,)).fetchone()
    conn.close()
    if trainer is None:
        return jsonify({'error': 'Trainer not found'}), 404
    
    conn = get_db_conn()
    oldSubs = conn.execute('SELECT Subs FROM Members WHERE Mem_ID = ?', (Mem_ID,)).fetchone()[0]
    conn.execute('UPDATE Members SET M_Name = ?, Phone = ?, Gender = ?, Subs = ?, Height = ?, Weight = ?, Age = ?, Email_ID = ?, Trainer_ID = ? WHERE Mem_ID = ?', (M_Name, Phone, Gender, Subs, Height, Weight, Age, Email_ID, Trainer_ID, Mem_ID))
    if oldSubs != Subs:
        conn.execute('UPDATE Subscriptions SET Sub_Num = Sub_Num - 1 WHERE Sub_ID = ?', (oldSubs,))
        conn.execute('UPDATE Subscriptions SET Sub_Num = Sub_Num + 1 WHERE Sub_ID = ?', (Subs,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Member updated'})

@app.route('/members/<Mem_ID>', methods=['DELETE'])
def delete_member(Mem_ID):
    conn = get_db_conn()
    member = conn.execute('SELECT * FROM Members WHERE Mem_ID = ?', (Mem_ID,)).fetchone()
    conn.close()
    if member is None:
        return jsonify({'error': 'Member not found'}), 404
    
    conn = get_db_conn()
    Subs = conn.execute('SELECT Subs FROM Members WHERE Mem_ID = ?', (Mem_ID,)).fetchone()[0]
    conn.execute('UPDATE Subscriptions SET Sub_Num = Sub_Num - 1 WHERE Sub_ID = ?', (Subs,))
    conn.execute('DELETE FROM Members WHERE Mem_ID = ?', (Mem_ID,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Member deleted'})


# Subscriptions' routes
@app.route('/subscriptions', methods=['POST'])
def create_subscription():
    new_subscription = request.get_json()
    Sub_ID = generate_Sub_ID()
    Price = new_subscription['Price']
    Duration = new_subscription['Duration']
    
    try:
        Price = float(Price)
    except ValueError:
        return jsonify({'error': 'Price must be numeric'}), 400
    
    try:
        Duration = int(Duration)
        if isinstance(new_subscription['Duration'], float):
            return jsonify({'error': 'Duration must be an integer'}), 400
    except ValueError:
        return jsonify({'error': 'Duration must be an integer'}), 400
    
    conn = get_db_conn()
    conn.execute('INSERT INTO Subscriptions (Sub_ID, Price, Duration) VALUES (?, ?, ?)', (Sub_ID, Price, Duration))
    conn.commit()
    conn.close()
    
    return jsonify({'Sub_ID': Sub_ID, 'Duration': Duration, 'Price': Price}), 201

def generate_Sub_ID():
    conn = get_db_conn()
    cursor = conn.cursor()
    while True:
        Sub_ID = 'Su' + ''.join(random.choice(string.digits) for _ in range(8))
        cursor.execute('SELECT 1 FROM Subscriptions WHERE Sub_ID = ?', (Sub_ID,))
        if cursor.fetchone() is None:
            conn.close()
            return Sub_ID

@app.route('/subscriptions', methods=['GET'])
def get_subscriptions():
    conn = get_db_conn()
    subscriptions = conn.execute('SELECT * FROM Subscriptions ORDER BY Duration ASC, Price ASC').fetchall()
    conn.close()
    
    return jsonify([dict(subscription) for subscription in subscriptions])

@app.route('/subscriptions/<Sub_ID>', methods=['GET'])
def get_subscription(Sub_ID):
    conn = get_db_conn()
    subscription = conn.execute('SELECT * FROM Subscriptions WHERE Sub_ID = ?', (Sub_ID,)).fetchone()
    conn.close()
    if subscription is None:
        return jsonify({'error': 'Subscription not found'}), 404
    
    return jsonify(dict(subscription))

@app.route('/subscriptions/<Sub_ID>/members', methods=['GET'])
def get_members_of_subscription(Sub_ID):
    conn = get_db_conn()
    subscription = conn.execute('SELECT * FROM Subscriptions WHERE Sub_ID = ?', (Sub_ID,)).fetchone()
    conn.close()
    if subscription is None:
        return jsonify({'error': 'Subscription not found'}), 404
    
    conn = get_db_conn()
    members = conn.execute('SELECT Members.Mem_ID as Member_ID, Members.M_Name as Member_Name FROM Subscriptions JOIN Members ON Subscriptions.Sub_ID = Members.Subs WHERE Sub_ID = ?', (Sub_ID,)).fetchall()
    conn.close()
    
    return jsonify([dict(member) for member in members])

@app.route('/subscriptions/<Sub_ID>', methods=['PATCH'])
def update_subscription(Sub_ID):
    conn = get_db_conn()
    subscription = conn.execute('SELECT * FROM Subscriptions WHERE Sub_ID = ?', (Sub_ID,)).fetchone()
    conn.close()
    if subscription is None:
        return jsonify({'error': 'Subscription not found'}), 404
    
    update_data = request.get_json()
    Price = update_data['Price']
    Duration = update_data['Duration']
    
    try:
        Price = float(Price)
    except ValueError:
        return jsonify({'error': 'Price must be numeric'}), 400
    
    try:
        Duration = int(Duration)
        if isinstance(update_data['Duration'], float):
            return jsonify({'error': 'Duration must be an integer'}), 400
    except ValueError:
        return jsonify({'error': 'Duration must be an integer'}), 400
    
    conn = get_db_conn()
    conn.execute('UPDATE Subscriptions SET Price = ?, Duration = ? WHERE Sub_ID = ?', (Price, Duration, Sub_ID))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Subscription updated'})

@app.route('/subscriptions/<Sub_ID>', methods=['DELETE'])
def delete_subscription(Sub_ID):
    conn = get_db_conn()
    subscription = conn.execute('SELECT * FROM Subscriptions WHERE Sub_ID = ?', (Sub_ID,)).fetchone()
    conn.close()
    if subscription is None:
        return jsonify({'error': 'Subscription not found'}), 404
    
    conn = get_db_conn()
    conn.execute('DELETE FROM Subscriptions WHERE Sub_ID = ?', (Sub_ID,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Subscription deleted'})


# Equipments' routes
@app.route('/equipments', methods=['POST'])
def create_equipment():
    new_equipment = request.get_json()
    Eq_ID = generate_Eq_ID()
    Name = new_equipment['Name']
    Quantity = new_equipment['Quantity']
    Cost = new_equipment['Cost']
    
    if not new_equipment['Name'] or new_equipment['Name'] == "":
        return jsonify({'error': 'Name cannot be empty'}), 400
    
    try:
        Quantity = int(Quantity)
        if isinstance(new_equipment['Quantity'], float):
            return jsonify({'error': 'Quantity must be an integer'}), 400
        if Quantity < 1:
            return jsonify({'error': 'Quantity must be at least 1'})
    except ValueError:
        return jsonify({'error': 'Quantity must be an integer'}), 400
    
    try:
        Cost = float(Cost)
    except ValueError:
        return jsonify({'error': 'Cost must be numeric'}), 400
    
    conn = get_db_conn()
    conn.execute('INSERT INTO Equipments (Eq_ID, Name, Quantity, Cost) VALUES (?, ?, ?, ?)', (Eq_ID, Name, Quantity, Cost))
    conn.commit()
    conn.close()
    
    return jsonify({'Eq_ID': Eq_ID, 'Name': Name}), 201

def generate_Eq_ID():
    conn = get_db_conn()
    cursor = conn.cursor()
    while True:
        Eq_ID = 'Eq' + ''.join(random.choice(string.digits) for _ in range(8))
        cursor.execute('SELECT 1 FROM Equipments WHERE Eq_ID = ?', (Eq_ID,))
        if cursor.fetchone() is None:
            conn.close()
            return Eq_ID

@app.route('/equipments', methods=['GET'])
def get_equipments():
    conn = get_db_conn()
    equipments = conn.execute('SELECT * FROM Equipments').fetchall()
    conn.close()
    
    return jsonify([dict(equipment) for equipment in equipments])

@app.route('/equipments/<Eq_ID>', methods=['GET'])
def get_equipment(Eq_ID):
    conn = get_db_conn()
    equipment = conn.execute('SELECT * FROM Equipments WHERE Eq_ID = ?', (Eq_ID,)).fetchone()
    conn.close()
    if equipment is None:
        return jsonify({'error': 'Equipment not found'}), 404
    
    return jsonify(dict(equipment))

@app.route('/equipments/<Eq_ID>', methods=['PATCH'])
def update_equipment(Eq_ID):
    conn = get_db_conn()
    equipment = conn.execute('SELECT * FROM Equipments WHERE Eq_ID = ?', (Eq_ID,)).fetchone()
    conn.close()
    if equipment is None:
        return jsonify({'error': 'Equipment not found'}), 404
    
    update_data = request.get_json()
    Name = update_data['Name']
    Quantity = update_data['Quantity']
    Cost = update_data['Cost']
    
    if not update_data['Name'] or update_data['Name'] == "":
        return jsonify({'error': 'Name cannot be empty'}), 400
    
    try:
        Quantity = int(Quantity)
        if isinstance(update_data['Quantity'], float):
            return jsonify({'error': 'Quantity must be an integer'}), 400
        if Quantity < 1:
            return jsonify({'error': 'Quantity must be at least 1'})
    except ValueError:
        return jsonify({'error': 'Quantity must be an integer'}), 400
    
    try:
        Cost = float(Cost)
    except ValueError:
        return jsonify({'error': 'Cost must be numeric'}), 400
    
    conn = get_db_conn()
    conn.execute('UPDATE Equipments SET Name = ?, Quantity = ?, Cost = ? WHERE Eq_ID = ?', (Name, Quantity, Cost, Eq_ID))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Equipment updated'})

@app.route('/equipments/<Eq_ID>', methods=['DELETE'])
def delete_equipment(Eq_ID):
    conn = get_db_conn()
    equipment = conn.execute('SELECT * FROM Equipments WHERE Eq_ID = ?', (Eq_ID,)).fetchone()
    conn.close()
    if equipment is None:
        return jsonify({'error': 'Equipment not found'}), 404
    
    conn = get_db_conn()
    conn.execute('DELETE FROM Equipments WHERE Eq_ID = ?', (Eq_ID,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Equipment deleted'})


# Exercises' routes
@app.route('/exercises', methods=['POST'])
def create_exercise():
    new_exercise = request.get_json()
    EX_ID = generate_EX_ID()
    EX_Name = new_exercise['EX_Name']
    Type = new_exercise['Type']
    Time_Slot = new_exercise['Time_Slot']
    Frequency = new_exercise['Frequency']
    
    if Type not in ["Upper Body", "Lower Body", "Arm"]:
        return jsonify({'error': 'Type must be Upper Body, Lower Body, or Arm'}), 400
    
    conn = get_db_conn()
    conn.execute('INSERT INTO Exercises (EX_ID, EX_Name, Type, Time_Slot, Frequency) VALUES (?, ?, ?, ?, ?)', (EX_ID, EX_Name, Type, Time_Slot, Frequency))
    conn.commit()
    conn.close()
    
    return jsonify({'EX_id': EX_ID, 'EX_Name': EX_Name}), 201

def generate_EX_ID():
    conn = get_db_conn()
    cursor = conn.cursor()
    while True:
        EX_ID = 'Ex' + ''.join(random.choice(string.digits) for _ in range(8))
        cursor.execute('SELECT 1 FROM Exercises WHERE EX_ID = ?', (EX_ID,))
        if cursor.fetchone() is None:
            conn.close()
            return EX_ID

@app.route('/exercises', methods=['GET'])
def get_exercises():
    conn = get_db_conn()
    exercises = conn.execute('SELECT * FROM Exercises ORDER BY CASE WHEN Type = "Arm" THEN 1 WHEN Type = "Upper Body" THEN 2 ELSE 3 END').fetchall()
    conn.close()
    
    exercises_list = []
    for exercise in exercises:
        exercise_dict = dict(exercise)
        exercise_dict['EX_id'] = exercise_dict.pop('EX_ID')
        exercises_list.append(exercise_dict)
    exercises = exercises_list
    
    return jsonify([dict(exercise) for exercise in exercises])

@app.route('/exercises/<EX_ID>', methods=['GET'])
def get_exercise(EX_ID):
    conn = get_db_conn()
    exercise = conn.execute('SELECT * FROM Exercises WHERE EX_ID = ?', (EX_ID,)).fetchone()
    conn.close()
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404
    
    exercise_dict = dict(exercise)
    exercise_dict['EX_id'] = exercise_dict.pop('EX_ID')
    exercise = exercise_dict
    
    return jsonify(dict(exercise))

@app.route('/exercises/<EX_ID>', methods=['PATCH'])
def update_exercise(EX_ID):
    conn = get_db_conn()
    exercise = conn.execute('SELECT * FROM Exercises WHERE EX_ID = ?', (EX_ID,)).fetchone()
    conn.close()
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404
    
    update_data = request.get_json()
    EX_Name = update_data['EX_Name']
    Type = update_data['Type']
    Time_Slot = update_data['Time_Slot']
    Frequency = update_data['Frequency']
    
    if Type not in ["Upper Body", "Lower Body", "Arm"]:
        return jsonify({'error': 'Type must be Upper Body, Lower Body, or Arm'}), 400
    
    conn = get_db_conn()
    conn.execute('UPDATE Exercises SET EX_Name = ?, Type = ?, Time_Slot = ?, Frequency = ? WHERE EX_ID = ?', (EX_Name, Type, Time_Slot, Frequency, EX_ID))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Exercise updated'})

@app.route('/exercises/<EX_ID>', methods=['DELETE'])
def delete_exercise(EX_ID):
    conn = get_db_conn()
    exercise = conn.execute('SELECT * FROM Exercises WHERE EX_ID = ?', (EX_ID,)).fetchone()
    conn.close()
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404
    
    conn = get_db_conn()
    conn.execute('DELETE FROM Exercises WHERE EX_ID = ?', (EX_ID,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Exercise deleted'})


# routes of Use
@app.route('/use', methods=['POST'])
def create_use():
    new_use = request.get_json()
    Member_ID = new_use['Member_ID']
    Equipment_ID = new_use['Equipment_ID']
    
    conn = get_db_conn()
    member = conn.execute('SELECT * FROM Members WHERE Mem_ID = ?', (Member_ID,)).fetchone()
    conn.close()
    if member is None:
        return jsonify({'error': 'Member not found'}), 404
    
    conn = get_db_conn()
    equipment = conn.execute('SELECT * FROM Equipments WHERE Eq_ID = ?', (Equipment_ID,)).fetchone()
    conn.close()
    if equipment is None:
        return jsonify({'error': 'Equipment not found'}), 404
    
    conn = get_db_conn()
    use = conn.execute('SELECT * FROM Use WHERE Member_ID = ? AND Equipment_ID = ?', (Member_ID, Equipment_ID)).fetchone()
    conn.close()
    if use:
        return jsonify({'error': 'Relation-Use has already existed'}), 500
    
    conn = get_db_conn()
    conn.execute('INSERT INTO Use (Member_ID, Equipment_ID) VALUES (?, ?)', (Member_ID, Equipment_ID))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Relation-Use created'}), 201

@app.route('/use', methods=['GET'])
def get_use():
    conn = get_db_conn()
    all_use = conn.execute('SELECT Members.M_Name as Member, Use.Member_ID, Equipments.Name as Equipment, Use.Equipment_ID FROM Use JOIN Members ON Use.Member_ID = Members.Mem_ID JOIN Equipments ON Use.Equipment_ID = Equipments.Eq_ID').fetchall()
    conn.close()
    
    return jsonify([dict(use) for use in all_use])

@app.route('/use', methods=['DELETE'])
def delete_use():
    delete_data = request.get_json()
    Member_ID = delete_data['Member_ID']
    Equipment_ID = delete_data['Equipment_ID']
    
    conn = get_db_conn()
    member = conn.execute('SELECT * FROM Members WHERE Mem_ID = ?', (Member_ID,)).fetchone()
    conn.close()
    if member is None:
        return jsonify({'error': 'Member not found'}), 404
    
    conn = get_db_conn()
    equipment = conn.execute('SELECT * FROM Equipments WHERE Eq_ID = ?', (Equipment_ID,)).fetchone()
    conn.close()
    if equipment is None:
        return jsonify({'error': 'Equipment not found'}), 404
    
    conn = get_db_conn()
    conn.execute('DELETE FROM Use WHERE Member_ID = ? AND Equipment_ID = ?', (Member_ID, Equipment_ID))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Relation-Use deleted'})


# routes of Do
@app.route('/do', methods=['POST'])
def create_do():
    new_do = request.get_json()
    Member_ID = new_do['Member_ID']
    Exercise_ID = new_do['Exercise_ID']
    
    conn = get_db_conn()
    member = conn.execute('SELECT * FROM Members WHERE Mem_ID = ?', (Member_ID,)).fetchone()
    conn.close()
    if member is None:
        return jsonify({'error': 'Member not found'}), 404
    
    conn = get_db_conn()
    exercise = conn.execute('SELECT * FROM Exercises WHERE EX_ID = ?', (Exercise_ID,)).fetchone()
    conn.close()
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404
    
    conn = get_db_conn()
    do = conn.execute('SELECT * FROM Do WHERE Member_ID = ? AND Exercise_ID = ?', (Member_ID, Exercise_ID)).fetchone()
    conn.close()
    if do:
        return jsonify({'error': 'Relation-Do has already existed'}), 500
    
    conn = get_db_conn()
    conn.execute('INSERT INTO Do (Member_ID, Exercise_ID) VALUES (?, ?)', (Member_ID, Exercise_ID))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Relation-Do created'}), 201

@app.route('/do', methods=['GET'])
def get_do():
    conn = get_db_conn()
    all_do = conn.execute('SELECT Members.M_Name as Member, Do.Member_ID, Exercises.EX_Name as Exercise, Do.Exercise_ID FROM Do JOIN Members ON Do.Member_ID = Members.Mem_ID JOIN Exercises ON Do.Exercise_ID = Exercises.EX_ID').fetchall()
    conn.close()
    
    return jsonify([dict(do) for do in all_do])

@app.route('/do', methods=['DELETE'])
def delete_do():
    delete_data = request.get_json()
    Member_ID = delete_data['Member_ID']
    Exercise_ID = delete_data['Exercise_ID']
    
    conn = get_db_conn()
    member = conn.execute('SELECT * FROM Members WHERE Mem_ID = ?', (Member_ID,)).fetchone()
    conn.close()
    if member is None:
        return jsonify({'error': 'Member not found'}), 404
    
    conn = get_db_conn()
    exercise = conn.execute('SELECT * FROM Exercises WHERE EX_ID = ?', (Exercise_ID,)).fetchone()
    conn.close()
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404
    
    conn = get_db_conn()
    conn.execute('DELETE FROM Do WHERE Member_ID = ? AND Exercise_ID = ?', (Member_ID, Exercise_ID))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Relation-Do deleted'})


# routes of Consist
@app.route('/consist', methods=['POST'])
def create_consist():
    new_consist = request.get_json()
    Sub_Pack = new_consist['Sub_Pack']
    Exercise_ID = new_consist['Exercise_ID']
    
    conn = get_db_conn()
    subscription = conn.execute('SELECT * FROM Subscriptions WHERE Sub_ID = ?', (Sub_Pack,)).fetchone()
    conn.close()
    if subscription is None:
        return jsonify({'error': 'Subscription not found'}), 404
    
    conn = get_db_conn()
    exercise = conn.execute('SELECT * FROM Exercises WHERE EX_ID = ?', (Exercise_ID,)).fetchone()
    conn.close()
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404
    
    conn = get_db_conn()
    consist = conn.execute('SELECT * FROM Consist WHERE Sub_Pack = ? AND Exercise_ID = ?', (Sub_Pack, Exercise_ID)).fetchone()
    conn.close()
    if consist:
        return jsonify({'error': 'Relation-Consist has already existed'}), 500
    
    conn = get_db_conn()
    conn.execute('INSERT INTO Consist (Sub_Pack, Exercise_ID) VALUES (?, ?)', (Sub_Pack, Exercise_ID))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Relation-Consist created'}), 201

@app.route('/consist', methods=['GET'])
def get_consist():
    conn = get_db_conn()
    all_consist = conn.execute('SELECT Subscriptions.Duration, Consist.Sub_Pack, Exercises.EX_Name as Exercise, Consist.Exercise_ID FROM Consist JOIN Subscriptions ON Consist.Sub_Pack = Subscriptions.Sub_ID JOIN Exercises ON Consist.Exercise_ID = Exercises.EX_ID').fetchall()
    conn.close()
    
    return jsonify([dict(consist) for consist in all_consist])

@app.route('/consist', methods=['DELETE'])
def delete_consist():
    delete_data = request.get_json()
    Sub_Pack = delete_data['Sub_Pack']
    Exercise_ID = delete_data['Exercise_ID']
    
    conn = get_db_conn()
    subscription = conn.execute('SELECT * FROM Subscriptions WHERE Sub_ID = ?', (Sub_Pack,)).fetchone()
    conn.close()
    if subscription is None:
        return jsonify({'error': 'Subscription not found'}), 404
    
    conn = get_db_conn()
    exercise = conn.execute('SELECT * FROM Exercises WHERE EX_ID = ?', (Exercise_ID,)).fetchone()
    conn.close()
    if exercise is None:
        return jsonify({'error': 'Exercise not found'}), 404
    
    conn = get_db_conn()
    conn.execute('DELETE FROM Consist WHERE Sub_Pack = ? AND Exercise_ID = ?', (Sub_Pack, Exercise_ID))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Relation-Consist deleted'})

if __name__ == '__main__':
    app.run(debug=True)
