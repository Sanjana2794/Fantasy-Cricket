import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "database", "fantasy_cricket.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


# MATCH TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS match (
    player TEXT,
    scored INTEGER,
    faced INTEGER,
    fours INTEGER,
    sixes INTEGER,
    bowled INTEGER,
    maiden INTEGER,
    given INTEGER,
    wkts INTEGER,
    catches INTEGER,
    stumping INTEGER,
    runout INTEGER
)
""")

# STATS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS stats (
    player TEXT,
    matches INTEGER,
    runs INTEGER,
    hundreds INTEGER,
    fifties INTEGER,
    value INTEGER,
    ctg TEXT
)
""")

# TEAMS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS teams (
    name TEXT,
    players TEXT,
    value INTEGER
)
""")

conn.commit()
conn.close()

print("Database created successfully")
