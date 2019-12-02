import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='',database='test',charset='utf8')

cursor = conn.cursor()

#sql1 = """CREATE TABLE USER1(id INT auto_increment PRIMARY KEY,name CHAR(10) NOT NULL UNIQUE,
#age TINYINT NOT NULL)ENGINE=innodb DEFAULT CHARSET=utf8;"""

#ret = cursor.execute(sql,[User,Password])
#cursor.execute(sql1)

#sql2 = """select * from USER1;"""
#ret = cursor.execute(sql2)

login_name = input ("请输入登录名：")
login_pwd = input ("请输入登录密码：")

sql3 = """ SELECT * from user1 where login_name = %s and login_pwd = %s;"""
print (sql3)

ret = cursor.execute(sql3,[login_name,login_pwd])
print("{}rows in set.".format(ret))
print("=" * 60)
print(ret)

print("=" * 60)

#ret2 = cursor.execute(sql3)
#print (ret2)
#print("=" * 60)
cursor.close()
conn.close()

if ret:
	print ('登录成功')
else:
	print ('登录失败')
