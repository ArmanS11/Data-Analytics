import json

# Load the JSON data
with open('MOCK_DATA.json', 'r') as file:
    data = json.load(file)

# Example: Print the first record
print("First Record:", data[0])

# Example: Extract and display all students' first names
first_names = [record['first_name'] for record in data]
print("First Names:", first_names[:10])

# Example: Filter students enrolled in a specific department (e.g., "History")
history_students = [record for record in data if record['department'] == "History"]
print(f"Number of students in History department: {len(history_students)}")

# Example: Group students by grade level
from collections import defaultdict

students_by_grade = defaultdict(list)
for record in data:
    students_by_grade[record['grade_level']].append(record)

for grade, students in students_by_grade.items():
    print(f"Grade {grade}: {len(students)} students")

import pandas as pd

# Load JSON data
df = pd.read_json('MOCK_DATA.json')

# Save as CSV
df.to_csv('mockaroo_dataset.csv', index=False)

# Save as SQL (optional)
from sqlalchemy import create_engine
engine = create_engine('sqlite:///data_school.db')
df.to_sql('students', engine, if_exists='replace', index=False)
