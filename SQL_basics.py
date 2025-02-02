import pandas as pd

# Load data from CSV
df = pd.read_csv("data.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df["grade_level"] = df["grade_level"].fillna(df["grade_level"].mode()[0])

print(df.head())  # Preview cleaned data

import matplotlib.pyplot as plt
import seaborn as sns

# Plot student distribution by grade level
plt.figure(figsize=(8,5))
sns.countplot(x=df["grade_level"], palette="coolwarm")
plt.title("Student Count per Grade Level")
plt.xlabel("Grade Level")
plt.ylabel("Number of Students")
plt.show()
