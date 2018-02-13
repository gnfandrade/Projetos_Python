import mysql.connector as mysqlcnx

cnx = mysqlcnx.connect(user='root', password='123@abc', host='192.168.30.2', database='python')

cursor = cnx.cursor()

id = 2

cursor.execute("DELETE FROM nomes WHERE idnomes = %s", (id,))

cnx.commit()

print("Registro excluído com sucesso !!!")

cursor.close()
cnx.close()