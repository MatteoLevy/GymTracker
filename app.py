import sqlite3
from datetime import datetime
from utils.dataHandler import create_tables, insert_workout
from utils.inputValidator import get_string_input, get_integer_input


conn = sqlite3.connect("workouts.db")
cur = conn.cursor()
current_time = datetime.now().isoformat()


create_tables()


def main():
    create_tables()
    start_workout = get_string_input("Start workout (Y/N)? ", ["Y", "N"])
    if start_workout == "Y":
        insert_workout()
        cur.execute("SELECT id FROM Workouts WHERE date = ? ", (current_time,))
        workout_id = cur.fetchone()[0]
        sets_counter = 0

        while True:
            sets_counter += 1
            exercise = get_string_input("Exercise? ")
            reps_counter = get_integer_input("Reps? ")

            # Insert a new row in the Exercises table
            cur.execute(
                """INSERT OR IGNORE INTO Exercises (workout_id, name)
                        VALUES ( ? , ? )""",
                (workout_id, exercise),
            )

            conn.commit()

            # Provides the ID of the Exercise created in the Exercises table
            cur.execute(
                "SELECT MAX(id) FROM Exercises WHERE workout_id = ? AND name = ? ",
                (workout_id, exercise),
            )
            exercise_id = cur.fetchone()[0]

            # Insert a new row in the Sets table
            cur.execute(
                """INSERT OR IGNORE INTO Sets (exercise_id, sets_counter, reps_counter)
                        VALUES ( ? , ? , ? )""",
                (exercise_id, sets_counter, reps_counter),
            )

            conn.commit()

            choice = get_string_input(
                "More reps (R), new exercise (N), or end workout (Q)? ", ["R", "N", "Q"]
            )
            while choice == "R":
                sets_counter += 1
                reps_counter = get_integer_input("Reps? ")

                # Insert a new row in the Exercises table
                cur.execute(
                    """INSERT OR IGNORE INTO Exercises (workout_id, name)
                            VALUES ( ? , ? )""",
                    (workout_id, exercise),
                )

                conn.commit()

                # Provides the ID of the Exercise created in the Exercises table
                cur.execute(
                    "SELECT MAX(id) FROM Exercises WHERE workout_id = ? AND name = ? ",
                    (workout_id, exercise),
                )
                exercise_id = cur.fetchone()[0]

                # Insert a new row in the Sets table
                cur.execute(
                    """INSERT OR IGNORE INTO Sets (exercise_id, sets_counter, reps_counter)
                            VALUES ( ? , ? , ? )""",
                    (exercise_id, sets_counter, reps_counter),
                )

                conn.commit()

                choice = get_string_input(
                    "More reps (R), new exercise (N), or end workout (Q)? ",
                    ["R", "N", "Q"],
                )

            if choice == "N":
                sets_counter = 0
                continue
            if choice == "Q":
                break

        print("Well done!")

    else:
        print("Alright, see you next time!")
        quit()

    conn.close()


if __name__ == "__main__":
    main()
