import sqlite3
from datetime import datetime

conn = sqlite3.connect('workouts.db')
cur = conn.cursor()
current_time = datetime.now().isoformat()

def create_tables():
    # Create Workouts and Exercises tables, if they do not alrady exist
    cur.executescript('''
    CREATE TABLE IF NOT EXISTS Workouts(
                    id INTEGER PRIMARY KEY,
                    date TEXT
    );
            
    CREATE TABLE IF NOT EXISTS Exercises(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    workout_id INTEGER,
                    sets_counter INTEGER,
                    reps_counter INTEGER
    );                         
    ''')

# Verify that the string input is among the valid choices, if any, and throws error otherwise and asks for input again.
def get_string_input(prompt, valid_choices=None):
    while True:
        user_input = input(prompt).upper()
        if valid_choices is None or user_input in valid_choices:
            return user_input
        else:
            print(f'Error! Value not allowed! Allowed choices: {", ".join(map(repr, valid_choices))}')

# Verify that the reps input is an integer, throws error otherwise and asks for input again.
def get_integer_input(prompt):
    while True:
        try: 
            user_input = int(input(prompt))
            return user_input
        except ValueError: 
            print('Error! Insert an integer number (e.g. \'8\' or \'12\')')

def main():
    create_tables()
    start_workout = get_string_input('Start workout (Y/N)? ', ['Y', 'N'])
    if start_workout == 'Y':
        # Insert a new row in the Workouts table
        cur.execute('''INSERT OR IGNORE INTO Workouts (date)
                    VALUES ( ? )''', (current_time, ))
        
        conn.commit()

        # Provides the ID of the Workout created in the Workputs table
        cur.execute('SELECT id FROM Workouts WHERE date = ? ', (current_time, ))
        workout_id = cur.fetchone()[0]
        sets_counter = 0

        while True:
            sets_counter += 1
            exercise = get_string_input('Exercise? ')
            reps_counter = get_integer_input('Reps? ')

            # Insert a new row in the Exercises table
            cur.execute('''INSERT OR IGNORE INTO Exercises (name, workout_id, sets_counter, reps_counter)
                        VALUES ( ? , ? , ? , ? )''', (exercise, workout_id, sets_counter, reps_counter))
            
            conn.commit()

            choice = get_string_input('More reps (R), new exercise (N), or end workout (Q)? ', ["R", "N", "Q"])
            while choice == "R":
                sets_counter += 1
                reps_counter = get_integer_input('Reps? ')

                # Insert a new row in the Exercises table
                cur.execute('''INSERT OR IGNORE INTO Exercises (name, workout_id, sets_counter, reps_counter)
                            VALUES ( ? , ? , ? , ? )''', (exercise, workout_id, sets_counter, reps_counter))
                
                conn.commit()

                choice = get_string_input('More reps (R), new exercise (N), or end workout (Q)? ', ["R", "N", "Q"])

            if choice == 'N':
                sets_counter = 0
                continue
            if choice == 'Q':
                break
        
        print('Well done!')

    else: 
        print('Alright, see you next time!')
        quit()

    conn.close()

if __name__ == "__main__":
    main()