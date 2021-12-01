import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets


class Design_calc(object):
    def setupUi(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mult = QtWidgets.QPushButton(self.centralwidget)
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fact = QtWidgets.QPushButton(self.centralwidget)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.btn_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_pow = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()

        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eq = QtWidgets.QPushButton(self.centralwidget)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 552)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0454545 rgba(12, 89, 115, "
            "255), stop:0.982955 rgba(39, 55, 64, 255))"
        )
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border: none;\n" "color: white\n" "")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_9.addWidget(self.lineEdit)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, 2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pow.sizePolicy().hasHeightForWidth())
        self.btn_pow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_pow.setFont(font)
        self.btn_pow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pow.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: #09eded;\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn_pow.setObjectName("btn_pow")
        self.gridLayout_3.addWidget(self.btn_pow, 0, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sqrt.sizePolicy().hasHeightForWidth())
        self.btn_sqrt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_sqrt.setFont(font)
        self.btn_sqrt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_sqrt.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: #09eded;\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.gridLayout_3.addWidget(self.btn_sqrt, 0, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fact.sizePolicy().hasHeightForWidth())
        self.btn_fact.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_fact.setFont(font)
        self.btn_fact.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_fact.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: #09eded;\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn_fact.setObjectName("btn_fact")
        self.gridLayout_3.addWidget(self.btn_fact, 0, 2, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn7.setFont(font)
        self.btn7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn7.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: white;\n"
            "\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn7.setObjectName("btn7")
        self.gridLayout_3.addWidget(self.btn7, 1, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn8.setFont(font)
        self.btn8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn8.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: white;\n"
            "\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn8.setObjectName("btn8")
        self.gridLayout_3.addWidget(self.btn8, 1, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn9.setFont(font)
        self.btn9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn9.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: white;\n"
            "\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn9.setObjectName("btn9")
        self.gridLayout_3.addWidget(self.btn9, 1, 2, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mult.sizePolicy().hasHeightForWidth())
        self.btn_mult.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_mult.setFont(font)
        self.btn_mult.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_mult.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: #09eded;\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn_mult.setObjectName("btn_mult")
        self.gridLayout_3.addWidget(self.btn_mult, 1, 3, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn4.setFont(font)
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn4.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: white;\n"
            "\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn4.setObjectName("btn4")
        self.gridLayout_3.addWidget(self.btn4, 2, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn5.setFont(font)
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn5.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: white;\n"
            "\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn5.setObjectName("btn5")
        self.gridLayout_3.addWidget(self.btn5, 2, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn6.setFont(font)
        self.btn6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn6.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: white;\n"
            "\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn6.setObjectName("btn6")
        self.gridLayout_3.addWidget(self.btn6, 2, 2, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_minus.setFont(font)
        self.btn_minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minus.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: #09eded;\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn_minus.setObjectName("btn_minus")
        self.gridLayout_3.addWidget(self.btn_minus, 2, 3, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_div.setFont(font)
        self.btn_div.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_div.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: #09eded;\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn_div.setObjectName("btn_div")
        self.gridLayout_3.addWidget(self.btn_div, 0, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn1.setFont(font)
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn1.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: white;\n"
            "\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn1.setObjectName("btn1")
        self.gridLayout_2.addWidget(self.btn1, 0, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn2.setFont(font)
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn2.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: white;\n"
            "\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn2.setObjectName("btn2")
        self.gridLayout_2.addWidget(self.btn2, 0, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn3.setFont(font)
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn3.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: white;\n"
            "\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn3.setObjectName("btn3")
        self.gridLayout_2.addWidget(self.btn3, 0, 2, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_plus.setFont(font)
        self.btn_plus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_plus.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: #09eded;\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout_2.addWidget(self.btn_plus, 0, 3, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn0.setFont(font)
        self.btn0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn0.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: white;\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn0.setObjectName("btn0")
        self.gridLayout_2.addWidget(self.btn0, 1, 0, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_dot.setFont(font)
        self.btn_dot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_dot.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: white;\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout_2.addWidget(self.btn_dot, 1, 1, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_clear.setFont(font)
        self.btn_clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: #09eded;\n"
            "background-color: #03b3ff00\n"
            "\n"
            ""
        )
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout_2.addWidget(self.btn_clear, 1, 2, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_eq.sizePolicy().hasHeightForWidth())
        self.btn_eq.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_eq.setFont(font)
        self.btn_eq.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_eq.setStyleSheet(
            "border: 0.5px solid rgba(255, 255, 255, 20);\n"
            "color: white;\n"
            "background-color: #0ff\n"
            "\n"
            ""
        )
        self.btn_eq.setObjectName("btn_eq")
        self.gridLayout_2.addWidget(self.btn_eq, 1, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.btn_pow.setText(_translate("MainWindow", "^"))
        self.btn_sqrt.setText(_translate("MainWindow", "√"))
        self.btn_fact.setText(_translate("MainWindow", "!"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_eq.setText(_translate("MainWindow", "="))


class Calculator(QMainWindow, Design_calc):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()
        self.num = ""
        self.second = ""
        self.op = 0
        self.btn1.clicked.connect(self.run)
        self.btn2.clicked.connect(self.run1)
        self.btn3.clicked.connect(self.run2)
        self.btn4.clicked.connect(self.run3)
        self.btn5.clicked.connect(self.run4)
        self.btn6.clicked.connect(self.run5)
        self.btn7.clicked.connect(self.run6)
        self.btn8.clicked.connect(self.run7)
        self.btn9.clicked.connect(self.run8)
        self.btn0.clicked.connect(self.run9)
        self.btn_eq.clicked.connect(self.suma)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_plus.clicked.connect(self.sum)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_mult.clicked.connect(self.mult)
        self.btn_div.clicked.connect(self.div)
        self.btn_dot.clicked.connect(self.dot)
        self.btn_pow.clicked.connect(self.pow)
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_fact.clicked.connect(self.fact)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.lineEdit.setReadOnly(True)

    def initUi(self):
        self.setWindowIcon(QIcon("Icons/calc.png"))

    """
    Выводим иконку приложения на окошке
    """



    def fact(self):
        self.op = math.factorial(int(self.num))
        self.lineEdit.setText(str(self.op))
        self.num = str(self.op)

    def sqrt(self):
        if int(self.num) < 0:
            self.lineEdit.setText("ERROR")
            self.num = ""
        else:
            self.op = int(self.num) ** 0.5
            self.lineEdit.setText(str(self.op))
            self.num = str(self.op)

    def pow(self):
        self.op = int(self.num) ** 2
        self.lineEdit.setText(str(self.op))
        self.num = str(self.op)

    def dot(self):
        self.num += "."
        self.lineEdit.setText(self.num)

    def div(self):
        self.num += "/"
        self.lineEdit.setText(self.num)

    def mult(self):
        self.num += "*"
        self.lineEdit.setText(self.num)

    def minus(self):
        self.num += "-"
        self.lineEdit.setText(self.num)

    def clear(self):
        self.num = ""
        self.lineEdit.setText(self.num)

    def sum(self):
        self.num += "+"
        self.lineEdit.setText(self.num)

    def suma(self):
        self.second = eval(self.num)
        self.lineEdit.setText(str(self.second))
        self.num = str(eval(self.num))

    def run(self):
        self.num += "1"
        self.lineEdit.setText(self.num)

    def run1(self):
        self.num += "2"
        self.lineEdit.setText(self.num)

    def run2(self):
        self.num += "3"
        self.lineEdit.setText(self.num)

    def run3(self):
        self.num += "4"
        self.lineEdit.setText(self.num)

    def run4(self):
        self.num += "5"
        self.lineEdit.setText(self.num)

    def run5(self):
        self.num += "6"
        self.lineEdit.setText(self.num)

    def run6(self):
        self.num += "7"
        self.lineEdit.setText(self.num)

    def run7(self):
        self.num += "8"
        self.lineEdit.setText(self.num)

    def run8(self):
        self.num += "9"
        self.lineEdit.setText(self.num)

    def run9(self):
        self.num += "0"
        self.lineEdit.setText(self.num)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())
