import sqlite3

import os
database_path = os.path.join(os.path.dirname(__file__), 'gym.db')

def init_db():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Enable foreign key support
    cursor.execute('PRAGMA foreign_keys = ON')

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Trainers (
            T_ID TEXT PRIMARY KEY,
            T_Name TEXT NOT NULL,
            Email_ID TEXT,
            Phone TEXT,
            Gender TEXT,
            Hire_Date TEXT NOT NULL,
            Salary REAL NOT NULL CHECK (Salary >= 50000)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Members (
            Mem_ID TEXT PRIMARY KEY,
            M_Name TEXT NOT NULL,
            Phone TEXT,
            Start_Date TEXT NOT NULL,
            Gender TEXT,
            Subs TEXT NOT NULL,
            Height REAL,
            Weight REAL,
            Age INTEGER,
            Email_ID TEXT,
            Trainer_ID TEXT NOT NULL,
            FOREIGN KEY (Trainer_ID) REFERENCES Trainers(T_ID) ON DELETE CASCADE ON UPDATE CASCADE
            FOREIGN KEY (Subs) REFERENCES Subscriptions(Sub_ID) ON DELETE CASCADE ON UPDATE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Subscriptions (
            Sub_ID TEXT PRIMARY KEY,
            Price REAL NOT NULL,
            Duration INTEGER NOT NULL CHECK (Duration >= 1),
            Sub_Num INTEGER DEFAULT 0
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Consist (
            Sub_Pack TEXT,
            Exercise_ID TEXT,
            PRIMARY KEY (Sub_Pack, Exercise_ID),
            FOREIGN KEY (Sub_Pack) REFERENCES Subscriptions(Sub_ID) ON DELETE CASCADE,
            FOREIGN KEY (Exercise_ID) REFERENCES Exercises(EX_ID) ON DELETE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Equipments (
            Eq_ID TEXT PRIMARY KEY,
            Name TEXT NOT NULL,
            Quantity INTEGER DEFAULT 10 CHECK (Quantity <= 10 AND Quantity >= 1),
            Cost REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Use (
            Member_ID TEXT,
            Equipment_ID TEXT,
            PRIMARY KEY (Member_ID, Equipment_ID),
            FOREIGN KEY (Member_ID) REFERENCES Members(Mem_ID) ON DELETE CASCADE,
            FOREIGN KEY (Equipment_ID) REFERENCES Equipments(Eq_ID) ON DELETE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Exercises (
            EX_ID TEXT PRIMARY KEY,
            EX_Name TEXT NOT NULL,
            Type TEXT NOT NULL CHECK (Type IN ('Upper Body', 'Lower Body', 'Arm')),
            Time_Slot INTEGER NOT NULL,
            Frequency INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Do (
            Member_ID TEXT,
            Exercise_ID TEXT,
            PRIMARY KEY (Member_ID, Exercise_ID),
            FOREIGN KEY (Member_ID) REFERENCES Members(Mem_ID) ON DELETE CASCADE,
            FOREIGN KEY (Exercise_ID) REFERENCES Exercises(EX_ID) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
