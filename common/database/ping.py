import sqlite3
# Connect to an in-memory database to check if the connection is still available.
conn = sqlite3.connect(":memory:")
print("Connected Successfully.")
conn.close()