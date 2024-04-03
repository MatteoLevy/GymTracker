import sqlite3
from datetime import datetime

conn = sqlite3.connect('workouts.db')
cur = conn.cursor()
current_time = datetime.now()

# Create Workouts, Sets and Exercises tables, if they do not alrady exist
cur.executescript('''
CREATE TABLE IF NOT EXISTS Workouts(
                  id INTEGER PRIMARY KEY,
                  date TEXT
);

CREATE TABLE IF NOT EXISTS Sets(
                  id INTEGER PRIMARY KEY,
                  workout_id INTEGER,
                  count INTEGER
);                

CREATE TABLE IF NOT EXISTS Exercises(
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  set_id INTEGER
);                         
''')

# Verify that the input is among the valid options, throws error otherwise and asks for input again.
start_workout_choices = ["Y", "N"]
while True:
    start_workout = input('Start workout (Y/N)? ').upper()
    if start_workout in start_workout_choices:
        break
    else:
        print('Error! Value not allowed! It must be "Y" or "N"')

if start_workout == 'Y':
    
    # Insert a new row in the Workouts table
    cur.execute('''INSERT OR IGNORE INTO Workouts (date)
                VALUES ( ? )''', (current_time, ))
    
    conn.commit()

    # Provides the ID of the Workout created in the Workputs table
    cur.execute('SELECT id FROM Workouts WHERE date = ? ', (current_time, ))
    workout_id = cur.fetchone()[0]
    print("Workout ID: ", workout_id)

    conn.close()

    exercise = input('Exercise? ')
    while True:
        # Verify that the reps input is an integer, throws error otherwise and asks for input again.
        while True:
            try: 
                reps = int(input('Reps? '))
                break
            except ValueError: 
                print('Error! Insert an integer number (e.g. \'8\' or \'12\')')
                continue
        
        # Verify that the input is among the valid options, throws error otherwise and asks for input again.
        valid_choices = ["R", "N", "Q"]
        while True:
            choice = input('More reps (R), new exercise (N), or end workout (Q)? ').upper()
            if choice in valid_choices:
                break
            else:
                print('Error! Value not allowed! It must be "R", "N", or "Q"')

        if choice == 'R':
            continue
        elif choice == 'N': 
            next_exercise = input('Next exercise? ')
        elif choice == 'Q': 
            break
        else: 
            print('Error!')
    print('Well done!')
else: 
    print('Alright, see you next time!')
    quit()
