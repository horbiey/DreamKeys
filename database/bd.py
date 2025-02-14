import mysql.connector
import hashlib


conn = mysql.connector.connect(
    host="localhost",  
    user="root",       
    password="password" 
)
cursor = conn.cursor()


cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
cursor.execute("USE mydatabase")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        login VARCHAR(100) UNIQUE,
        password VARCHAR(255),
        phone_number VARCHAR(20),
        token VARCHAR(255)
    )
''')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

cursor.execute("INSERT INTO users (login, password, phone_number, token) VALUES (%s, %s, %s, %s)", 
               ("ivan123", hash_password("mypassword"), "1234567890", "sampletoken123"))
cursor.execute("INSERT INTO users (login, password, phone_number, token) VALUES (%s, %s, %s, %s)", 
               ("maria456", hash_password("securepass"), "0987654321", "anothertoken456"))
conn.commit()  

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()