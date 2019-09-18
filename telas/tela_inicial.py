# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_inicial.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget


class Ui_Tela_Inicio(object):
    def setupUi(self, Tela_Inicio):
        Tela_Inicio.setObjectName("Tela_Inicio")
        Tela_Inicio.resize(800, 600)
        Tela_Inicio.setFixedSize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        Tela_Inicio.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Tela_Inicio)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(230, 80, 351, 381))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 30, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 255, 56, 19))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.senha_login = QtWidgets.QLineEdit(self.centralwidget)
        self.senha_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha_login.setMaxLength(15)
        self.senha_login.setGeometry(QtCore.QRect(300, 280, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.senha_login.setFont(font)
        self.senha_login.setObjectName("senha_login")
        self.e_mail_login = QtWidgets.QLineEdit(self.centralwidget)
        self.e_mail_login.setGeometry(QtCore.QRect(300, 198, 211, 30))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.e_mail_login.setFont(font)
        self.e_mail_login.setObjectName("e_mail_login")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 173, 56, 19))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.botao_criar_conta = QtWidgets.QPushButton(self.centralwidget)
        self.botao_criar_conta.setGeometry(QtCore.QRect(350, 380, 112, 30))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.botao_criar_conta.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/uer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_criar_conta.setIcon(icon)
        self.botao_criar_conta.setIconSize(QtCore.QSize(16, 16))
        self.botao_criar_conta.setObjectName("botao_criar_conta")
        self.botao_entrar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_entrar.setGeometry(QtCore.QRect(360, 320, 91, 30))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.botao_entrar.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/Login_37128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_entrar.setIcon(icon1)
        self.botao_entrar.setObjectName("botao_entrar")
        Tela_Inicio.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Inicio)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Tela_Inicio.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tela_Inicio)
        self.statusbar.setObjectName("statusbar")
        Tela_Inicio.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Inicio)
        QtCore.QMetaObject.connectSlotsByName(Tela_Inicio)

    def retranslateUi(self, Tela_Inicio):
        _translate = QtCore.QCoreApplication.translate
        Tela_Inicio.setWindowTitle(_translate("Tela_Inicio", "Login"))
        self.label_3.setText(_translate("Tela_Inicio", "LOGIN"))
        self.label_2.setText(_translate("Tela_Inicio", "Senha:"))
        self.label.setText(_translate("Tela_Inicio", "E-mail:"))
        self.botao_criar_conta.setText(_translate("Tela_Inicio", "CRIAR CONTA"))
        self.botao_entrar.setText(_translate("Tela_Inicio", "ENTRAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Inicio = QtWidgets.QMainWindow()
    ui = Ui_Tela_Inicio()
    ui.setupUi(Tela_Inicio)
    Tela_Inicio.show()
    sys.exit(app.exec_())
