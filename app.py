import sqlite3
from datetime import datetime
from utils.DataHandler import DataHandler
from utils.inputValidator import get_string_input, get_integer_input

conn = sqlite3.connect("workouts.db")
cur = conn.cursor()
current_time = datetime.now().isoformat()


def main():

    # Initialize database and database commands
    data_handler = DataHandler("workouts.db")

    # Create tables if not already existing
    data_handler.create_table("Workouts", id="INTEGER PRIMARY KEY", date="TEXT")
    data_handler.create_table(
        "Exercises", id="INTEGER PRIMARY KEY", workout_id="INTEGER", name="TEXT"
    )
    data_handler.create_table(
        "Sets",
        id="INTEGER PRIMARY KEY",
        exercise_id="INTEGER",
        sets_counter="INTEGER",
        reps_counter="INTEGER",
    )

    start_workout = get_string_input("Start workout (Y/N)? ", ["Y", "N"])
    if start_workout == "Y":
        # Insert a new workout in the Workouts table
        data_handler.insert_into_table("Workouts", date=current_time)

        cur.execute("SELECT id FROM Workouts WHERE date = ? ", (current_time,))
        workout_id = cur.fetchone()[0]
        sets_counter = 0

        while True:
            sets_counter += 1
            exercise = get_string_input("Exercise? ")
            reps_counter = get_integer_input("Reps? ")

            # Insert a new row in the Exercises table
            data_handler.insert_into_table(
                "Exercises", workout_id=workout_id, name=exercise
            )

            # Provides the ID of the Exercise created in the Exercises table
            cur.execute(
                "SELECT MAX(id) FROM Exercises WHERE workout_id = ? AND name = ? ",
                (workout_id, exercise),
            )
            exercise_id = cur.fetchone()[0]

            # Insert a new row in the Sets table
            data_handler.insert_into_table(
                "Sets",
                exercise_id=exercise_id,
                sets_counter=sets_counter,
                reps_counter=reps_counter,
            )

            choice = get_string_input(
                "More reps (R), new exercise (N), or end workout (Q)? ", ["R", "N", "Q"]
            )
            while choice == "R":
                sets_counter += 1
                reps_counter = get_integer_input("Reps? ")

                # Insert a new row in the Exercises table
                data_handler.insert_into_table(
                    "Exercises", workout_id=workout_id, name=exercise
                )

                # Provides the ID of the Exercise created in the Exercises table
                cur.execute(
                    "SELECT MAX(id) FROM Exercises WHERE workout_id = ? AND name = ? ",
                    (workout_id, exercise),
                )
                exercise_id = cur.fetchone()[0]

                # Insert a new row in the Sets table
                data_handler.insert_into_table(
                    "Sets",
                    exercise_id=exercise_id,
                    sets_counter=sets_counter,
                    reps_counter=reps_counter,
                )

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
