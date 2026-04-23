import pymysql
conn=pymysql.connect(host='localhost',user='tharun4',password='Tharun@4237')
print("Connected")
cur=conn.cursor()
cur.execute("use hotel")
cur.execute("select * from hotels")
tables=cur.fetchall()
for x in tables:
    print(x)