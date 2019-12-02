import pymysql

User = input ("请输入名字：")
Password = input ("请输入密码：")


conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='',database='mysql',charset='utf8')

cursor = conn.cursor()

sql = """SELECT * from user where User = %s and Password = %s;"""


print(sql)

#ret = cursor.execute(sql,[User,Password])
ret = cursor.execute(sql)

print (ret)
cursor.close()
conn.close()

if ret:
	print ('登录成功')
else:
	print ('登录失败')
