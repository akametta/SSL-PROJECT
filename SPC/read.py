import sqlite3
connection = sqlite3.connect("db.sqlite3")
mycursor = connection.cursor()
mycursor.execute("""SELECT * FROM auth_user""")
ans=mycursor.fetchall()
for i in ans:
	print(i)
connection.close()