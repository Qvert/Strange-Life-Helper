import sys
import sqlite3
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(797, 616)
        Form.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.545, y1:0, x2:0, y2:1, stop:0 rgba(226, 144, 29, "
            "255), stop:0.318182 rgba(237, 121, 110, 255), stop:0.704545 rgba(158, 80, 203, 255), stop:1 rgba(57, 77, "
            "255, 255));")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(41, -1, 36, -1)
        self.horizontalLayout_2.setSpacing(132)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.specift_time = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.specift_time.setFont(font)
        self.specift_time.setStyleSheet("background-color: none;\n"
                                        "color: white;")
        self.specift_time.setObjectName("specift_time")
        self.horizontalLayout_2.addWidget(self.specift_time)
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(11)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet("\n"
                                    "background-color:rgba(255,255,255,1);\n"
                                    "")
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_2.addWidget(self.timeEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(56, 3, 46, 4)
        self.formLayout.setHorizontalSpacing(85)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.specify = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.specify.setFont(font)
        self.specify.setStyleSheet("background-color: none;\n"
                                   "color: white;")
        self.specify.setObjectName("specify")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.specify)
        self.calendar = QtWidgets.QCalendarWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.calendar.setFont(font)
        self.calendar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.calendar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calendar.setAutoFillBackground(False)
        self.calendar.setStyleSheet("alternate-background-color:rgb(128,128,128, 0);\n"
                                    "color: white;\n"
                                    "background-color:rgba(255,255,255,0);\n"
                                    "")
        self.calendar.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendar.setNavigationBarVisible(True)
        self.calendar.setDateEditEnabled(True)
        self.calendar.setDateEditAcceptDelay(1500)
        self.calendar.setObjectName("calendar")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.calendar)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(36, 0, 357, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.heading_text = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.heading_text.setFont(font)
        self.heading_text.setStyleSheet("background-color: none;\n"
                                        "color: white;")
        self.heading_text.setObjectName("heading_text")
        self.verticalLayout.addWidget(self.heading_text)
        self.sobitie = QtWidgets.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sobitie.setFont(font)
        self.sobitie.setStyleSheet("background-color:rgba(255,255,255,0);\n"
                                   "border: 1px solid rgba(255,255,255,0.3);;\n"
                                   "color: white")
        self.sobitie.setObjectName("sobitie")
        self.verticalLayout.addWidget(self.sobitie)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 23, -1, -1)
        self.horizontalLayout.setSpacing(565)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Ok = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ok.sizePolicy().hasHeightForWidth())
        self.Ok.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(7)
        self.Ok.setFont(font)
        self.Ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Ok.setStyleSheet("border-radius: 20px;\n"
                              "padding: 15px 0 15px 0;\n"
                              "font: 63 italic 12pt \"Montserrat\";\n"
                              "border-top: 1px solid white;\n"
                              "border-right: 1px solid white;\n"
                              "border-bottom: 1px solid white;\n"
                              "border-left: 1px solid white;\n"
                              "background-color: none;\n"
                              "color: white\n"
                              "\n"
                              "\n"
                              "\n"
                              "")
        self.Ok.setObjectName("Ok")
        self.horizontalLayout.addWidget(self.Ok)
        self.Cancel = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Cancel.sizePolicy().hasHeightForWidth())
        self.Cancel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(7)
        self.Cancel.setFont(font)
        self.Cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Cancel.setStyleSheet("border-radius: 20px;\n"
                                  "padding: 15px 0 15px 0;\n"
                                  "font: 63 italic 12pt \"Montserrat\";\n"
                                  "border-top: 1px solid white;\n"
                                  "border-right: 1px solid white;\n"
                                  "border-bottom: 1px solid white;\n"
                                  "border-left: 1px solid white;\n"
                                  "background-color: none;\n"
                                  "color: white\n"
                                  "\n"
                                  "\n"
                                  "")
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout.addWidget(self.Cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Создание плана"))
        self.specift_time.setText(_translate("Form", "Укажите время события:"))
        self.specify.setText(_translate("Form", "Укажите дату события:"))
        self.heading_text.setText(_translate("Form", "Напишите само событие:"))
        self.Ok.setText(_translate("Form", "Ок"))
        self.Cancel.setText(_translate("Form", "Cancel"))


class Ui_MainWindow(object):
    def __init__(self):
        self.lang_rus = None
        self.lang_eng = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 772)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.545, y1:0, x2:0, y2:1, stop:0 rgba(226, 144, 29, "
            "255), stop:0.318182 rgba(237, 121, 110, 255), stop:0.704545 rgba(158, 80, 203, 255), stop:1 rgba(57, 77, "
            "255, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(17, 41, 18, 24)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(7)
        self.btn_delete.setFont(font)
        self.btn_delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_delete.setStyleSheet("padding: 15px 0 15px 0;\n"
                                      "font: 63 italic 12pt \"Montserrat\";\n"
                                      "border-top: 1px solid white;\n"
                                      "border-left: 1px solid white;\n"
                                      "border-bottom: 1px solid white;\n"
                                      "background-color: none;\n"
                                      "color: white\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "")
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reset.sizePolicy().hasHeightForWidth())
        self.reset.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(7)
        self.reset.setFont(font)
        self.reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset.setStyleSheet("border: 1px solid white;\n"
                                 "font: 63 italic 12pt \"Montserrat\";\n"
                                 "background-color: none;\n"
                                 "color: white\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "")
        self.reset.setObjectName("reset")
        self.horizontalLayout.addWidget(self.reset)
        self.make_plan = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.make_plan.sizePolicy().hasHeightForWidth())
        self.make_plan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(7)
        self.make_plan.setFont(font)
        self.make_plan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.make_plan.setStyleSheet("border-top: 1px solid white;\n"
                                     "font: 63 italic 12pt \"Montserrat\";\n"
                                     "border-right: 1px solid white;\n"
                                     "border-bottom: 1px solid white;\n"
                                     "background-color: none;\n"
                                     "color: white\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "")
        self.make_plan.setObjectName("make_plan")
        self.horizontalLayout.addWidget(self.make_plan)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(18, 0, 22, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border-bottom: 1px solid white;\n"
                                 "background-color: none;\n"
                                 "color:white;\n"
                                 "")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("background-color: none")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(16, 11, 1, 228)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.window_show = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.window_show.sizePolicy().hasHeightForWidth())
        self.window_show.setSizePolicy(sizePolicy)
        self.window_show.setMinimumSize(QtCore.QSize(0, 300))
        self.window_show.setStyleSheet("padding: 0;\n"
                                       "margin: 0;\n"
                                       "color: white;\n"
                                       "background-color:rgba(255,255,255,0);\n"
                                       "font: 63 italic 12pt \"Montserrat\";\n"
                                       "border: none\n"
                                       "")
        self.window_show.setAutoScroll(True)
        self.window_show.setResizeMode(QtWidgets.QListView.Fixed)
        self.window_show.setObjectName("window_show")
        self.verticalLayout_2.addWidget(self.window_show)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 675, 21))
        self.menuBar.setStyleSheet("background-color: none")
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menuFile)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.russian = QtWidgets.QAction(MainWindow)
        self.russian.setObjectName("russian")
        self.englisg = QtWidgets.QAction(MainWindow)
        self.englisg.setObjectName("englisg")
        self.menu.addAction(self.russian)
        self.menu.addAction(self.englisg)
        self.menuFile.addAction(self.menu.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Планировщик"))
        self.btn_delete.setText(_translate("MainWindow", "Удалить"))
        self.reset.setText(_translate("MainWindow", "Обновить"))
        self.make_plan.setText(_translate("MainWindow", "Создать план"))
        self.label.setText(_translate("MainWindow", "Загруженные планы:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu.setTitle(_translate("MainWindow", "Язык"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.russian.setText(_translate("MainWindow", "Русский"))
        self.englisg.setText(_translate("MainWindow", "Английский"))


class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        """
        Инициализируем класс

        :param parent:
        """

        super(ClssDialog, self).__init__(parent)

        self.pi = Ui_Form()

        self.pi.setupUi(self)
        self.pi.Ok.clicked.connect(self.save)
        self.pi.Cancel.clicked.connect(self.canc)

        """
            Проверяем какой язык показывать
        """

        result = open('planirov_sec.txt', mode='r', encoding='utf8').read()
        if result == '50':
            self.pi.specift_time.setText('Specify the time of the event:')
            self.pi.specify.setText('Specify the date of the event:')
            self.pi.heading_text.setText('Write the event itself:')

        if result == '60':
            self.pi.specift_time.setText('Укажите время события:')
            self.pi.specify.setText('Укажите дату события:')
            self.pi.heading_text.setText('Напишите само событие:')


    def save(self):

        """
            Записываем в переменные данные из календаря, времени, события.

        :return:
        """
        # Дата события
        set_date = self.pi.calendar.selectedDate().getDate()
        if int(set_date[1]) <= 9:
            set_date = (set_date[0], "0" + str(set_date[1]), set_date[2])
        elif int(set_date[2]) <= 9:
            set_date = (set_date[0], set_date[1], "0" + str(set_date[2]))

        # Текст события
        text_edit = self.pi.sobitie.toPlainText()
        # Время события
        time_vr = self.pi.timeEdit.time().toString()

        """Открываем базу данных и записываем в неё значения"""
        con = sqlite3.connect("database/pani.sqlite")
        cur = con.cursor()
        cur.execute(
            """INSERT INTO pani (date, time, plan)
                       VALUES (?, ?, ?);""",
            (f"{set_date[0]} - {set_date[1]} - {set_date[2]}", time_vr, text_edit),
        )
        con.commit()
        con.close()
        self.close()

    def canc(self):

        """
            Закрываем окно по нажатию кнопки
        :return:
        """
        self.close()


class PrimaryWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.ui = Ui_MainWindow()
        self.pi = Ui_Form()
        self.pi.setupUi(self)
        self.ui.setupUi(self)
        self.ui.russian.triggered.connect(self.lang_rus)
        self.ui.englisg.triggered.connect(self.lang_eng)
        self.ui.actionExit.triggered.connect(self.exit)
        self.ui.make_plan.clicked.connect(self.openWindow)
        self.ui.reset.clicked.connect(self.repeat)
        self.ui.btn_delete.clicked.connect(self.delete)

        result = open('planirov_sec.txt', mode='r', encoding='utf8').read()
        if result == '60':
            self.ui.btn_delete.setText('Удалить')
            self.ui.reset.setText('Обновить')
            self.ui.make_plan.setText('Создать план')
            self.ui.label.setText('Загруженные планы:')

        if result == '50':
            self.ui.btn_delete.setText('Delete')
            self.ui.reset.setText('Update')
            self.ui.make_plan.setText('Create a plan')
            self.ui.label.setText('Uploaded Plans:')

        """
            Открываем базу данных и выводим данные из неё
        """
        con = sqlite3.connect("database/pani.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT date, time, plan FROM pani""").fetchall()
        for i in result:
            self.ui.window_show.addItem(i[0] + "\n" + i[1] + "\n" + i[2])
        con.close()

    def initUi(self):

        """
            Подкючаем иконку окна
        :return:
        """

        self.setWindowIcon(QIcon("Icons/plan.png"))

    def lang_rus(self):

        """
            Меняем язык на Русский
        :return:
        """


        result = open('planirov_sec.txt', mode='r').read()

        if result == '50':
            self.ui.btn_delete.setText('Удалить')
            self.ui.reset.setText('Обновить')
            self.ui.make_plan.setText('Создать план')
            self.ui.label.setText('Загруженные планы:')
        result = '60'
        with open('planirov_sec.txt', mode='w', encoding='utf8') as file:
            file.write(result)


    def lang_eng(self):

        """
            Меняем язык на Английский
        :return:
        """
        result = open('planirov_sec.txt', mode='r').read()

        if result == '60':
            self.ui.btn_delete.setText('Delete')
            self.ui.reset.setText('Update')
            self.ui.make_plan.setText('Create a plan')
            self.ui.label.setText('Uploaded Plans:')
        result = '50'
        with open('planirov_sec.txt', mode='w', encoding='utf8') as file:
            file.write(result)



    def exit(self):
        self.close()

    def repeat(self):
        # Очищаем старый вывод базы перед новым
        self.ui.window_show.clear()
        con = sqlite3.connect("database/pani.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT date, time, plan FROM pani""").fetchall()
        for i in result:
            self.ui.window_show.addItem(i[0] + "\n" + i[1] + "\n" + i[2])
        con.close()

    def openWindow(self):

        """
            Открываем новое окно для создания плана
        :return:
        """

        dialog = ClssDialog(self)
        dialog.exec_()



    def delete(self):

        """
            Очищаем базу по нажатию кнопки если этого хочет пользователь
        :return:
        """

        con = sqlite3.connect("database/pani.sqlite")
        cur = con.cursor()
        cur.execute("""DELETE from pani""").fetchall()
        con.commit()
        con.close()
        # Очищаем старый вывод
        self.ui.window_show.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PrimaryWindow()
    window.show()
    sys.exit(app.exec_())
