# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_acervo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Acervo(object):
    def setupUi(self, Tela_Acervo):
        Tela_Acervo.setObjectName("Tela_Acervo")
        Tela_Acervo.resize(926, 547)
        self.centralwidget = QtWidgets.QWidget(Tela_Acervo)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 80, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(-10, -20, 941, 571))
        self.textBrowser.setObjectName("textBrowser")
        self.sair = QtWidgets.QPushButton(self.centralwidget)
        self.sair.setGeometry(QtCore.QRect(690, 90, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.sair.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon)
        self.sair.setObjectName("sair")
        self.campoBusca = QtWidgets.QLineEdit(self.centralwidget)
        self.campoBusca.setGeometry(QtCore.QRect(160, 90, 401, 28))
        self.campoBusca.setObjectName("campoBusca")
        self.botaoBusca = QtWidgets.QPushButton(self.centralwidget)
        self.botaoBusca.setGeometry(QtCore.QRect(580, 90, 92, 28))
        self.botaoBusca.setObjectName("botaoBusca")
        self.tabelaLivros = QtWidgets.QTableView(self.centralwidget)
        self.tabelaLivros.setGeometry(QtCore.QRect(160, 150, 621, 291))
        self.tabelaLivros.setObjectName("tabelaLivros")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser.raise_()
        self.label.raise_()
        self.sair.raise_()
        self.campoBusca.raise_()
        self.botaoBusca.raise_()
        self.tabelaLivros.raise_()
        self.label_2.raise_()
        Tela_Acervo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Acervo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 22))
        self.menubar.setObjectName("menubar")
        Tela_Acervo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tela_Acervo)
        self.statusbar.setObjectName("statusbar")
        Tela_Acervo.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Acervo)
        QtCore.QMetaObject.connectSlotsByName(Tela_Acervo)

    def retranslateUi(self, Tela_Acervo):
        _translate = QtCore.QCoreApplication.translate
        Tela_Acervo.setWindowTitle(_translate("Tela_Acervo", "MainWindow"))
        self.sair.setText(_translate("Tela_Acervo", "SAIR"))
        self.botaoBusca.setText(_translate("Tela_Acervo", "Buscar"))
        self.label_2.setText(_translate("Tela_Acervo", "Acervo"))
