import psycopg2

# 获得连接对象
# database：数据库名称
# user：用户名
# password：密码
# host：数据库ip地址
# port：端口号，默认为5432
conn = psycopg2.connect(database="xinfang", user="runoob", password="password", host="127.0.0.1", port="5432")

# 获取游标对象
cursor = conn.cursor()
cursor.execute('''select * from xf ''')
result=cursor.fetchall()
print('succ')
conn.commit()
conn.close()