import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv('DB_HOST', '127.0.0.1'),
    port=int(os.getenv('DB_PORT', 3307)),
    user=os.getenv('DB_USER', 'sneha'),
    password=os.getenv('DB_PASSWORD', 'Sneha@123'),
    database=os.getenv('DB_NAME', 'sneha')
)

cursor = conn.cursor()
cursor.execute("SELECT NOW();")
result = cursor.fetchone()

print("Connected Successfully", result)

cursor.execute("""
INSERT INTO students (name, email) VALUES
('John Doe', 'johndoe@example.com'),
('Jane Smith', 'janesmith@example.com');
                """)

conn.commit()

cursor.execute("SELECT * FROM students;")
for row in cursor.fetchall():
    print(row)
cursor.close()
conn.close()