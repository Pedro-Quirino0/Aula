import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='SensorAranha',
    autocommit=True
)

cursor = conexao.cursor()
