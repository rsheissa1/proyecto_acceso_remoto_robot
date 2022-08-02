# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(490, 653)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.mot1Spin = QSpinBox(self.groupBox)
        self.mot1Spin.setObjectName(u"mot1Spin")
        self.mot1Spin.setMaximum(180)

        self.gridLayout.addWidget(self.mot1Spin, 1, 1, 1, 1)

        self.delay1Spin = QSpinBox(self.groupBox)
        self.delay1Spin.setObjectName(u"delay1Spin")
        self.delay1Spin.setMinimum(1)
        self.delay1Spin.setMaximum(10)

        self.gridLayout.addWidget(self.delay1Spin, 1, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_8.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.mot2Spin = QSpinBox(self.groupBox_2)
        self.mot2Spin.setObjectName(u"mot2Spin")
        self.mot2Spin.setMaximum(180)

        self.gridLayout_2.addWidget(self.mot2Spin, 1, 1, 1, 1)

        self.delay2Spin = QSpinBox(self.groupBox_2)
        self.delay2Spin.setObjectName(u"delay2Spin")
        self.delay2Spin.setMinimum(1)
        self.delay2Spin.setMaximum(10)

        self.gridLayout_2.addWidget(self.delay2Spin, 1, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_8.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_10, 0, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_12, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.mot3Spin = QSpinBox(self.groupBox_3)
        self.mot3Spin.setObjectName(u"mot3Spin")
        self.mot3Spin.setMaximum(180)

        self.gridLayout_3.addWidget(self.mot3Spin, 1, 1, 1, 1)

        self.delay3Spin = QSpinBox(self.groupBox_3)
        self.delay3Spin.setObjectName(u"delay3Spin")
        self.delay3Spin.setMinimum(1)
        self.delay3Spin.setMaximum(10)

        self.gridLayout_3.addWidget(self.delay3Spin, 1, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_3)


        self.verticalLayout_8.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_13, 0, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_14, 0, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)

        self.mot4Spin = QSpinBox(self.groupBox_4)
        self.mot4Spin.setObjectName(u"mot4Spin")
        self.mot4Spin.setMaximum(180)

        self.gridLayout_4.addWidget(self.mot4Spin, 1, 1, 1, 1)

        self.delay4Spin = QSpinBox(self.groupBox_4)
        self.delay4Spin.setObjectName(u"delay4Spin")
        self.delay4Spin.setMinimum(1)
        self.delay4Spin.setMaximum(10)

        self.gridLayout_4.addWidget(self.delay4Spin, 1, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)


        self.verticalLayout_8.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_15, 0, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_16, 0, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 1, 0, 1, 1)

        self.mot5Spin = QSpinBox(self.groupBox_5)
        self.mot5Spin.setObjectName(u"mot5Spin")
        self.mot5Spin.setMaximum(180)

        self.gridLayout_5.addWidget(self.mot5Spin, 1, 1, 1, 1)

        self.delay5Spin = QSpinBox(self.groupBox_5)
        self.delay5Spin.setObjectName(u"delay5Spin")
        self.delay5Spin.setMinimum(1)
        self.delay5Spin.setMaximum(10)

        self.gridLayout_5.addWidget(self.delay5Spin, 1, 2, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_5)


        self.verticalLayout_8.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_17, 0, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_18, 0, 2, 1, 1)

        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 1, 0, 1, 1)

        self.mot6Spin = QSpinBox(self.groupBox_6)
        self.mot6Spin.setObjectName(u"mot6Spin")
        self.mot6Spin.setMaximum(180)

        self.gridLayout_6.addWidget(self.mot6Spin, 1, 1, 1, 1)

        self.delay6Spin = QSpinBox(self.groupBox_6)
        self.delay6Spin.setObjectName(u"delay6Spin")
        self.delay6Spin.setMinimum(1)
        self.delay6Spin.setMaximum(10)

        self.gridLayout_6.addWidget(self.delay6Spin, 1, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_6)


        self.verticalLayout_8.addWidget(self.groupBox_6)


        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 218, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.enviarButton = QPushButton(self.centralwidget)
        self.enviarButton.setObjectName(u"enviarButton")

        self.verticalLayout.addWidget(self.enviarButton)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.borrarButton = QPushButton(self.centralwidget)
        self.borrarButton.setObjectName(u"borrarButton")

        self.verticalLayout.addWidget(self.borrarButton)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.cerrarButton = QPushButton(self.centralwidget)
        self.cerrarButton.setObjectName(u"cerrarButton")

        self.verticalLayout.addWidget(self.cerrarButton)

        self.verticalSpacer_3 = QSpacerItem(20, 108, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.mot1Spin, self.delay1Spin)
        QWidget.setTabOrder(self.delay1Spin, self.mot2Spin)
        QWidget.setTabOrder(self.mot2Spin, self.delay2Spin)
        QWidget.setTabOrder(self.delay2Spin, self.mot3Spin)
        QWidget.setTabOrder(self.mot3Spin, self.delay3Spin)
        QWidget.setTabOrder(self.delay3Spin, self.mot4Spin)
        QWidget.setTabOrder(self.mot4Spin, self.delay4Spin)
        QWidget.setTabOrder(self.delay4Spin, self.mot5Spin)
        QWidget.setTabOrder(self.mot5Spin, self.delay5Spin)
        QWidget.setTabOrder(self.delay5Spin, self.mot6Spin)
        QWidget.setTabOrder(self.mot6Spin, self.delay6Spin)
        QWidget.setTabOrder(self.delay6Spin, self.enviarButton)
        QWidget.setTabOrder(self.enviarButton, self.borrarButton)
        QWidget.setTabOrder(self.borrarButton, self.cerrarButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Garra de Halc\u00f3n", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Movimiento", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Retraso", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Motor 1", None))
        self.mot1Spin.setSuffix(QCoreApplication.translate("MainWindow", u" Grados", None))
        self.delay1Spin.setSuffix(QCoreApplication.translate("MainWindow", u" segundos", None))
        self.groupBox_2.setTitle("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Movimiento", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Retraso", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Motor 2", None))
        self.mot2Spin.setSuffix(QCoreApplication.translate("MainWindow", u" Grados", None))
        self.delay2Spin.setSuffix(QCoreApplication.translate("MainWindow", u" segundos", None))
        self.groupBox_3.setTitle("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Movimiento", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Retraso", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Motor 3", None))
        self.mot3Spin.setSuffix(QCoreApplication.translate("MainWindow", u" Grados", None))
        self.delay3Spin.setSuffix(QCoreApplication.translate("MainWindow", u" segundos", None))
        self.groupBox_4.setTitle("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Movimiento", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Retraso", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Motor 4", None))
        self.mot4Spin.setSuffix(QCoreApplication.translate("MainWindow", u" Grados", None))
        self.delay4Spin.setSuffix(QCoreApplication.translate("MainWindow", u" segundos", None))
        self.groupBox_5.setTitle("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Movimiento", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Retraso", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Motor 5", None))
        self.mot5Spin.setSuffix(QCoreApplication.translate("MainWindow", u" Grados", None))
        self.delay5Spin.setSuffix(QCoreApplication.translate("MainWindow", u" segundos", None))
        self.groupBox_6.setTitle("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Movimiento", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Retraso", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Motor 6", None))
        self.mot6Spin.setSuffix(QCoreApplication.translate("MainWindow", u" Grados", None))
        self.delay6Spin.setSuffix(QCoreApplication.translate("MainWindow", u" segundos", None))
        self.enviarButton.setText(QCoreApplication.translate("MainWindow", u"&Enviar", None))
        self.borrarButton.setText(QCoreApplication.translate("MainWindow", u"&Borrar", None))
        self.cerrarButton.setText(QCoreApplication.translate("MainWindow", u"&Cerrar", None))
    # retranslateUi

