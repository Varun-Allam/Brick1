import sqlite3 

conn = sqlite3.connect("becky.db") 

cursor = conn.cursor() 

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))" 
cursor.execute(query)  

#query = "INSERT INTO sys_command VALUES (null,'Google Chrome', 'Macintosh HD/Applications/bin/Google Chrome')" 
#cursor.execute(query) 
#conn.commit()  

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),url VARCHAR(1000))" 
cursor.execute(query)  

#query = "INSERT INTO web_command VALUES (null,'Google', 'https://www.google.com/')" 
#cursor.execute(query) 
#conn.commit()  

