import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from currency_converter import CurrencyConverter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(426, 769)
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setStyleSheet("background-color: #22222e;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 270))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 270))
        self.frame.setStyleSheet("background-color: #fb5b5d;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Heading = QtWidgets.QLabel(self.frame)
        self.Heading.setGeometry(QtCore.QRect(70, 10, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Heading.setFont(font)
        self.Heading.setStyleSheet("color: white;")
        self.Heading.setObjectName("Heading")
        self.pic = QtWidgets.QLabel(self.frame)
        self.pic.setGeometry(QtCore.QRect(100, 70, 191, 171))
        self.pic.setSizeIncrement(QtCore.QSize(0, 12))
        self.pic.setText("")
        self.pic.setPixmap(
            QtGui.QPixmap("Icons/exchanging.png"))
        self.pic.setObjectName("pic")
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.from_currency = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.from_currency.setFont(font)
        self.from_currency.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.from_currency.setStyleSheet("color: #7d7b7a;\n"
                                         "background-color: #22222e;\n"
                                         "selection-color: #7d7b7a;\n"
                                         "selection-background-color: #22222e;\n"
                                         "border: 2px solid #f66867;\n"
                                         "border-radius: 25px;\n"
                                         "padding:15px")
        self.from_currency.setObjectName("from_currency")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.verticalLayout.addWidget(self.from_currency)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.isval_ = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.isval_.setFont(font)
        self.isval_.setStyleSheet("background-color: #22222e;\n"
                                  "color: #7d7b7a;\n"
                                  "border: 2px solid #f66867;\n"
                                  "border-radius: 25px;\n"
                                  "padding:15px")
        self.isval_.setText("")
        self.isval_.setObjectName("isval_")
        self.verticalLayout.addWidget(self.isval_)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.to_currency = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.to_currency.setFont(font)
        self.to_currency.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.to_currency.setStyleSheet("background-color: #22222e;\n"
                                       "color: #7d7b7a;\n"
                                       "border: 2px solid #f66867;\n"
                                       "border-radius: 25px;\n"
                                       "padding:15px")
        self.to_currency.setObjectName("to_currency")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.verticalLayout_2.addWidget(self.to_currency)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.at_the_val = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.at_the_val.setFont(font)
        self.at_the_val.setStyleSheet("background-color: #22222e;\n"
                                      "color: #7d7b7a;\n"
                                      "border: 2px solid #f66867;\n"
                                      "border-radius: 25px;\n"
                                      "padding:15px")
        self.at_the_val.setText("")
        self.at_the_val.setObjectName("at_the_val")
        self.verticalLayout_2.addWidget(self.at_the_val)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.convert_but = QtWidgets.QPushButton(self.centralwidget)
        self.convert_but.setMinimumSize(QtCore.QSize(380, 60))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.convert_but.setFont(font)
        self.convert_but.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.convert_but.setStyleSheet("QPushButton {\n"
                                       "    color: white;\n"
                                       "    background-color: #fb5b5d;\n"
                                       "    border-radius: 30;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: #fa4244\n"
                                       "}")
        self.convert_but.setObjectName("convert_but")
        self.verticalLayout_3.addWidget(self.convert_but)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Heading.setText(_translate("MainWindow", "КОНВЕРТЕР ВАЛЮТ"))
        self.from_currency.setItemText(0, _translate("MainWindow", "Из валюты:"))
        self.from_currency.setItemText(1, _translate("MainWindow", "USD - Доллар США"))
        self.from_currency.setItemText(2, _translate("MainWindow", "RUB - Российский рубль"))
        self.from_currency.setItemText(3, _translate("MainWindow", "FRF - Францурский франк"))
        self.from_currency.setItemText(4, _translate("MainWindow", "BEF - Бельгийский франк"))
        self.from_currency.setItemText(5, _translate("MainWindow", "AUD - Австралийский доллар"))
        self.from_currency.setItemText(6, _translate("MainWindow", "CAD - Канадский доллар"))
        self.from_currency.setItemText(7, _translate("MainWindow", "SGD - Сингапурский доллар"))
        self.from_currency.setItemText(8, _translate("MainWindow", "ATS - Австрийский шиллинг"))
        self.from_currency.setItemText(9, _translate("MainWindow", "EUR - Евро"))
        self.from_currency.setItemText(10, _translate("MainWindow", "NOK - Норвежская крона"))
        self.from_currency.setItemText(11, _translate("MainWindow", "DKK - Датская крона"))
        self.from_currency.setItemText(12, _translate("MainWindow", "FIM - Финская крона "))
        self.from_currency.setItemText(13, _translate("MainWindow", "SEK - Шведская крона"))
        self.from_currency.setItemText(14, _translate("MainWindow", "DEM - Немецкая марка"))
        self.from_currency.setItemText(15, _translate("MainWindow", "PTE - Португальское эскудо"))
        self.from_currency.setItemText(16, _translate("MainWindow", "JPY - Японская валюта"))
        self.from_currency.setItemText(17, _translate("MainWindow", "GBP - Английский фунт"))
        self.from_currency.setItemText(18, _translate("MainWindow", "CHF - Швейцарский франк"))
        self.to_currency.setItemText(0, _translate("MainWindow", "В валюту:"))
        self.to_currency.setItemText(1, _translate("MainWindow", "USD - Доллар США"))
        self.to_currency.setItemText(2, _translate("MainWindow", "RUB - Российский рубль"))
        self.to_currency.setItemText(3, _translate("MainWindow", "FRF - Францурский франк"))
        self.to_currency.setItemText(4, _translate("MainWindow", "BEF - Бельгийский франк"))
        self.to_currency.setItemText(5, _translate("MainWindow", "AUD - Австралийский доллар"))
        self.to_currency.setItemText(6, _translate("MainWindow", "CAD - Канадский доллар"))
        self.to_currency.setItemText(7, _translate("MainWindow", "SGD - Сингапурский доллар"))
        self.to_currency.setItemText(8, _translate("MainWindow", "ATS - Австрийский шиллинг"))
        self.to_currency.setItemText(9, _translate("MainWindow", "EUR - Евро"))
        self.to_currency.setItemText(10, _translate("MainWindow", "NOK - Норвежская крона"))
        self.to_currency.setItemText(11, _translate("MainWindow", "DKK - Датская крона"))
        self.to_currency.setItemText(12, _translate("MainWindow", "FIM - Финская крона "))
        self.to_currency.setItemText(13, _translate("MainWindow", "SEK - Шведская крона"))
        self.to_currency.setItemText(14, _translate("MainWindow", "DEM - Немецкая марка"))
        self.to_currency.setItemText(15, _translate("MainWindow", "PTE - Португальское эскудо"))
        self.to_currency.setItemText(16, _translate("MainWindow", "JPY - Японская валюта"))
        self.to_currency.setItemText(17, _translate("MainWindow", "GBP - Английский фунт"))
        self.to_currency.setItemText(18, _translate("MainWindow", "CHF - Швейцарский франк"))
        self.convert_but.setText(_translate("MainWindow", "КОНВЕРТИРУЙ"))


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):

        """
            Создаём иконку приложения и добавляем картинку в QLabel.
            Также задаём текст LineEdit и подключаем кнопку.
            :return:
        """

        self.setWindowTitle("Конвертер валют")
        self.setWindowIcon(QIcon("Icons/exchanging.png"))

        self.ui.isval_.setPlaceholderText("У меня есть:")

        self.ui.at_the_val.setText("Я получу:")
        self.ui.convert_but.clicked.connect(self.converter)

    def converter(self):

        """
            Сам код выполнения.
        """

        c = CurrencyConverter()
        # Входная валюта
        input_currency = self.ui.from_currency.currentText().split()
        # Выходная валюта
        output_currency = self.ui.to_currency.currentText().split()
        # Кол-во денег в валюте
        input_amount = int(self.ui.isval_.text())
        output_amount = round(
            c.convert(input_amount, "%s" % (input_currency[0]), "%s" % (output_currency[0])),
            2,
        )
        # Выводим значение
        self.ui.at_the_val.setText(str(output_amount))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
