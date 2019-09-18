# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Principal(object):
    def setupUi(self, Tela_Principal):
        Tela_Principal.setObjectName("Tela_Principal")
        Tela_Principal.resize(926, 547)
        Tela_Principal.setFixedSize(926, 547)
        self.centralwidget = QtWidgets.QWidget(Tela_Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 80, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.ver_acervo = QtWidgets.QPushButton(self.centralwidget)
        self.ver_acervo.setGeometry(QtCore.QRect(500, 260, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.ver_acervo.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ver_acervo.setIcon(icon)
        self.ver_acervo.setIconSize(QtCore.QSize(25, 25))
        self.ver_acervo.setObjectName("ver_acervo")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(-10, -20, 941, 571))
        self.textBrowser.setObjectName("textBrowser")
        self.cadastrar_novo_livro = QtWidgets.QPushButton(self.centralwidget)
        self.cadastrar_novo_livro.setGeometry(QtCore.QRect(130, 260, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.cadastrar_novo_livro.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/new-file_40454.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cadastrar_novo_livro.setIcon(icon1)
        self.cadastrar_novo_livro.setIconSize(QtCore.QSize(25, 25))
        self.cadastrar_novo_livro.setObjectName("cadastrar_novo_livro")
        self.sair = QtWidgets.QPushButton(self.centralwidget)
        self.sair.setGeometry(QtCore.QRect(700, 90, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.sair.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sair.setIcon(icon2)
        self.sair.setObjectName("sair")
        self.textBrowser.raise_()
        self.label.raise_()
        self.ver_acervo.raise_()
        self.cadastrar_novo_livro.raise_()
        self.sair.raise_()
        Tela_Principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 22))
        self.menubar.setObjectName("menubar")
        Tela_Principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tela_Principal)
        self.statusbar.setObjectName("statusbar")
        Tela_Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Principal)
        QtCore.QMetaObject.connectSlotsByName(Tela_Principal)

    def retranslateUi(self, Tela_Principal):
        _translate = QtCore.QCoreApplication.translate
        Tela_Principal.setWindowTitle(_translate("Tela_Principal", "Início"))
        self.ver_acervo.setText(_translate("Tela_Principal", "VER ACERVO"))
        self.cadastrar_novo_livro.setText(_translate("Tela_Principal", "CADASTAR NOVO LIVRO"))
        self.sair.setText(_translate("Tela_Principal", "SAIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Principal = QtWidgets.QMainWindow()
    ui = Ui_Tela_Principal()
    ui.setupUi(Tela_Principal)
    Tela_Principal.show()
    sys.exit(app.exec_())
