import mysql.connector
   
#Create the connection object
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root", 
	passwd = "",
	database="demo"
)
   
#printing the connection object

my_process = mydb.cursor()
# my_process.execute("CREATE TABLE typeapp (ID VARCHAR(255), NAME VARCHAR(255), TYPE VARCHAR(255), URL VARCHAR(255))")
# my_process.execute("SELECT * FROM typeapp")
# fomula = "INSERT INTO typeapp (ID,NAME,TYPE,URL) VALUES (%s,%s,%s,%s)"
# google = ("1","google","WEB_SEARCH","https://www.google.com/")
# my_process.execute(fomula,google)
# mydb.commit()
# my_process.execute("SELECT * FROM typeapp")
# for row in my_process.fall()
my_process.execute("SELECT * FROM typeapp")
for row in my_process.fetchall():
	print(row)
mydb.close()
