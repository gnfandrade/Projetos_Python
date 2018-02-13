import mysql.connector as mysqlcnx

cnx = mysqlcnx.connect(user='root', password='123@abc', host="192.168.30.2", database='python')

cursor = cnx.cursor()

cursor.execute("SELECT * FROM nomes;")

for linha in cursor.fetchall():
    print(linha)

cursor.close()
cnx.close()



