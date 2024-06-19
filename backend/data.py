import requests

# Create Trainers
trainer_url = "http://127.0.0.1:5000/trainers"
trainers = [
    {
        "T_Name": "Test1",
        "Email_ID": "test1@test.com",
        "Phone": "0900-000-001",
        "Gender": "M",
        "Hire_Date": "2024-01-01",
        "Salary": 50000
    },
    {
        "T_Name": "Test2",
        "Email_ID": "test2@test.com",
        "Phone": "0900-000-002",
        "Gender": "M",
        "Hire_Date": "2024-01-01",
        "Salary": 50000
    },
    {
        "T_Name": "Test3",
        "Email_ID": "test3@test.com",
        "Phone": "0900-000-003",
        "Gender": "F",
        "Hire_Date": "2024-01-01",
        "Salary": 50000
    }
]

def create_trainer(trainer):
    response = requests.post(trainer_url, json=trainer)
    if response.status_code == 201:
        print("Create trainer successfully")
    else:
        print("Failed to create trainer")

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
        "Duration": 1
    },
    {
        "Price": 4000,
        "Duration": 3
    }
]

def create_subscription(subscription):
    response = requests.post(subscription_url, json=subscription)
    if response.status_code == 201:
        print("Create subscription successfully")
    else:
        print("Failed to create subscription")

for subscription in subscriptions:
    create_subscription(subscription)

# Create Equipments
equipment_url = "http://127.0.0.1:5000/equipments"
equipments = [
    {
        "Name": "Treadmill",
        "Quantity": 5,
        "Cost": 10000
    },
    {
        "Name": "Spinning Bike",
        "Quantity": 5,
        "Cost": 8000
    },
    {
        "Name": "Dumbbell",
        "Quantity": 5,
        "Cost": 5000
    }
]

def create_equipment(equipment):
    response = requests.post(equipment_url, json=equipment)
    if response.status_code == 201:
        print("Create equipment successfully")
    else:
        print("Failed to create equipment")

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
    }
]

def create_exercise(exercise):
    response = requests.post(exercise_url, json=exercise)
    if response.status_code == 201:
        print("Create exercise successfully")
    else:
        print("Failed to create exercise")

for exercise in exercises:
    create_exercise(exercise)
