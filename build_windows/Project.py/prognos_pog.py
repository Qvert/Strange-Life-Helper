import sys
from pyowm import OWM
import datetime
import socket
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon


class Wither_design(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 636)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.528136, y1:0, x2:0.54, y2:1, stop:0 rgba(0, 147, 255, "
            "255), stop:1 rgba(218, 218, 218, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(29, 8, -1, 3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.date = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Outfit Light")
        font.setPointSize(14)
        self.date.setFont(font)
        self.date.setStyleSheet("background-color: none;\n"
                                "color: white")
        self.date.setObjectName("date")
        self.horizontalLayout_6.addWidget(self.date)
        self.city = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(14)
        self.city.setFont(font)
        self.city.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                "color: white;\n"
                                "border-bottom: 1px solid white;\n"
                                "alternate-background-color: white;")
        self.city.setObjectName("city")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.city.addItem("")
        self.horizontalLayout_6.addWidget(self.city)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(24, 1, 0, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.temp_like_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Outfit")
        font.setPointSize(36)
        self.temp_like_value.setFont(font)
        self.temp_like_value.setStyleSheet("background-color: none;\n"
                                           "color: white")
        self.temp_like_value.setObjectName("temp_like_value")
        self.horizontalLayout_7.addWidget(self.temp_like_value)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(28, 7, 128, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.itfeels_like = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(10)
        self.itfeels_like.setFont(font)
        self.itfeels_like.setStyleSheet("background-color: none;\n"
                                        "color: white")
        self.itfeels_like.setObjectName("itfeels_like")
        self.horizontalLayout_9.addWidget(self.itfeels_like)
        self.temp_po_osh = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(10)
        self.temp_po_osh.setFont(font)
        self.temp_po_osh.setStyleSheet("background-color: none;\n"
                                       "color: white")
        self.temp_po_osh.setText("")
        self.temp_po_osh.setObjectName("temp_po_osh")
        self.horizontalLayout_9.addWidget(self.temp_po_osh)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, -1, 30, 28)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_8.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pogoda_yz = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pogoda_yz.sizePolicy().hasHeightForWidth())
        self.pogoda_yz.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.pogoda_yz.setFont(font)
        self.pogoda_yz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pogoda_yz.setStyleSheet("padding: 20px 20px 20px 20px;\n"
                                     "color: white;\n"
                                     "background-color: rgba(0, 0, 0, 0);\n"
                                     "border: 1.5px solid white;\n"
                                     "\n"
                                     "\n"
                                     "")
        self.pogoda_yz.setObjectName("pogoda_yz")
        self.horizontalLayout_5.addWidget(self.pogoda_yz)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: white")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(14, -1, 0, -1)
        self.formLayout.setHorizontalSpacing(18)
        self.formLayout.setObjectName("formLayout")
        self.pixmap_wind = QtWidgets.QLabel(self.widget)
        self.pixmap_wind.setText("")
        self.pixmap_wind.setPixmap(QtGui.QPixmap("Pixmap/zapis.png"))
        self.pixmap_wind.setObjectName("pixmap_wind")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pixmap_wind)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ind_text = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Outfit Light")
        font.setPointSize(14)
        self.ind_text.setFont(font)
        self.ind_text.setObjectName("ind_text")
        self.horizontalLayout.addWidget(self.ind_text)
        self.wind_value = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(16)
        self.wind_value.setFont(font)
        self.wind_value.setStyleSheet("background-color: none;\n"
                                      "")
        self.wind_value.setText("")
        self.wind_value.setObjectName("wind_value")
        self.horizontalLayout.addWidget(self.wind_value)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(13, -1, -1, -1)
        self.formLayout_2.setHorizontalSpacing(19)
        self.formLayout_2.setObjectName("formLayout_2")
        self.dav_pix = QtWidgets.QLabel(self.widget)
        self.dav_pix.setText("")
        self.dav_pix.setPixmap(QtGui.QPixmap("Pixmap/dav.jpg"))
        self.dav_pix.setObjectName("dav_pix")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dav_pix)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dav_text = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Outfit Light")
        font.setPointSize(14)
        self.dav_text.setFont(font)
        self.dav_text.setObjectName("dav_text")
        self.horizontalLayout_2.addWidget(self.dav_text)
        self.dav_value = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(16)
        self.dav_value.setFont(font)
        self.dav_value.setStyleSheet("background-color: none;\n"
                                     "")
        self.dav_value.setText("")
        self.dav_value.setObjectName("dav_value")
        self.horizontalLayout_2.addWidget(self.dav_value)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.formLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(14, -1, -1, -1)
        self.formLayout_3.setHorizontalSpacing(18)
        self.formLayout_3.setObjectName("formLayout_3")
        self.vlag_pixmap = QtWidgets.QLabel(self.widget)
        self.vlag_pixmap.setText("")
        self.vlag_pixmap.setPixmap(QtGui.QPixmap("Pixmap/vlag.png"))
        self.vlag_pixmap.setObjectName("vlag_pixmap")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.vlag_pixmap)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.vlag_text = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Outfit Light")
        font.setPointSize(14)
        self.vlag_text.setFont(font)
        self.vlag_text.setObjectName("vlag_text")
        self.horizontalLayout_3.addWidget(self.vlag_text)
        self.vlag_value = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Outfit")
        font.setPointSize(16)
        self.vlag_value.setFont(font)
        self.vlag_value.setStyleSheet("background-color: none;\n"
                                      "")
        self.vlag_value.setText("")
        self.vlag_value.setObjectName("vlag_value")
        self.horizontalLayout_3.addWidget(self.vlag_value)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.formLayout_3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setContentsMargins(14, 0, -1, 20)
        self.formLayout_4.setHorizontalSpacing(18)
        self.formLayout_4.setObjectName("formLayout_4")
        self.temp_pixmap = QtWidgets.QLabel(self.widget)
        self.temp_pixmap.setText("")
        self.temp_pixmap.setPixmap(QtGui.QPixmap("Pixmap/temp.jpg"))
        self.temp_pixmap.setObjectName("temp_pixmap")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.temp_pixmap)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(27)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.temp_text = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Outfit Light")
        font.setPointSize(14)
        self.temp_text.setFont(font)
        self.temp_text.setObjectName("temp_text")
        self.horizontalLayout_4.addWidget(self.temp_text)
        self.temp_value = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Outfit")
        font.setPointSize(16)
        self.temp_value.setFont(font)
        self.temp_value.setStyleSheet("background-color: none;\n"
                                      "")
        self.temp_value.setText("")
        self.temp_value.setObjectName("temp_value")
        self.horizontalLayout_4.addWidget(self.temp_value)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.formLayout_4)
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 418, 21))
        self.menuBar.setStyleSheet("color: black;\n"
                                   "background-color: none")
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menuFile)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.ex = QtWidgets.QAction(MainWindow)
        self.ex.setObjectName("ex")
        self.russian = QtWidgets.QAction(MainWindow)
        self.russian.setObjectName("russian")
        self.english = QtWidgets.QAction(MainWindow)
        self.english.setObjectName("english")
        self.menu.addAction(self.russian)
        self.menu.addAction(self.english)
        self.menuFile.addAction(self.menu.menuAction())
        self.menuFile.addAction(self.ex)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Прогноз погоды"))
        self.date.setText(_translate("MainWindow", "Ср.9 Января"))
        self.city.setItemText(0, _translate("MainWindow", "Выберите город"))
        self.city.setItemText(1, _translate("MainWindow", "Санкт-Петербург"))
        self.city.setItemText(2, _translate("MainWindow", "Новосибирск"))
        self.city.setItemText(3, _translate("MainWindow", "Екатеринбург"))
        self.city.setItemText(4, _translate("MainWindow", "Нижний Новгород"))
        self.city.setItemText(5, _translate("MainWindow", "Самара"))
        self.city.setItemText(6, _translate("MainWindow", "Омск"))
        self.city.setItemText(7, _translate("MainWindow", "Казань"))
        self.city.setItemText(8, _translate("MainWindow", "Челябинск"))
        self.city.setItemText(9, _translate("MainWindow", "Ростов-на-Дону"))
        self.city.setItemText(10, _translate("MainWindow", "Чита"))
        self.city.setItemText(11, _translate("MainWindow", "Москва"))
        self.city.setItemText(12, _translate("MainWindow", "Засопка"))
        self.city.setItemText(13, _translate("MainWindow", "Уфа"))
        self.city.setItemText(14, _translate("MainWindow", "Красноярск"))
        self.city.setItemText(15, _translate("MainWindow", "Волгоград"))
        self.city.setItemText(16, _translate("MainWindow", "Пермь"))
        self.city.setItemText(17, _translate("MainWindow", "Воронеж"))
        self.city.setItemText(18, _translate("MainWindow", "Саратов"))
        self.city.setItemText(19, _translate("MainWindow", "Краснодар"))
        self.city.setItemText(20, _translate("MainWindow", "Тольятти"))
        self.city.setItemText(21, _translate("MainWindow", "Ижевск"))
        self.city.setItemText(22, _translate("MainWindow", "Ульяновск"))
        self.city.setItemText(23, _translate("MainWindow", "Барнаул"))
        self.city.setItemText(24, _translate("MainWindow", "Владивосток"))
        self.city.setItemText(25, _translate("MainWindow", "Ярославль"))
        self.city.setItemText(26, _translate("MainWindow", "Иркутск"))
        self.city.setItemText(27, _translate("MainWindow", "Тюмень"))
        self.city.setItemText(28, _translate("MainWindow", "Махачкала"))
        self.city.setItemText(29, _translate("MainWindow", "Хабаровск"))
        self.city.setItemText(30, _translate("MainWindow", "Новокузнецк"))
        self.city.setItemText(31, _translate("MainWindow", "Оренбург"))
        self.city.setItemText(32, _translate("MainWindow", "Кемерово"))
        self.city.setItemText(33, _translate("MainWindow", "Рязань"))
        self.city.setItemText(34, _translate("MainWindow", "Томск"))
        self.city.setItemText(35, _translate("MainWindow", "Астрахань"))
        self.city.setItemText(36, _translate("MainWindow", "Калининград"))
        self.city.setItemText(37, _translate("MainWindow", "Улан-Удэ"))
        self.city.setItemText(38, _translate("MainWindow", "Тверь"))
        self.city.setItemText(39, _translate("MainWindow", "Белгород"))
        self.city.setItemText(40, _translate("MainWindow", "Сочи"))
        self.city.setItemText(41, _translate("MainWindow", "Владикавказ"))
        self.city.setItemText(42, _translate("MainWindow", "Саранск"))
        self.city.setItemText(43, _translate("MainWindow", "Тамбов"))
        self.city.setItemText(44, _translate("MainWindow", "Стерлитамак"))
        self.city.setItemText(45, _translate("MainWindow", "Якутск"))
        self.city.setItemText(46, _translate("MainWindow", "Кострома"))
        self.temp_like_value.setText(_translate("MainWindow", "0 ˚C"))
        self.itfeels_like.setText(_translate("MainWindow", "По ощущению:"))
        self.pogoda_yz.setText(_translate("MainWindow", "Узнать погоду"))
        self.ind_text.setText(_translate("MainWindow", "Скорость ветра:"))
        self.dav_text.setText(_translate("MainWindow", "Давление:"))
        self.vlag_text.setText(_translate("MainWindow", "Влажность:"))
        self.temp_text.setText(_translate("MainWindow", "Температура  мин.:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu.setTitle(_translate("MainWindow", "Сменить язык"))
        self.action_2.setText(_translate("MainWindow", "Русский"))
        self.action_3.setText(_translate("MainWindow", "Русский"))
        self.action_4.setText(_translate("MainWindow", "Английский"))
        self.ex.setText(_translate("MainWindow", "Exit"))
        self.russian.setText(_translate("MainWindow", "Русский"))
        self.english.setText(_translate("MainWindow", "Английский"))


def proc(hum):
    if str(hum)[-1] == 0:
        return 'процентов'
    elif str(hum)[-1] == 1:
        return 'процент'
    elif 1 < int(str(hum)[-1]) < 5:
        return 'процента'
    elif int(str(hum)) >= 5:
        return 'процентов'



def temp_prov(temp_cr):
    if int(temp_cr) < 0:
        return str(temp_cr)[1:]
    else:
        return temp_cr


def is_temp(cr_temp):
    if int(cr_temp) < 0:
        return 'минус'
    else:
        return 'плюс'


def prov_week(week, dic):
    for i in dic.keys():
        if week == i:
            return dic[week]


def prov_month(month, dic_m):
    for i in dic_m.keys():
        if month == i:
            return dic_m[month]


# Словарь месяцев
DICT_month = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь',
}
# Словарь дней недели
DICT = {
    1: 'Пн.',
    2: 'Вт.',
    3: 'Ср.',
    4: 'Чт.',
    5: 'Пт.',
    6: 'Сб.',
    7: 'Вс.'
}

DICT_ENG = {
    1: 'Sun.',
    2: 'Mon.',
    3: 'Tues.',
    4: 'Wed.',
    5: 'Thurs.',
    6: 'Fri.',
    7: 'Sat.'
}

DICT_month_ENG = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}


class MyWidget(QMainWindow, Wither_design):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.setupUi(self)
        self.pogoda_yz.clicked.connect(self.wither)
        self.russian.triggered.connect(lambda: self.rus())
        self.english.triggered.connect(lambda: self.en())
        self.ex.triggered.connect(lambda: self.exit())

        # Проверяем какой язык стоит
        result = open('wither_prov.txt', mode='r', encoding='utf8').read()
        if result == 'False':
            self.city.setCurrentText("Select city")
            self.itfeels_like.setText('It feels like:')
            self.pogoda_yz.setText('Find out the weather')
            self.ind_text.setText('Wind speed')
            self.dav_text.setText('Pressure')
            self.vlag_text.setText('Humidity')
            self.temp_text.setText('Temperature min.:')
            now = datetime.datetime.now()
            week = prov_week(now.isoweekday(), DICT_ENG), now.day, prov_month(now.month, DICT_month_ENG)
            self.date.setText(' '.join([str(x) for x in week]))

        if result == 'True':
            self.city.setCurrentText('Выберите город')
            self.itfeels_like.setText('По ощущению:')
            self.pogoda_yz.setText('Узнать погоду')
            self.ind_text.setText('Скорость ветра')
            self.dav_text.setText('Давление')
            self.vlag_text.setText('Влажность')
            self.temp_text.setText('Температура мин.:')
            now = datetime.datetime.now()
            week = prov_week(now.isoweekday(), DICT), now.day, prov_month(now.month, DICT_month)
            self.date.setText(' '.join([str(x) for x in week]))

    def initUi(self):
        self.setWindowIcon(QIcon("Icons/Prog.jpg"))

    def rus(self):
        """
            Меняем язык русский
        :return:
        """
        result = open('wither_prov.txt', mode='r').read()

        if result == 'False':
            self.city.setCurrentText("Выберите город")
            self.itfeels_like.setText('По ощущению:')
            self.pogoda_yz.setText('Узнать погоду')
            self.ind_text.setText('Скорость ветра')
            self.dav_text.setText('Давление')
            self.vlag_text.setText('Влажность')
            self.temp_text.setText('Температура мин.:')
            now = datetime.datetime.now()
            week = prov_week(now.isoweekday(), DICT), now.day, prov_month(now.month, DICT_month)
            self.date.setText(' '.join([str(x) for x in week]))
        result = 'True'
        with open('wither_prov.txt', mode='w', encoding='utf8') as file:
            file.write(result)

    def en(self):
        """
            Меняем язык английский
        :return:
        """
        result = open('wither_prov.txt', mode='r').read()

        if result == 'True':
            self.city.setCurrentText("Select city")
            self.itfeels_like.setText('It feels like:')
            self.pogoda_yz.setText('Find out the weather')
            self.ind_text.setText('Wind speed')
            self.dav_text.setText('Pressure')
            self.vlag_text.setText('Humidity')
            self.temp_text.setText('Temperature min.:')
            now = datetime.datetime.now()
            week = prov_week(now.isoweekday(), DICT_ENG), now.day, prov_month(now.month, DICT_month_ENG)
            self.date.setText(' '.join([str(x) for x in week]))

        result = 'False'
        with open('wither_prov.txt', mode='w', encoding='utf8') as file:
            file.write(result)

    def exit(self):
        # Закрываем приложение
        self.close()

    def wither(self):
        """
            Проверка есть ли интернет
        :return:
        """

        try:
            socket.gethostbyaddr('www.yandex.ru')

            # Узнаём температуру
            owm = OWM("01d2ce5b8b7211e0ef9a0b12f5f9c5b3")
            mgr = owm.weather_manager()

            observation = mgr.weather_at_place(self.city.currentText())
            w = observation.weather

            temperature = w.temperature("celsius")
            wind = w.wind()
            hum = w.humidity
            self.temp_po_osh.setText(f"{temperature['temp_max']}˚C")
            self.temp_like_value.setText(f"{temperature['temp']}˚C")
            self.temp_value.setText(f"{temperature['temp_min']}˚C")
            self.wind_value.setText(f"{wind['speed']} м/c ")
            self.dav_value.setText(f"{wind['deg']} мм/рт/с")
            self.vlag_value.setText(f"{hum}%")
            QApplication.setQuitOnLastWindowClosed(False)



        except socket.gaierror:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Проверьте соединение с интернетом")
            msg.setInformativeText('More information')
            msg.setWindowTitle("Error")
            msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
