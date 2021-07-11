import mysql.connector
   
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root", 
	passwd = "",
)

class connect_database:
	def query_database_search(sefl):
		