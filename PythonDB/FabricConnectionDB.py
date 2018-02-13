import mysql.connector as mysqlcnx

# Classe que inicia uma comunicação com o banco de dados passado conforme parâmetro em 'connect'
class FabricConnectionDB(object):

    def __init__(self, db_name):
        try:
            self.cnx = mysqlcnx.connect(user='root', password='123@abc', host='192.168.30.2', database=db_name)
            self.cursor = self.cnx.cursor()
        except mysqlcnx.Error as err:
            print(err)

    def commit_db(self):
        if self.cnx:
            self.cnx.commit()

    #Método para fechar a conexão do cursor e o banco de dados.
    def CloseConnection(self):

        if self.cursor:
            self.cursor.close()
            print("Cursor Fechado")

        if self.cnx:
            self.cnx.close()
            print("Conexão com o Banco Fechada")

# Classe que representa a tabela nomes no banco de dados.
class NomesDB(object):

    def __init__(self):
        self.db = FabricConnectionDB('python')

    def close_connection(self):
        self.db.CloseConnection()

    def inserir_um_registro(self):
        try:
            self.db.cursor.execute("INSERT INTO nomes (nome, email, telefone) VALUE('Paulo dos Reis', 'paulo@gmail.com', '(11)2121-4444')")
            self.db.commit_db()
            print("Registro Inserido com Sucesso !")
        except mysqlcnx.Error as err:
            print(err)
            return False

# Abaixo inicia-se os métodos para realizar o CRUD (CREATE, READ, UPDATE, DELETE)
    def inserir_lista(self):
        lista = [('Agenor da Silva', 'agenor@uol.com.br', '(21)5555-7676'),
                 ('Carla de Souza', 'carla@outlook.com', '(11)2929-0001'),
                 ('Fábio da Costa', 'faabio@gmail.com', '(11)6666-4444'),
                 ('Larissa Picon', 'larissa.picon@hotmail.com', '(21)7777-8888')
                 ]

        try:
            self.db.cursor.executemany('INSERT INTO nomes(nome, email, telefone) VALUES(%s, %s, %s)', lista)
            self.db.commit_db()
            print("Informações Inseridas com Sucesso a partir de uma Lista com: %s Registros"%len(lista))
        except mysqlcnx.Error as err:
            print(err)

    def ler_todas_pessoas(self):
        self.db.cursor.execute("SELECT * FROM nomes")
        return self.db.cursor.fetchall()

    def imprimir_todas_pessoas(self):
        lista = self.ler_todas_pessoas()

        for lst in lista:
            print(lst)

    def localizar_pessoa(self, idnomes):
        self.db.cursor.execute("SELECT * FROM nomes WHERE idnomes = %s", (idnomes,))
        return self.db.cursor.fetchall()

    def atualizar(self, idnomes):
        try:
            p = self.localizar_pessoa(idnomes)
            if p:
                self.novo_email = input("Email: ")
                self.db.cursor.execute("UPDATE nomes SET email = %s WHERE idnomes = %s", (self.novo_email, idnomes,))
                self.db.commit_db()
                print("Dados Atualizados com Sucesso !!!")
            else:
                print("Pessoa inexistente conforme id informado !")
        except mysqlcnx.Error as err:
            print(err)

    def deletar(self, idnomes):
        try:
            p = self.localizar_pessoa(idnomes)
            if p:
                self.db.cursor.execute("DELETE FROM nomes WHERE idnomes = %s", (idnomes,))
                self.db.commit_db()
                print("Pessoa Deletada com Sucesso !")
            else:
                print("Não existe Pessoa com id informado.")
        except mysqlcnx.Error as err:
            print(err)




if __name__ == '__main__':
    nomes = NomesDB()
    nomes.deletar(7)
    nomes.imprimir_todas_pessoas()
    nomes.close_connection()



