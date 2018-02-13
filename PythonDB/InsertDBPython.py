import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root', password='123@abc', host='192.168.30.2', database='python')
    cursor = cnx.cursor()

    add_nomes = ("INSERT INTO nomes (nome, email, telefone) VALUES('Joaquim dos Santos', 'joaquim@gmail.com', '(21)2525-2424')")

    cursor.execute(add_nomes)

    cnx.commit()

    cursor.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DANIED_ERROR:
        print("Nome ou senha do servidor de Mysql inválidos!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de Dados inexixtente!")
    else:
        print(err)

finally:
    cnx.close()






