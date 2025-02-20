import mysql.connector
import hashlib


conn = mysql.connector.connect(
    host="localhost",  
    user="root",       
    password="password" 
)
cursor = conn.cursor()


cursor.execute("mydatabase")
cursor.execute("USE mydatabase")

cursor.execute('''
   users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        login VARCHAR(100) UNIQUE,
        password VARCHAR(255),
        phone_number VARCHAR(20),
        token VARCHAR(255)
    )
''')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
