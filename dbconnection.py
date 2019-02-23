'''import pymysql
db=pymysql.connect("http://localhost","root","","mysql")
cursor=db.cursor()
cursor.execute("select version()")
db.commit()
data=cursor.fetchone()
print("db version:%s"%data)
db.close()'''


import pymysql
db=pymysql.connect("http://localhost","root","","mysql")
cursor=db.cursor()
sql="""insert onto sailors(sid,sname,sage)values(10,"smith",25)"""
cursor.execute(sql)
db.commit()

db.close()
