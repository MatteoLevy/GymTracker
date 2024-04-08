import sqlite3


class DatabaseHandler:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    # Method to create a table
    def create_table(self, table_name, **columns):
        try:
            # Columns is a dictionary containing column names as keys and data types as values
            column_definitions = ", ".join(
                [f"{column} {data_type}" for column, data_type in columns.items()]
            )
            create_table_query = (
                f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
            )
            self.cur.execute(create_table_query)
            self.conn.commit()
        except sqlite3.Error as error:
            print(f"Error creating table {table_name}: {error}")

    # Example create_table
    # data_handler = DataHandler("workouts.db")
    # data_handler.create_table("Workouts", id="INTEGER PRIMARY KEY", date="TEXT")

    # Insert new row(s) in a table
    def insert_into_table(self, table_name, **data):
        try:
            # Columns is a dictionary containing column names as keys and data types as values
            columns = ", ".join(data.keys())
            question_marks = ", ".join("?" * len(data))
            insert_query = f"INSERT OR IGNORE INTO {table_name} ({columns}) VALUES ({question_marks})"
            self.cur.execute(insert_query, tuple(data.values()))
            self.conn.commit()
        except sqlite3.Error as error:
            print(f"Error inserting row into table {table_name}: {error}")

    # Example insert_into_table
    # data_handler = DataHandler("workouts.db")
    # data_handler.insert_into_table("Workouts", date=current_time)
