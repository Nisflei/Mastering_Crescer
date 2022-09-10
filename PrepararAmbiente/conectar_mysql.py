import mysql.connector

DBConnect = mysql.connector.connect(host='localhost', database='ProjetoSQL', user='root', password='Info@1234')

if DBConnect.is_connected():
    # ver informações do servidor MySQL
    db_info = DBConnect.get_server_info()
    print('Conectado ao servidor MySQL: ', db_info)

    # enviar um comando SQL para o Servidor MySQL
    cursor = DBConnect.cursor()
    cursor.execute("select database();")
    retorno = cursor.fetchone()
    print("Conectado ao banco de dados: ", retorno)

    cursor.close()
    DBConnect.close()
    print("Conexão ao MySQL Encerrada.....")


