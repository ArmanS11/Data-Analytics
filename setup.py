import sqlite3
import pandas as pd

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("dataset_school.db")

# Load the JSON file into a DataFrame
students_data = pd.read_json("MOCK_DATA.json")

# Insert the DataFrame into the `students` table
students_data.to_sql("students", conn, if_exists="replace", index=False)

# Verify that the data was inserted
print("Data loaded into the 'students' table successfully!")
print(pd.read_sql("SELECT * FROM students LIMIT 5;", conn))

# Load the data from the 'students' table into a Pandas DataFrame
query = "SELECT * FROM students"
students_data = pd.read_sql(query, conn)

# Display the first few rows of the data
print(students_data.head())

# # Close the connection (you can re-open it later if needed)
# conn.close()


# Close the connection
conn.close()
