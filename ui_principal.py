# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_PrincipalWindow(object):
    def setupUi(self, PrincipalWindow):
        if not PrincipalWindow.objectName():
            PrincipalWindow.setObjectName(u"PrincipalWindow")
        PrincipalWindow.resize(800, 600)
        self.centralwidget = QWidget(PrincipalWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mostrar_correo = QLabel(self.centralwidget)
        self.mostrar_correo.setObjectName(u"mostrar_correo")
        self.mostrar_correo.setGeometry(QRect(50, 40, 411, 51))
        self.mostrar_correo.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.buscador = QLineEdit(self.centralwidget)
        self.buscador.setObjectName(u"buscador")
        self.buscador.setGeometry(QRect(50, 120, 321, 31))
        self.boton_buscar = QPushButton(self.centralwidget)
        self.boton_buscar.setObjectName(u"boton_buscar")
        self.boton_buscar.setGeometry(QRect(50, 170, 80, 24))
        self.check_id = QCheckBox(self.centralwidget)
        self.check_id.setObjectName(u"check_id")
        self.check_id.setGeometry(QRect(400, 130, 41, 22))
        self.check_name = QCheckBox(self.centralwidget)
        self.check_name.setObjectName(u"check_name")
        self.check_name.setGeometry(QRect(450, 130, 71, 22))
        self.nombre_producto = QLabel(self.centralwidget)
        self.nombre_producto.setObjectName(u"nombre_producto")
        self.nombre_producto.setGeometry(QRect(110, 250, 451, 71))
        self.nombre_producto.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.cantidad_producto = QLabel(self.centralwidget)
        self.cantidad_producto.setObjectName(u"cantidad_producto")
        self.cantidad_producto.setGeometry(QRect(110, 370, 451, 71))
        self.cantidad_producto.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.boton_cerrar = QPushButton(self.centralwidget)
        self.boton_cerrar.setObjectName(u"boton_cerrar")
        self.boton_cerrar.setGeometry(QRect(650, 20, 121, 21))
        PrincipalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PrincipalWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        PrincipalWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PrincipalWindow)
        self.statusbar.setObjectName(u"statusbar")
        PrincipalWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PrincipalWindow)

        QMetaObject.connectSlotsByName(PrincipalWindow)
    # setupUi

    def retranslateUi(self, PrincipalWindow):
        PrincipalWindow.setWindowTitle(QCoreApplication.translate("PrincipalWindow", u"MainWindow", None))
        self.mostrar_correo.setText(QCoreApplication.translate("PrincipalWindow", u"Bienvenido: ", None))
        self.buscador.setPlaceholderText(QCoreApplication.translate("PrincipalWindow", u"Ingresa el ID del producto", None))
        self.boton_buscar.setText(QCoreApplication.translate("PrincipalWindow", u"Buscar", None))
        self.check_id.setText(QCoreApplication.translate("PrincipalWindow", u"ID", None))
        self.check_name.setText(QCoreApplication.translate("PrincipalWindow", u"Nombre", None))
        self.nombre_producto.setText("")
        self.cantidad_producto.setText("")
        self.boton_cerrar.setText(QCoreApplication.translate("PrincipalWindow", u"Cerrar sesi\u00f3n", None))
    # retranslateUi
