import sqlite3

conn = sqlite3.connect('answer.db')

c = conn.cursor()
c.execute('''
                CREATE TABLE ANSWER
                (ID INT PRIMARY KEY NOT NULL,
                TITLE CHAR(200) NOT NULL,
                ANSWER CHAR(200));
            ''')
conn.commit()
conn.close()

print(conn)