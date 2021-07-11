import mysql.connector
   
#Create the connection object
mydb = mysql.connector.connect(
	host = "localhost",
	user = "root", 
	passwd = "",
	database="app_and_web"
)
   
#printing the connection object

my_process = mydb.cursor()
# my_process.execute("CREATE TABLE database_web_and_app (ID VARCHAR(255), NAME VARCHAR(255), TYPE VARCHAR(255), URL VARCHAR(255))")
# my_process.execute("CREATE DATABASE app_and_web")
# my_process.execute("SELECT * FROM app_and_web")


fomula = "INSERT INTO app_and_web (ID,NAME,TYPE,URL) VALUES (%s,%s,%s,%s)"
f = open('text.txt','r',encoding="utf8")
lines = f.readlines()
cnt = 1
a = ["Web_search","Web_watch_video","Web_chat","Shop_online","Same_spaper","Web_anathor"]
for i in range(0,len(lines),3):
	s = lines[i].replace("\n","")
	s1 = lines[i + 1].replace("\n","")
	app = (str(cnt),s,s1,a[int(lines[i + 2])])
	# print(app)
	my_process.execute(fomula,app)
	mydb.commit()
	cnt = cnt + 1

f.close()



# my_process.execute("SELECT * FROM typeapp")
# for row in my_process.fall()
# text = "TYPE"
# text = "SELECT NAME FROM typeapp where " + text + " = 'WEB_SEARCH'"
# my_process.execute(text)
# # my_process.execute("SELECT * FROM typeapp")
# for row in my_process.fetchall():
# 	print(row)
# 	for a in row:
# 		print(a);


mydb.close()
