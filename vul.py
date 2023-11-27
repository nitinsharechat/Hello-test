# Vulnerable code

user_input = "admin'; DROP TABLE users; --"
query = "SELECT * FROM users WHERE username = '" + user_input + "';"

# Secure code using parameterized queries
import sqlite3

user_input = "admin'; DROP TABLE users; --"
query = "SELECT * FROM users WHERE username = ?;"
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute(query, (user_input,))
