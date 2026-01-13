import sqlite3

def insecure(user_input):
    conn = sqlite3.connect("test.db")
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    conn.execute(query)
