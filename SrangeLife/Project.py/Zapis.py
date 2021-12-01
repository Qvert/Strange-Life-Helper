import sys
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(949, 522)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba("
                                 "47, 129, 133, 255), stop:1 rgba(255, 201, 108, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(121)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Create_paz = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Create_paz.sizePolicy().hasHeightForWidth())
        self.Create_paz.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Create_paz.setFont(font)
        self.Create_paz.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Create_paz.setStyleSheet("padding-top: 20px;\n"
                                      "border-radius: 20px;\n"
                                      "color: white;\n"
                                      "border: 1.5px solid white\n"
                                      ";\n"
                                      "padding: 20px;\n"
                                      "background: rgba(255, 255, 255, 0)\n"
                                      "\n"
                                      "\n"
                                      "")
        self.Create_paz.setObjectName("Create_paz")
        self.horizontalLayout_2.addWidget(self.Create_paz)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.Writeing = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Writeing.sizePolicy().hasHeightForWidth())
        self.Writeing.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Writeing.setFont(font)
        self.Writeing.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Writeing.setStyleSheet("border-radius: 20px;\n"
                                    "color: white;\n"
                                    "border: 1.5px solid white;\n"
                                    "background: rgba(250, 250, 250, 0)\n"
                                    "\n"
                                    "")
        self.Writeing.setObjectName("Writeing")
        self.horizontalLayout_2.addWidget(self.Writeing)
        self.Delete = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Delete.sizePolicy().hasHeightForWidth())
        self.Delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Delete.setFont(font)
        self.Delete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Delete.setStyleSheet("border-radius: 20px;\n"
                                  "color: white;\n"
                                  "border: 1.5px solid white;\n"
                                  "background: rgba(250, 250, 250, 0)\n"
                                  "\n"
                                  "")
        self.Delete.setObjectName("Delete")
        self.horizontalLayout_2.addWidget(self.Delete)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 1, 1, 2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(57, -1, -1, -1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.write_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.write_2.setFont(font)
        self.write_2.setStyleSheet("color: white;\n"
                                   "background: none\n"
                                   "")
        self.write_2.setObjectName("write_2")
        self.verticalLayout_2.addWidget(self.write_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, 20, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.text_heading = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.text_heading.setFont(font)
        self.text_heading.setStyleSheet("color: white;\n"
                                        "\n"
                                        "border: none;\n"
                                        "background: rgba(250, 250, 250, 0)\n"
                                        "")
        self.text_heading.setText("")
        self.text_heading.setObjectName("text_heading")
        self.gridLayout.addWidget(self.text_heading, 1, 0, 1, 1)
        self.heading = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.heading.setFont(font)
        self.heading.setStyleSheet("color: white;\n"
                                   "background: none\n"
                                   "")
        self.heading.setObjectName("heading")
        self.gridLayout.addWidget(self.heading, 0, 0, 1, 1)
        self.write = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.write.setFont(font)
        self.write.setStyleSheet("color: white;\n"
                                 "background: none\n"
                                 "")
        self.write.setObjectName("write")
        self.gridLayout.addWidget(self.write, 3, 0, 1, 1)
        self.write_text = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        self.write_text.setFont(font)
        self.write_text.setStyleSheet("color: white;\n"
                                      "\n"
                                      "border: none;\n"
                                      "background: rgba(250, 250, 250, 0)\n"
                                      "")
        self.write_text.setObjectName("write_text")
        self.gridLayout.addWidget(self.write_text, 4, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Display = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(14)
        font.setItalic(False)
        self.Display.setFont(font)
        self.Display.setStyleSheet("color: white;\n"
                                   "border: none;\n"
                                   "background: rgba(250, 250, 250, 0)\n"
                                   "")
        self.Display.setObjectName("Display")
        self.verticalLayout.addWidget(self.Display)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 0, 4, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 949, 21))
        self.menubar.setStyleSheet("background: none")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menuFile)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.Russian = QtWidgets.QAction(MainWindow)
        self.Russian.setObjectName("Russian")
        self.English = QtWidgets.QAction(MainWindow)
        self.English.setObjectName("English")
        self.menu.addAction(self.Russian)
        self.menu.addAction(self.English)
        self.menuFile.addAction(self.menu.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Записная книжка"))
        self.Create_paz.setText(_translate("MainWindow", "Создать запись"))
        self.Writeing.setText(_translate("MainWindow", "Записать"))
        self.Delete.setText(_translate("MainWindow", "Удалить записи"))
        self.write_2.setText(_translate("MainWindow", "Записки:"))
        self.heading.setText(_translate("MainWindow", "Заголовок:"))
        self.write.setText(_translate("MainWindow", "Запись:"))
        self.write_text.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                           "type=\"text/css\">\n "
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Segoe Print\'; "
                                           "font-size:14pt; font-weight:400; font-style:normal;\">\n "
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                           "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                           "text-indent:0px;\"><br /></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu.setTitle(_translate("MainWindow", "Язык"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.Russian.setText(_translate("MainWindow", "Русский"))
        self.English.setText(_translate("MainWindow", "Английский"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.setupUi(self)
        self.heading.setText('')
        self.write.setText('')

        self.Writeing.clicked.connect(self.doit)
        self.Delete.clicked.connect(self.delete)
        self.Create_paz.clicked.connect(self.make)
        self.Russian.triggered.connect(lambda: self.rus())
        self.English.triggered.connect(lambda: self.en())
        self.text_heading.setReadOnly(True)
        self.write_text.setReadOnly(True)

        result = open('Notebook_base.txt', mode='r', encoding='utf8').read()
        if result == 'True':
            self.heading.setText('Заголовок:')
            self.write.setText('Запись:')
            self.write_2.setText('Записки:')
            self.Create_paz.setText('Создать запись')
            self.Writeing.setText('Записать')
            self.Delete.setText('Удалить записи')

        if result == 'False':
            self.write_2.setText('Notes:')
            self.Create_paz.setText('Create notes')
            self.Writeing.setText('Write')
            self.Delete.setText('Delete notes')
        """
            Открываем базу данных и выводим её
        """

        con = sqlite3.connect("database/films_db.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT auth_name, title FROM record""").fetchall()
        for i in result:
            self.Display.addItem(i[1] + "\n" + i[0])
        con.close()

    def doit(self):
        """
            Добавляем записи в базу и сразу выводим её содержимое
        :return:
        """

        self.Display.clear()
        con = sqlite3.connect("database/films_db.sqlite")
        cur = con.cursor()
        cur.execute(
            """INSERT INTO record (auth_name, title)
                       VALUES (?, ?);""",
            (self.write_text.toPlainText(), self.text_heading.text()),
        )
        con.commit()
        result = cur.execute("""SELECT auth_name, title FROM record""").fetchall()
        for i in result:
            self.Display.addItem(i[1] + "\n" + i[0])
        con.close()
        self.write_text.setPlainText("")
        self.text_heading.setText("")
        self.heading.setText('')
        self.write.setText('')
        self.text_heading.setReadOnly(True)
        self.write_text.setReadOnly(True)

    def delete(self):
        """
            Очищаем базу данных

        :return:
        """

        con = sqlite3.connect("database/films_db.sqlite")
        cur = con.cursor()
        cur.execute("""DELETE from record""").fetchall()
        con.commit()
        con.close()
        self.Display.clear()

    def make(self):
        """
            Показываем строки для заполнения записки
        :return:
        """
        self.text_heading.setReadOnly(False)
        self.write_text.setReadOnly(False)
        result = open('Notebook_base.txt', mode='r', encoding='utf8').read()
        if result == 'True':
            self.heading.setText('Заголовок:')
            self.write.setText('Запись:')
        if result == 'False':
            self.heading.setText('Heading:')
            self.write.setText('Note:')


    def rus(self):
        """
            Меняем язык русский
        :return:
        """
        result = open('Notebook_base.txt', mode='r').read()

        if result == 'False':
            self.write_2.setText('Записки:')
            self.Create_paz.setText('Создать запись')
            self.Writeing.setText('Записать')
            self.Delete.setText('Удалить записи')
        result = 'True'
        with open('Notebook_base.txt', mode='w', encoding='utf8') as file:
            file.write(result)

    def en(self):
        """
            Меняем язык на английский
        :return:
        """
        result = open('Notebook_base.txt', mode='r').read()

        if result == 'True':
            self.write_2.setText('Notes:')
            self.Create_paz.setText('Create notes')
            self.Writeing.setText('Write')
            self.Delete.setText('Delete notes')
        result = 'False'
        with open('Notebook_base.txt', mode='w', encoding='utf8') as file:
            file.write(result)

    def initUi(self):
        # Выводит иконку приложения
        self.setWindowIcon(QIcon("Icons/zapis.png"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
