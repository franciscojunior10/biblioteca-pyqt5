from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem
from telas.tela_inicial import Ui_Tela_Inicio
from telas.tela_cadastro import Ui_Tela_Cadastro
from telas.tela_cadastro_livro import Ui_Tela_Cadastro_Livro
from telas.tela_principal import Ui_Tela_Principal
from telas.tela_acervo import Ui_Tela_Acervo
from PyQt5.QtGui import QPixmap
import PyQt5
import sys
import os
from PyQt5.QtCore import pyqtSlot

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1200, 900)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()

        self.tela_inicio = Ui_Tela_Inicio()
        self.tela_inicio.setupUi(self.stack0)

        self.tela_cadastro = Ui_Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_principal = Ui_Tela_Principal()
        self.tela_principal.setupUi(self.stack2)

        self.tela_cadastro_livro = Ui_Tela_Cadastro_Livro()
        self.tela_cadastro_livro.setupUi(self.stack3)

        self.tela_acervo = Ui_Tela_Acervo()
        self.tela_acervo.setupUi(self.stack4)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.tela_inicio.botao_entrar.clicked.connect(self.entrar)
        self.tela_inicio.botao_criar_conta.clicked.connect(self.openCriarConta)

        self.tela_cadastro.botao_salvar.clicked.connect(self.criarConta)
        self.tela_cadastro.toolButton.clicked.connect(self.voltarInicio)

        self.tela_principal.cadastrar_novo_livro.clicked.connect(self.openCadastrarLivro)
        self.tela_principal.ver_acervo.clicked.connect(self.openAcervoLivro)
        self.tela_principal.sair.clicked.connect(self.voltarInicio)

        self.tela_cadastro_livro.botao_salvar_livro.clicked.connect(self.cadastrarLivro)
        self.tela_cadastro_livro.buttonVoltar.clicked.connect(self.voltarPrincipal)

        self.tela_acervo.sair.clicked.connect(self.entrar)

    def entrar(self):
        self.QtStack.setCurrentIndex(2)

    def openCriarConta(self):
        self.QtStack.setCurrentIndex(1)

    def voltarInicio(self):
        self.QtStack.setCurrentIndex(0)

    def criarConta(self):
        self.QtStack.setCurrentIndex(0)

    def openCadastrarLivro(self):
        self.QtStack.setCurrentIndex(3)

    def openAcervoLivro(self):
        self.QtStack.setCurrentIndex(4)

    def voltarPrincipal(self):
        self.QtStack.setCurrentIndex(2)

    def cadastrarLivro(self):
        self.QtStack.setCurrentIndex(2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())