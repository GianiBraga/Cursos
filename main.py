# Importar a biblioteca do pyqt
from PyQt5 import uic, QtWidgets

# Estrutura para abrir a página
app = QtWidgets.QApplication([])
tela = uic.loadUi("cadastro_curso.ui")

# Comandos para abrir a tela
tela.show()
app.exec()