# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"QLabel {\n"
"	font: 700 italic 28pt \"Sitka Banner\";\n"
"	color:rgb(255,255,255)\n"
"	\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.boton_prueba = QPushButton(self.centralwidget)
        self.boton_prueba.setObjectName(u"boton_prueba")
        self.boton_prueba.setGeometry(QRect(280, 280, 211, 51))
        self.boton_prueba.setStyleSheet(u"QPushButton {\n"
"    background-color:#9c120b; /* Color de fondo */\n"
"    border: 4px solid #000000; /* Borde del bot\u00f3n con el color RGB deseado */\n"
" 	color: #000000; /* Color del texto */\n"
"    padding: 10px 20px; /* Espaciado interno */\n"
"	text-align: center;\n"
"	text-decoration: none\n"
"	display: inline-block;\n"
"	font-family: 'Cinzel', serif; /* Fuente g\u00f3tica */\n"
"    font-size: 16px; /* Tama\u00f1o de la fuente */\n"
"	margin: 4px 2px;\n"
"    cursor: pointer; /* Cambia el cursor a una mano al pasar sobre el bot\u00f3n */\n"
"	border-radius: 20px; /* Bordes un poco redondeados\n"
"    box-shadow: 0  4px 8px rgba(0, 0, 0, 0.2); /* Sombra de fondo */\n"
"    transition: background-color 0.3s; /* Transici\u00f3n suave al pasar el cursor */\n"
"}\n"
"\n"
"/* Oscurecer el bot\u00f3n al pasar el cursor */\n"
"QPushButton:hover {\n"
"    background-color: #1a1a1a; /* Color de fondo m\u00e1s oscuro */\n"
"}\n"
"")
        self.input_email = QLineEdit(self.centralwidget)
        self.input_email.setObjectName(u"input_email")
        self.input_email.setGeometry(QRect(260, 140, 261, 24))
        self.texto_salida = QLabel(self.centralwidget)
        self.texto_salida.setObjectName(u"texto_salida")
        self.texto_salida.setGeometry(QRect(170, 470, 451, 51))
        self.texto_salida.setStyleSheet(u"")
        self.input_pass = QLineEdit(self.centralwidget)
        self.input_pass.setObjectName(u"input_pass")
        self.input_pass.setGeometry(QRect(260, 200, 261, 24))
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 50, 241, 61))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.boton_prueba.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.input_email.setText("")
        self.input_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresa tu correo", None))
        self.texto_salida.setText(QCoreApplication.translate("MainWindow", u"Hola ", None))
        self.input_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingresa tu contrase\u00f1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Inicio de Sesi\u00f3n", None))
    # retranslateUi

