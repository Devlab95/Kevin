import pymysql 
import os

connection = pymysql.connect(host='localhost',user='root',passwd='',db='mysql-python')
mycursor = connection.cursor()
def showTB():

	print("\n\tTable\n-----------------------")
	mycursor.execute("SHOW TABLES")
	fetch = mycursor.fetchall()
	for x in fetch:
		print("\n  "+str(x))

def showColumn():
	print("\n\tColumn\n----------------------")
	mycursor.execute("SELECT id,names FROM branch ;")
	f2 = mycursor.fetchall()
	for y in f2:
		print('\n  '+str(y))

def rmDB():

	box = input ("\n$:rmDB\\> ")
	mycursor.execute("DELETE FROM branch WHERE names='"+box+"';")
	print("\n"+box+" Deleted Successfull !")


def insrtDB():
	box = input("\n$:insertDB\\> ")
	# box2 = input("\n$:IDNO:\\>  ")
	if str(0) < box :
		mycursor.execute("INSERT INTO branch (names) VALUES('"+box+"')")
	else:
		print("\n\tData Not Inserted !!\n")


def update():
	boxid = input("\nEnter-> ")
	boxcn = input("\nEnter:Value-> ")
	mycursor.execute("UPDATE branch SET names='"+str(boxcn)+"' WHERE names='"+str(boxid)+"'")

def updateid():
	boxid = input("\nEnter-> ")
	boxcn = input("\nEnter:Value-> ")
	mycursor.execute("UPDATE branch SET id="+str(boxcn)+" WHERE names='"+str(boxid)+"';")

def clear():
	clear = lambda: os.system('cls') #on Windows System
	clear()
def help():
	print("""
Help Menu:
   [Option]:->

Insert\t-   Insert Data In To DataBase
show:
	show-all\t-   Show Table & Colm in Database
	show-col\t-   Show Only Columns in Database
	show-table\t-   Show Only Table in Database
	update-id\t-   Update Data id in Database

update\t-  Update Data in To Database
rmDB\t-  Delete Data In To Databse
clear\t-   Clear terminal Screen
cls\t-   Clear Terminal Screen
exit\t-   Exit The Program
help\t-   Help Menu

		""")


while True:
	box = input("\nRoot@Database:~# ")
	if box == 'show-table':
		showTB()
	elif box == 'show-col':
		showColumn()
	elif box == 'show-all':
		showTB()
		showColumn()
	elif box == 'rmDB':
		rmDB()
	elif box == 'insert':
		insrtDB()
	elif box == 'update':
		update()
	elif box == 'update-id':
		updateid()
	elif box == 'clear' or box == 'cls' :
		clear()
	elif box == 'exit':
		break
	elif box == 'help':
		help()
	else:
		print("\n\tCommand Not Found !\n")



connection.commit()
connection.close()

