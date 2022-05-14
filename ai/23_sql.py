import sqlite3

conn = sqlite3.connect("test.db", isolation_level=None)  # auto commit
c = conn.cursor()
c.execute(
    "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
)

# c.execute("INSERT INTO user (name, age) VALUES (?, ?)", ("아이언맨", 30))
# c.execute("INSERT INTO user (name, age) VALUES (?, ?)", ("헐크", 35))
c.execute("SELECT * FROM user")
print(c.fetchall())


conn.close()
