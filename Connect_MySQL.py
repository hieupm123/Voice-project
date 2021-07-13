import mysql.connector

class connect_database_web_and_app:
	mydb = mysql.connector.connect(
		host = "localhost",
		user = "root", 
		passwd = "",
		database=
	)
	def query_database_search(sefl):
		