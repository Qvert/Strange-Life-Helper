import sys
import os
import time

from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen, QProgressBar
from PyQt5.QtGui import QIcon, QPixmap, QMovie, QPainter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 509)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #1a1a1c;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(126)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dancing Script")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dancing Script")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dancing Script")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(28, 28, 30, -1)
        self.horizontalLayout.setSpacing(56)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calc = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calc.sizePolicy().hasHeightForWidth())
        self.calc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Balsamiq Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.calc.setFont(font)
        self.calc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calc.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calc.setStyleSheet("border-radius: 25px;\n"
                                "padding: 20px 20px 20px 20px;\n"
                                "background-color: qlineargradient(spread:pad, x1:0.449182, y1:0.568, x2:0, y2:1, "
                                "stop:0 rgba(85, 182, 201, 255), stop:1 rgba(174, 174, 174, 255));\n "
                                "color: white\n"
                                "")
        self.calc.setIconSize(QtCore.QSize(44, 41))
        self.calc.setObjectName("calc")
        self.horizontalLayout.addWidget(self.calc)
        self.conver = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conver.sizePolicy().hasHeightForWidth())
        self.conver.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Balsamiq Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.conver.setFont(font)
        self.conver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.conver.setStyleSheet("padding: 20px 20px 20px 20px;\n"
                                  "color: white;\n"
                                  "background-color: qlineargradient(spread:pad, x1:0.574, y1:0.397545, x2:0, y2:1, "
                                  "stop:0 rgba(201, 63, 35, 255), stop:1 rgba(183, 183, 183, 255));\n "
                                  "border-radius: 25px\n"
                                  "")
        self.conver.setObjectName("conver")
        self.horizontalLayout.addWidget(self.conver)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.plan = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plan.sizePolicy().hasHeightForWidth())
        self.plan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Balsamiq Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.plan.setFont(font)
        self.plan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plan.setStyleSheet("padding: 20px 20px 20px 20px;\n"
                                "color: white;\n"
                                "background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0.108136, y2:0.904, "
                                "stop:0 rgba(230, 180, 22, 255), stop:1 rgba(154, 31, 200, 255));\n "
                                "border-radius: 25px\n"
                                "")
        self.plan.setObjectName("plan")
        self.horizontalLayout.addWidget(self.plan)
        self.zapis = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zapis.sizePolicy().hasHeightForWidth())
        self.zapis.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Balsamiq Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.zapis.setFont(font)
        self.zapis.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zapis.setStyleSheet("padding: 20px 20px 20px 20px;\n"
                                 "color: white;\n"
                                 "background-color: qlineargradient(spread:pad, x1:0.568182, y1:0.33, x2:0, y2:1, "
                                 "stop:0 rgba(174, 165, 43, 255), stop:1 rgba(47, 189, 147, 255));\n "
                                 "border-radius: 25px\n"
                                 "")
        self.zapis.setObjectName("zapis")
        self.horizontalLayout.addWidget(self.zapis)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, -1, 27, -1)
        self.horizontalLayout_3.setSpacing(60)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dancing Script")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.trans = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trans.sizePolicy().hasHeightForWidth())
        self.trans.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Balsamiq Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.trans.setFont(font)
        self.trans.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.trans.setStyleSheet("padding: 20px 20px 20px 20px;\n"
                                 "color: white;\n"
                                 "background-color: qlineargradient(spread:pad, x1:0.631, y1:0.346591, x2:0, y2:1, "
                                 "stop:0 rgba(55, 112, 209, 255), stop:1 rgba(173, 173, 173, 255));\n "
                                 "border-radius: 25px\n"
                                 "")
        self.trans.setObjectName("trans")
        self.horizontalLayout_3.addWidget(self.trans)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dancing Script")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.wither = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wither.sizePolicy().hasHeightForWidth())
        self.wither.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Balsamiq Sans")
        font.setPointSize(14)
        font.setItalic(True)
        self.wither.setFont(font)
        self.wither.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wither.setStyleSheet("padding: 20px 20px 20px 20px;\n"
                                  "color: white;\n"
                                  "background-color: qlineargradient(spread:pad, x1:0.545, y1:0.324, x2:0, y2:1, "
                                  "stop:0 rgba(48, 60, 216, 255), "
                                  "stop:1 rgba(155, 155, 155, 255));\n "
                                  "border-radius: 25px\n"
                                  "")
        self.wither.setObjectName("wither")
        self.horizontalLayout_3.addWidget(self.wither)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setStyleSheet("padding: 50px")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menuBar.setStyleSheet("color: white")
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.menuFile.setFont(font)
        self.menuFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuFile.setStyleSheet("color: white")
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menuFile)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.russian = QtWidgets.QAction(MainWindow)
        self.russian.setObjectName("russian")
        self.english = QtWidgets.QAction(MainWindow)
        self.english.setObjectName("english")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu.addAction(self.russian)
        self.menu.addAction(self.english)
        self.menuFile.addAction(self.menu.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Strange Life"))
        self.label.setText(_translate("MainWindow", "Strange Life"))
        self.calc.setText(_translate("MainWindow", "Калькулятор"))
        self.conver.setText(_translate("MainWindow", "Конвертер валют"))
        self.plan.setText(_translate("MainWindow", "Планировщик"))
        self.zapis.setText(_translate("MainWindow", "Записная книжка"))
        self.trans.setText(_translate("MainWindow", "Переводчик"))
        self.wither.setText(_translate("MainWindow", "Прогноз погоды"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu.setTitle(_translate("MainWindow", "Изменить язык"))
        self.russian.setText(_translate("MainWindow", "Русский"))
        self.english.setText(_translate("MainWindow", "Английский"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


"""
    Класс загрузочного экрана
"""


class MovieSplashScreen(QSplashScreen):
    size = QSize(600, 600)

    def __init__(self, path_to_gif: str):
        self.movie = QMovie(path_to_gif)
        self.movie.jumpToFrame(0)
        pixmap = QPixmap(self.size)
        QSplashScreen.__init__(self, pixmap)
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.movie.start()

    def hideEvent(self, a0: QtGui.QHideEvent) -> None:
        self.movie.stop()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        pixmap = pixmap.scaled(self.size)
        painter.drawPixmap(0, 0, pixmap)


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.setupUi(self)
        # Подключаем кнопки
        self.calc.clicked.connect(self.calcu)
        self.conver.clicked.connect(self.conv)
        self.plan.clicked.connect(self.plani)
        self.zapis.clicked.connect(self.zap)
        self.trans.clicked.connect(self.translation)
        self.wither.clicked.connect(self.forecast)
        self.russian.triggered.connect(self.rus)
        self.english.triggered.connect(self.en)
        self.actionExit.triggered.connect(self.exit)


        # Проверяем язык
        result = open('main_true_false.txt', mode='r', encoding='utf8').read()
        if result == 'True':
            self.calc.setText("Калькулятор")
            self.conver.setText("Конвертер валют")
            self.plan.setText("Планировщик")
            self.zapis.setText("Записная книжка")
            self.trans.setText("Переводчик")
            self.wither.setText("Прогноз погоды")

        if result == 'False':
            self.calc.setText("Calculator")
            self.conver.setText("Currency converter")
            self.plan.setText("Scheduler")
            self.zapis.setText("Notebook")
            self.trans.setText("Translator")
            self.wither.setText("Weather forecast")

    def calcu(self):
        """
        Открываем калькулятор
        :return:
        """
        os.startfile(os.path.join(os.getcwd(), "calculator.exe"))

    def conv(self):
        # Открываем конвертер
        os.startfile(os.path.join(os.getcwd(), "converter-currency.exe"))

    def plani(self):
        # Открываем планировщик
        os.startfile(os.path.join(os.getcwd(), "planirov.exe"))

    def zap(self):
        # Открываем записную книжку
        os.startfile(os.path.join(os.getcwd(), "Notebook.exe"))

    def translation(self):
        # Открываем переводчик
        os.startfile(os.path.join(os.getcwd(), "Translator.exe"))

    def forecast(self):
        # Открываем прогноз погоды
        os.startfile(os.path.join(os.getcwd(), "Wither forecast.exe"))

    def initUi(self):
        self.setWindowIcon(QIcon("Icons/unnamed.jpg"))

    def exit(self):
        self.close()

    def rus(self):
        """
            Меняем на русский
        :return:
        """
        result = open('main_true_false.txt', mode='r').read()

        if result == 'False':
            self.calc.setText("Калькулятор")
            self.conver.setText("Конвертер валют")
            self.plan.setText("Планировщик")
            self.zapis.setText("Записная книжка")
            self.trans.setText("Переводчик")
            self.wither.setText("Прогноз погоды")
        result = 'True'
        with open('main_true_false.txt', mode='w', encoding='utf8') as file:
            file.write(result)

    def en(self):
        """
            Меняем на английский
        :return:
        """
        result = open('main_true_false.txt', mode='r').read()

        if result == 'True':
            self.calc.setText("Calculator")
            self.conver.setText("Currency converter")
            self.plan.setText("Scheduler")
            self.zapis.setText("Notebook")
            self.trans.setText("Translator")
            self.wither.setText("Weather forecast")
        result = 'False'
        with open('main_true_false.txt', mode='w', encoding='utf8') as file:
            file.write(result)

    def exit(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    progressbar_value = 30
    path_to_gif = 'Gif/2.gif'

    splash = MovieSplashScreen(path_to_gif)
    progressbar = QProgressBar(splash)
    progressbar.setMaximum(progressbar_value)
    progressbar.setTextVisible(False)
    progressbar.setGeometry(0, splash.size.height() - 50,
                            splash.size.width(), 20)
    splash.show()

    for i in range(progressbar_value):
        progressbar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            app.processEvents()

    time.sleep(1)
    ex = MyWidget()
    ex.show()
    splash.finish(ex)
    sys.exit(app.exec_())
