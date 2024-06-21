import requests

# Create Trainers
trainer_url = "http://127.0.0.1:5000/trainers"
trainers = [
    {
        "T_Name": "Test1",
        "Email_ID": "test1@test.com",
        "Phone": "0900-000-001",
        "Gender": "Male",
        "Salary": 50000
    },
    {
        "T_Name": "Test2",
        "Email_ID": "test2@test.com",
        "Phone": "0900-000-002",
        "Gender": "Female",
        "Salary": 50000
    },
    {
        "T_Name": "Test3",
        "Email_ID": "test3@test.com",
        "Phone": "0900-000-003",
        "Gender": "Male",
        "Salary": 50000
    },
    {
        "T_Name": "Test4",
        "Email_ID": "test4@test.com",
        "Phone": "0900-000-004",
        "Gender": "Female",
        "Salary": 50000
    },
    {
        "T_Name": "Test5",
        "Email_ID": "test5@test.com",
        "Phone": "0900-000-005",
        "Gender": "Male",
        "Salary": 50000
    }
]

def create_trainer(trainer):
    response = requests.post(trainer_url, json=trainer)
    if response.status_code == 201:
        result = response.json()
        print(result)
    else:
        print("Failed to create trainer.")

for trainer in trainers:
    create_trainer(trainer)

# Create Subscriptions
subscription_url = "http://127.0.0.1:5000/subscriptions"
subscriptions = [
    {
        "Price": 1500,
        "Duration": 1
    },
    {
        "Price": 2800,
        "Duration": 2
    },
    {
        "Price": 4000,
        "Duration": 3
    },
    {
        "Price": 7000,
        "Duration": 6
    },
    {
        "Price": 11000,
        "Duration": 12
    }
]

def create_subscription(subscription):
    response = requests.post(subscription_url, json=subscription)
    if response.status_code == 201:
        result = response.json()
        print(result)
    else:
        print("Failed to create subscription.")

for subscription in subscriptions:
    create_subscription(subscription)

# Create Equipments
equipment_url = "http://127.0.0.1:5000/equipments"
equipments = [
    {
        "Name": "Treadmill",
        "Quantity": 1,
        "Cost": 25000
    },
    {
        "Name": "Spinning Bike",
        "Quantity": 1,
        "Cost": 20000
    },
    {
        "Name": "Dumbbell Set",
        "Quantity": 1,
        "Cost": 15000
    },
    {
        "Name": "Leg Press Machine",
        "Quantity": 1,
        "Cost": 35000
    },
    {
        "Name": "Lat Pulldown Machine",
        "Quantity": 1,
        "Cost": 50000
    }
]

def create_equipment(equipment):
    response = requests.post(equipment_url, json=equipment)
    if response.status_code == 201:
        result = response.json()
        print(result)
    else:
        print("Failed to create equipment.")

for equipment in equipments:
    create_equipment(equipment)

# Create Exercises
exercise_url = "http://127.0.0.1:5000/exercises"
exercises = [
    {
        "EX_Name": "Plank",
        "Type": "Upper Body",
        "Time_Slot": 3,
        "Frequency": 5
    },
    {
        "EX_Name": "Crunch",
        "Type": "Upper Body",
        "Time_Slot": 3,
        "Frequency": 5
    },
    {
        "EX_Name": "Squat",
        "Type": "Lower Body",
        "Time_Slot": 3,
        "Frequency": 5
    },
    {
        "EX_Name": "Push Up",
        "Type": "Upper Body",
        "Time_Slot": 3,
        "Frequency": 5
    },
    {
        "EX_Name": "Lunge",
        "Type": "Lower Body",
        "Time_Slot": 3,
        "Frequency": 5
    }
]

def create_exercise(exercise):
    response = requests.post(exercise_url, json=exercise)
    if response.status_code == 201:
        result = response.json()
        print(result)
    else:
        print("Failed to create exercise.")

for exercise in exercises:
    create_exercise(exercise)
