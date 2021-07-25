import sqlite3

conn = sqlite3.connect('process_func.db')

c = conn.cursor()


# customer
# c.execute("INSERT INTO customer VALUES('Hieu','minhhieu@minhhieu')")

c.execute("""
	SELECT * FROM customer ORDER BY name DESC
""")
# c.execute("DROP TABLE customer")
# print(c.fetchall())
# conn.commit()
conn.close()

#Cương sửa code
