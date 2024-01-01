import sqlite3
import hashlib

db = sqlite3.connect('login_db.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS login
                  (username TEXT PRIMARY KEY,
                   password TEXT NOT NULL,
                   salt TEXT NOT NULL)''')

username = input("Enter a username: ")
password = input("Enter a password: ")

# Creates unique salt and hash
salt = hashlib.sha256(str(username).encode()).hexdigest()
hash_password = hashlib.pbkdf2_hmac('sha256', str(password).encode('utf-8'), salt.encode('utf-8'), 100000)

# Creates a new user with a password wih the unique salt and hash
cursor.execute("INSERT INTO login (username, password, salt) VALUES (?, ?, ?)", (username, hash_password, salt))
db.commit()
db.close()
