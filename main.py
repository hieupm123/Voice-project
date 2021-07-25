
driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

<<<<<<< HEAD
# Hieu sua
=======
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
>>>>>>> c3d60707dc7ab584f674eebf740421046a117ec1
