import sqlite3

def init_db():
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()

    # Enable foreign key support
    cursor.execute('PRAGMA foreign_keys = ON')

    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Trainers (
            T_ID INTEGER PRIMARY KEY,
            T_Name TEXT,
            Email_ID TEXT,
            Phone TEXT,
            Gender TEXT,
            Hire_Date TEXT,
            Salary REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Members (
            Mem_ID INTEGER PRIMARY KEY,
            M_Name TEXT,
            Phone TEXT,
            Start_Date TEXT,
            Gender TEXT,
            Subs INTEGER,
            Height REAL,
            Weight REAL,
            Age INTEGER,
            Email_ID TEXT,
            Trainer_ID INTEGER,
            FOREIGN KEY (Trainer_ID) REFERENCES Trainers(T_ID) ON DELETE CASCADE ON UPDATE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Subscriptions (
            Sub_ID INTEGER PRIMARY KEY,
            Price REAL,
            Duration TEXT,
            Sub_Num INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Consist (
            Sub_Pack INTEGER,
            Exercise_ID INTEGER,
            PRIMARY KEY (Sub_Pack, Exercise_ID),
            FOREIGN KEY (Sub_Pack) REFERENCES Subscriptions(Sub_ID),
            FOREIGN KEY (Exercise_ID) REFERENCES Exercises(EX_ID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Equipment (
            Eq_ID INTEGER PRIMARY KEY,
            Name TEXT,
            Quantity INTEGER,
            Cost REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Use (
            Member_ID INTEGER,
            Equipment_ID INTEGER,
            PRIMARY KEY (Member_ID, Equipment_ID),
            FOREIGN KEY (Member_ID) REFERENCES Members(Mem_ID),
            FOREIGN KEY (Equipment_ID) REFERENCES Equipment(Eq_ID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Exercises (
            EX_ID INTEGER PRIMARY KEY,
            EX_Name TEXT,
            Type TEXT,
            Time_Slot TEXT,
            Frequency TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Do (
            Member_ID INTEGER,
            EX_ID INTEGER,
            PRIMARY KEY (Member_ID, EX_ID),
            FOREIGN KEY (Member_ID) REFERENCES Members(Mem_ID),
            FOREIGN KEY (EX_ID) REFERENCES Exercises(EX_ID)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
