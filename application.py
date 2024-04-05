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
         
CREATE TABLE IF NOT EXISTS Exercises(
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  workout_id INTEGER,
                  sets_counter INTEGER,
                  reps_counter INTEGER
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
    sets_counter = 0

    while True:
        sets_counter += 1
        exercise = input('Exercise? ')
        reps_counter = int(input('Reps? '))

        # Insert a new row in the Exercises table
        cur.execute('''INSERT OR IGNORE INTO Exercises (name, workout_id, sets_counter, reps_counter)
                    VALUES ( ? , ? , ? , ? )''', (exercise, workout_id, sets_counter, reps_counter))
        
        conn.commit()

        # Provides the ID of the Exercise created in the Exercises table
        cur.execute('SELECT id FROM Exercises WHERE name = ? AND workout_id = ? AND sets_counter = ? AND reps_counter = ?', (exercise, workout_id, sets_counter, reps_counter))
        exercise_id = cur.fetchone()[0]
        print("Exercise ID: ", exercise_id)

        choice = input('More reps (R), new exercise (N), or end workout (Q)? ').upper()

        while choice == "R":
            sets_counter += 1
            reps_counter = int(input('Reps? '))

            # Insert a new row in the Exercises table
            cur.execute('''INSERT OR IGNORE INTO Exercises (name, workout_id, sets_counter, reps_counter)
                        VALUES ( ? , ? , ? , ? )''', (exercise, workout_id, sets_counter, reps_counter))
            
            conn.commit()

            # Provides the ID of the Exercise created in the Exercises table
            cur.execute('SELECT id FROM Exercises WHERE name = ? AND workout_id = ? AND sets_counter = ? AND reps_counter = ?', (exercise, workout_id, sets_counter, reps_counter))
            exercise_id = cur.fetchone()[0]
            print("Exercise ID: ", exercise_id)

            choice = input('More reps (R), new exercise (N), or end workout (Q)? ').upper()

            if choice != 'R':
                sets_counter = 0
                break

        if choice == 'N':
             continue
        if choice == 'Q':
            break
    
    print('Well done!')

    conn.close()

else: 
    print('Alright, see you next time!')
    quit()