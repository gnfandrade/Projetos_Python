import mysql.connector as mysqlcnx

cnx = mysqlcnx.connect(user='root', password='123@abc', host='192.168.30.2', database='python')

cursor = cnx.cursor()

id = 2
telefone = '(31)2222-2323'

cursor.execute("UPDATE nomes SET telefone=%s WHERE idnomes=%s", (telefone, id))

cnx.commit()

print("Dados atualizados com sucesso !!!")

cursor.close()
cnx.close

