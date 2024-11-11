# Importar a biblioteca do pyqt
from PyQt5 import uic, QtWidgets
import sqlite3
# Função para salvar os registros
def salvar_dados():

    # Criar as variáveis
    id = tela.lineEdit_id.text()
    nome = tela.lineEdit_nome.text()
    instituicao = tela.lineEdit_instituicao.text()


    try:
        # Criando a conexão com o banco de dados
        banco = sqlite3.connect('cursos.db')

        # Criação do objeto cursor
        cursor = banco.cursor()

        # Criação da tabela no banco de dados
        cursor.execute("CREATE TABLE IF NOT EXISTS curso(id integer, nome text, instituicao text)")

        # inserir dados na tabela
        cursor.execute("INSERT INTO curso VALUES('"+id+"','"+nome+"','"+instituicao+"')")

        # commit para confirmar as alterações
        banco.commit()

        # Fechar a conexão com o banco
        banco.close()

        print("Os dados foram inseridos com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ", erro )

# Criar uma função pra listar os dados na tabela
def listar_dados():

    tela2.show()
    
    # Criando a conexão com o banco de dados
    banco = sqlite3.connect('cursos.db')

    # Criação do objeto cursor
    cursor = banco.cursor()

    # Consultando os dados na tabela
    cursor.execute("SELECT * FROM curso")

    # Armazenando em uma variável
    dados_lidos = cursor.fetchall()

    # Exibindo os dados na tabela
    tela2.tableWidget.setRowCount(len(dados_lidos))
    tela2.tableWidget.setColumnCount(3)
    
    # Percorrer uma matriz de dados que seja exibido na tela 
    for i in range(0, len(dados_lidos)):
        for j in range(0,3):
            tela2.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    banco.close()



# Estrutura para abrir a página
app = QtWidgets.QApplication([])
tela = uic.loadUi("cadastro_curso.ui")
tela2 = uic.loadUi("listar.ui")

tela.pushButton_salvar.clicked.connect(salvar_dados)
tela.pushButton_listar.clicked.connect(listar_dados)

# Comandos para abrir a tela
tela.show()
app.exec()