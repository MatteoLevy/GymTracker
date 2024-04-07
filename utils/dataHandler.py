import sqlite3
from datetime import datetime


conn = sqlite3.connect("workouts.db")
cur = conn.cursor()
current_time = datetime.now().isoformat()


# Create Workouts and Exercises tables, if they do not already exist
def create_tables():
    cur.executescript(
        """
    CREATE TABLE IF NOT EXISTS Workouts(
        id INTEGER PRIMARY KEY,
        date TEXT
    );
            
    CREATE TABLE IF NOT EXISTS Exercises(
        id INTEGER PRIMARY KEY,
        workout_id INTEGER,
        name TEXT
    );
    
    CREATE TABLE IF NOT EXISTS Sets(
        id INTEGER PRIMARY KEY,
        exercise_id INTEGER,
        sets_counter INTEGER,
        reps_counter INTEGER
    );                          
    """
    )


# Insert a new row in the Workouts table
def insert_workout():
    cur.execute(
        """INSERT OR IGNORE INTO Workouts (date)
                    VALUES ( ? )""",
        (current_time,),
    )

    conn.commit()
