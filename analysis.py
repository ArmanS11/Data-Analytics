import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the SQLite database
conn = sqlite3.connect("dataset_school.db")

# Load the data from the 'students' table into a Pandas DataFrame
query = "SELECT * FROM students"
students_data = pd.read_sql(query, conn)

# Display the first few rows of the data
print(students_data.head())

# Close the connection (you can re-open it later if needed)
conn.close()
