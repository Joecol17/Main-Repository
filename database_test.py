from flask import Flask
import sqlite3 as SQLite3
from pathlib import Path

DB_PATH = Path("data.db")

def build_db():
	connection = SQLite3.connect(DB_PATH)
	connection.execute("""
		CREATE TABLE IF NOT EXISTS
		people (
			id INTEGER PRIMARY KEY,
			name TEXT NOT NULL
		);
	""")
	connection.commit()
	connection.close()

def prepopulate_db():
	connection = SQLite3.connect(DB_PATH)
	query = connection.execute("SELECT * FROM people;")
	people = query.fetchall()
	if not people:
		connection.executemany(
			"INSERT INTO people (name) VALUES (?);",
			[("Alice",), ("Bob",), ("Charlie",)]
		)
	connection.commit()
	connection.close()

def get_db():
	connection = SQLite3.connect(DB_PATH)
	connection.row_factory = SQLite3.Row
	return connection

build_db()
prepopulate_db()

app = Flask(__name__)

@app.route("/api/people", methods=["GET"])
def list_people():
	connection = get_db()
	query = connection.execute("SELECT * FROM people")
	people = query.fetchall()
	connection.close()
	return [dict(person) for person in people]

print(" * You might like to visit http://localhost:5000/api/people")
app.run()
