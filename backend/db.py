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
            T_Name TEXT NOT NULL,
            Email_ID TEXT,
            Phone TEXT,
            Gender TEXT,
            Hire_Date TEXT NOT NULL,
            Salary REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Members (
            Mem_ID INTEGER PRIMARY KEY,
            M_Name TEXT NOT NULL,
            Phone TEXT,
            Start_Date TEXT NOT NULL,
            Gender TEXT,
            Subs INTEGER NOT NULL,
            Height REAL,
            Weight REAL,
            Age INTEGER,
            Email_ID TEXT,
            Trainer_ID INTEGER NOT NULL,
            FOREIGN KEY (Trainer_ID) REFERENCES Trainers(T_ID) ON DELETE CASCADE ON UPDATE CASCADE
            FOREIGN KEY (Subs) REFERENCES Subscriptions(Sub_ID) ON DELETE CASCADE ON UPDATE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Subscriptions (
            Sub_ID INTEGER PRIMARY KEY,
            Price REAL NOT NULL,
            Duration TEXT NOT NULL,
            Sub_Num INTEGER DEFAULT 0
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Consist (
            Sub_Pack INTEGER,
            Exercise_ID INTEGER,
            PRIMARY KEY (Sub_Pack, Exercise_ID),
            FOREIGN KEY (Sub_Pack) REFERENCES Subscriptions(Sub_ID) ON DELETE CASCADE,
            FOREIGN KEY (Exercise_ID) REFERENCES Exercises(EX_ID) ON DELETE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Equipment (
            Eq_ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Quantity INTEGER,
            Cost REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Use (
            Member_ID INTEGER,
            Equipment_ID INTEGER,
            PRIMARY KEY (Member_ID, Equipment_ID),
            FOREIGN KEY (Member_ID) REFERENCES Members(Mem_ID) ON DELETE CASCADE,
            FOREIGN KEY (Equipment_ID) REFERENCES Equipment(Eq_ID) ON DELETE CASCADE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Exercises (
            EX_ID INTEGER PRIMARY KEY,
            EX_Name TEXT NOT NULL,
            Type TEXT NOT NULL,
            Time_Slot TEXT NOT NULL,
            Frequency TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Do (
            Member_ID INTEGER,
            EX_ID INTEGER,
            PRIMARY KEY (Member_ID, EX_ID),
            FOREIGN KEY (Member_ID) REFERENCES Members(Mem_ID) ON DELETE CASCADE,
            FOREIGN KEY (EX_ID) REFERENCES Exercises(EX_ID) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
