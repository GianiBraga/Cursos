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




# Estrutura para abrir a página
app = QtWidgets.QApplication([])
tela = uic.loadUi("cadastro_curso.ui")

tela.pushButton_salvar.clicked.connect(salvar_dados)


# Comandos para abrir a tela
tela.show()
app.exec()