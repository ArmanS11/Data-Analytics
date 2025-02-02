
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("dataset_school.db")
cursor = conn.cursor()

# 1. Create Tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS kids (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    favorite_toy TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS toys (
    id INTEGER PRIMARY KEY,
    toy_name TEXT NOT NULL,
    price REAL
);
""")

# 2. Insert Data
cursor.execute("""
INSERT INTO kids (id, name, age, favorite_toy)
VALUES
    (1, 'Alice', 5, 'Teddy Bear'),
    (2, 'Bob', 6, 'Lego Set'),
    (3, 'Charlie', 4, 'Train Set');
""")

cursor.execute("""
INSERT INTO toys (id, toy_name, price)
VALUES
    (1, 'Teddy Bear', 15.99),
    (2, 'Lego Set', 29.99),
    (3, 'Train Set', 19.99);
""")

conn.commit()

# 3. Query Examples
print("\n** Basic SELECT Query **")
cursor.execute("SELECT name, favorite_toy FROM kids;")
for row in cursor.fetchall():
    print(row)

print("\n** Filter with WHERE Clause **")
cursor.execute("SELECT name FROM kids WHERE age > 4;")
for row in cursor.fetchall():
    print(row)

print("\n** JOIN Query **")
cursor.execute("""
SELECT kids.name, kids.favorite_toy, toys.price
FROM kids
JOIN toys ON kids.favorite_toy = toys.toy_name;
""")
for row in cursor.fetchall():
    print(row)

print("\n** Aggregation Example **")
cursor.execute("""
SELECT favorite_toy, COUNT(*) as count
FROM kids
GROUP BY favorite_toy;
""")
for row in cursor.fetchall():
    print(row)

print("\n** Update Data Example **")
cursor.execute("UPDATE kids SET age = age + 1 WHERE name = 'Alice';")
conn.commit()
cursor.execute("SELECT name, age FROM kids;")
for row in cursor.fetchall():
    print(row)

print("\n** Delete Data Example **")
cursor.execute("DELETE FROM kids WHERE name = 'Charlie';")
conn.commit()
cursor.execute("SELECT * FROM kids;")
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()
