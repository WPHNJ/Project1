import sys

import sqlite3

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QLabel, QDialogButtonBox, QVBoxLayout, \
    QWidget, QMessageBox

SCREEN_SIZE = [400, 400]

name = ""
surname = ""
fict_money = 0
save = 0
file = 0
kolvo = 0
li = []


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 450)
        self.w = ""

        self.setWindowTitle("Взвешиватель")
        self.setGeometry(450, 300, *SCREEN_SIZE)
        self.pixmap = QPixmap('vesi.jpg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(800, 450)
        self.image.setPixmap(self.pixmap)

        uic.loadUi('project.ui', self)

        self.btn_exit.clicked.connect(self.button_exit_clicked)
        self.btn_spravka.clicked.connect(self.button_spravka_clicked)
        self.btn_start.clicked.connect(self.button_start_clicked)

    def button_exit_clicked(self):
        dlg = Dialog1(self)
        if dlg.exec():
            pass
        else:
            pass

    def button_spravka_clicked(self):
        self.close()
        self.w = SpravkaWindow()
        self.w.show()

    def button_start_clicked(self):
        self.close()
        self.w = StartWindow()
        self.w.show()


class Dialog1(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(400, 81)

        self.setWindowTitle("Выход?")

        uic.loadUi('project_dial_exit.ui', self)

        self.btn_return.clicked.connect(self.returner)
        self.btn_close.clicked.connect(self.closer)

    def returner(self):
        self.close()

    def closer(self):
        app.quit()


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 450)
        self.w = ""
        self.text1 = ""
        self.text2 = ""
        self.text3 = ""
        self.one_result = ""
        self.flag = 1

        self.setWindowTitle("Везвешиватель")
        self.setGeometry(450, 300, *SCREEN_SIZE)
        self.pixmap = QPixmap('vesi.jpg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(800, 450)
        self.image.setPixmap(self.pixmap)

        uic.loadUi('project_enter.ui', self)

        self.btn_return.clicked.connect(self.returner)
        self.btn_reg.clicked.connect(self.reg)
        self.btn_enter.clicked.connect(self.enter)

    def returner(self):
        self.close()
        self.w = MainWindow()
        self.w.show()

    def reg(self):
        self.close()
        self.w = RegWindow()
        self.w.show()

    def check(self):
        self.text1 = self.lineEdit.text()
        self.text2 = self.lineEdit2.text()
        self.text3 = self.lineEdit3.text()
        if self.text1.isdigit() is True or len(self.text1) == 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите имя символами алфавита",
            )
        elif self.text2.isdigit() is True or len(self.text2) == 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите фамилию символами алфавита",
            )
        elif len(self.text3) == 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите пароль",
            )

        con = sqlite3.connect("pols.db")

        cur = con.cursor()
        string = "SELECT * FROM users WHERE fname='" + self.text1 + "' and lname='" + self.text2 + "' and pass='" + \
                 self.text3 + "';"
        cur.execute(string)
        self.one_result = cur.fetchone()
        if self.one_result is None and self.flag != 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                'Данного пользователя не существует',
            )
        if self.flag == 0:
            return False
        return True

    def enter(self):
        if self.check() is True:
            string = "D:\pythonProject1\БД" + f'\{self.text1}{self.text2}.db'
            print(string)
            conn = sqlite3.connect(string)
            print(1)

            cur = conn.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS users(
                       save INT PRIMARY KEY,
                       left TEXT,
                       zn TEXT,
                       right TEXT);
                    """)
            conn.commit()

            global name
            name = self.text1
            global surname
            surname = self.text2

            self.close()
            self.w = SettingsWindow()
            self.w.show()
        self.flag = 1


class RegWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 450)
        self.w = ""
        self.text1 = ""
        self.text2 = ""
        self.text3 = ""
        self.text4 = ""
        self.one_result = ""
        self.flag = 1
        self.flag_1 = 0

        self.setWindowTitle("Везвешиватель")
        self.setGeometry(450, 300, *SCREEN_SIZE)
        self.pixmap = QPixmap('vesi.jpg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(800, 450)
        self.image.setPixmap(self.pixmap)

        uic.loadUi('project_reg.ui', self)

        self.btn_return.clicked.connect(self.returner)
        self.btn_ready.clicked.connect(self.ready)

    def returner(self):
        self.close()
        self.w = MainWindow()
        self.w.show()

    def check(self):
        self.text1 = self.lineEdit.text()
        self.text2 = self.lineEdit2.text()
        self.text3 = self.lineEdit3.text()
        self.text4 = self.lineEdit4.text()

        li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        for i in li:
            if i in self.text4:
                self.flag_1 = 1

        if self.text1.isdigit() is True or len(self.text1) == 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите имя символами алфавита",
            )
        elif self.text2.isdigit() is True or len(self.text2) == 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите фамилию символами алфавита",
            )
        elif len(self.text4) == 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите пароль",
            )

        elif self.text3[:3] != "муж" and self.text3[:3] != "жен" and self.text3 != "м" and self.text3 != "ж":
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите свой пол",
            )

        elif len(self.text4) < 10:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Пароль слишком короткий. Нужно хотя бы 10 символов",
            )

        elif self.text4.isdigit() is True:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "В пароле должна использоваться хотя бы 1 буква",
            )

        elif self.flag_1 == 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "В пароле должна использоваться хотя бы 1 цифра",
            )

        con = sqlite3.connect("pols.db")

        cur = con.cursor()
        string = "SELECT * FROM users WHERE fname='" + self.text1 + "' and lname='" + self.text2 + "';"
        cur.execute(string)
        self.one_result = cur.fetchone()
        if self.one_result is not None and self.flag != 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                'Данный пользователь уже существует',
            )
        if self.flag == 0:
            return False
        return True

    def ready(self):
        if self.check() is True:
            conn = sqlite3.connect(r'D:\pythonProject1\pols.db')

            cur = conn.cursor()

            result = cur.execute("""SELECT * FROM users
                        WHERE userid > 0""").fetchall()

            max_id = 0

            for i in result:
                if int(i[0]) > max_id:
                    max_id = int(i[0])

            if self.text3[0] == "м":
                data = [
                    (str(max_id + 1), self.text1, self.text2, "male", self.text4),
                ]
            else:
                data = [
                    (str(max_id + 1), self.text1, self.text2, "female", self.text4),
                ]

            cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?)", data)

            conn.commit()

            string = "D:\pythonProject1\БД" + f'\{self.text1}{self.text2}.db'
            print(string)
            conn = sqlite3.connect(string)
            print(1)

            cur = conn.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS users(
                                   save INT PRIMARY KEY,
                                   left TEXT,
                                   zn TEXT,
                                   right TEXT);
                                """)
            conn.commit()

            global name
            name = self.text1
            global surname
            surname = self.text2

            self.close()
            self.w = SettingsWindow()
            self.w.show()
        self.flag = 1


class SpravkaWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 450)
        self.w = ""

        self.setWindowTitle("Везвешиватель")
        self.setGeometry(450, 300, *SCREEN_SIZE)
        self.pixmap = QPixmap('vesi.jpg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(800, 450)
        self.image.setPixmap(self.pixmap)

        uic.loadUi('project_spravka.ui', self)

        self.btn_return.clicked.connect(self.returner)

    def returner(self):
        self.close()
        self.w = MainWindow()
        self.w.show()


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 450)
        self.w = ""

        self.setWindowTitle("Взвешиватель")
        self.setGeometry(450, 300, *SCREEN_SIZE)
        self.pixmap = QPixmap('vesi.jpg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(800, 450)
        self.image.setPixmap(self.pixmap)

        uic.loadUi('project_settings.ui', self)

        self.fict_money = 5
        self.save = 5
        self.file = 5

        self.btn_return.clicked.connect(self.returner)
        self.btn_ready.clicked.connect(self.ready)
        self.btn_acc.clicked.connect(self.acc)

        self.radioButton1.clicked.connect(self.click1)
        self.radioButton2.clicked.connect(self.click1)

        self.radioButton4.clicked.connect(self.click2)
        self.radioButton5.clicked.connect(self.click2)

        self.radioButton6.clicked.connect(self.click3)
        self.radioButton7.clicked.connect(self.click3)

        self.text = ""
        self.flag = 1

    def acc(self):
        self.close()
        self.w = AccWindow()
        self.w.show()

    def returner(self):
        self.close()
        self.w = MainWindow()
        self.w.show()

    def click1(self):
        if self.sender() == self.radioButton1:
            self.fict_money = 1
        if self.sender() == self.radioButton2:
            self.fict_money = 2

    def click2(self):
        if self.sender() == self.radioButton4:
            self.save = 1
        else:
            self.save = 0

    def click3(self):
        if self.sender() == self.radioButton6:
            self.file = 1
        else:
            self.file = 0

    def check(self):
        self.text = self.lineEdit.text()
        if self.text.isdigit() is False:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите натуральное число, не превосходящее 30",
            )
        elif int(self.text) < 2 or int(self.text) > 30:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите натуральное число большее 2 и не превосходящее 30",
            )
        elif self.file > 1:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Выберите записывать-ли результаты в файл",
            )
        elif self.save > 1:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Выберите, сохранять-ли реультаты",
            )
        elif self.fict_money > 3:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                'Выберите вес "Фальшивой" монеты',
            )
        if self.flag == 0:
            return False
        return True

    def ready(self):
        if self.check() is True:
            global fict_money
            fict_money = self.fict_money
            global save
            save = self.save
            global file
            file = self.file
            global kolvo
            kolvo = int(self.text)
            for i in range(kolvo):
                global li
                li.append(i + 1)
            self.close()
            self.w = VesiWindow()
            self.w.show()
        self.flag = 1


class VesiWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 450)
        self.w = ""
        self.flag = 0
        self.flag2 = 0

        self.setWindowTitle("Взвешиватель")
        self.setGeometry(450, 300, *SCREEN_SIZE)
        self.pixmap = QPixmap('vesi.jpg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(800, 450)
        self.image.setPixmap(self.pixmap)
        self.li1 = []

        uic.loadUi('project_game.ui', self)

        self.lineEdit.setEnabled(False)
        self.lineEdit2.setEnabled(False)
        self.lineEdit3.setEnabled(False)

        global li
        self.li = li
        print(self.li, "ui")

        self.text = self.lineEdit_enter.text()
        self.right_start()
        self.label1.setText(self.li2)
        self.left_start()
        self.label2.setText(self.li3)
        self.btn_ready.clicked.connect(self.ready)

    def check1(self):
        if len(li) == 0:
            return False
        return True

    def check(self):
        self.flag = 1
        if self.text != ">" and self.text != "<" and self.text != "=":
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Выберите, какая чаша перевесила",
            )
        elif self.text == "=" and len(self.li) == 2:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Нет фальшивой монеты",
            )

        if self.flag != 0:
            return True
        return False

    def ready(self):
        if save == 1:
            conn = sqlite3.connect(f'D:\pythonProject1\БД\{name}{surname}.db')

            cur = conn.cursor()

            result = cur.execute("""SELECT * FROM users
                                WHERE save > 0""").fetchall()

            max_id = 0

            for i in result:
                if int(i[3]) > max_id:
                    max_id = int(i[3])

            data = [
                (str(self.li3), str(self.lineEdit_enter.text()), str(self.li2), str(max_id + 1)),
            ]

            cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?)", data)

            conn.commit()
        if file == 1:
            f = open("D:/pythonProject1/взвешивания.txt", 'a')
            print(f.write(self.li3 + self.lineEdit_enter.text() + self.li2 + '\n'))
            f.close()

        self.text = self.lineEdit_enter.text()
        if self.check() is True:
            if fict_money == 1:
                if self.text == ">":
                    if len(self.li3.split()) == 1:
                        button = QMessageBox.critical(
                            self,
                            "Найдено",
                            f"Фальшивая монета найдена({self.li3[0]})",
                        )
                        conn = sqlite3.connect(f'D:\pythonProject1\БД\{name}{surname}.db')

                        cur = conn.cursor()

                        result = cur.execute("""SELECT * FROM users WHERE save > 0""").fetchall()

                        for i in result:
                            cur.execute(f"DELETE FROM users WHERE save = {int(i[3])}")

                        conn.commit()
                        self.flag2 = 1
                    else:
                        self.li = self.li3.split()
                elif self.text == "<":
                    if len(self.li2.split()) == 1:
                        button = QMessageBox.critical(
                            self,
                            "Найдено",
                            f"Фальшивая монета найдена({self.li2[0]})",
                        )
                        conn = sqlite3.connect(f'D:\pythonProject1\БД\{name}{surname}.db')

                        cur = conn.cursor()

                        result = cur.execute("""SELECT * FROM users WHERE save > 0""").fetchall()

                        for i in result:
                            cur.execute(f"DELETE FROM users WHERE save = {int(i[3])}")

                        conn.commit()
                        self.flag2 = 1
                    else:
                        self.li = self.li2.split()
                else:
                    if len(self.li) - len(self.li2.split()) - len(self.li3.split()) == 1:
                        button = QMessageBox.critical(
                            self,
                            "Найдено",
                            f"Фальшивая монета найдёна ({self.li[len(self.li2) - 1]})",
                        )
                        conn = sqlite3.connect(f'D:\pythonProject1\БД\{name}{surname}.db')

                        cur = conn.cursor()

                        result = cur.execute("""SELECT * FROM users WHERE save > 0""").fetchall()

                        for i in result:
                            cur.execute(f"DELETE FROM users WHERE save = {int(i[3])}")

                        conn.commit()
                        self.flag2 = 1
                    else:
                        self.li = self.li[len(self.li2.split()):]
                        self.li = self.li[:-len(self.li2.split())]
            if fict_money == 2:
                if self.text == "<":
                    if len(self.li3.split()) == 1:
                        button = QMessageBox.critical(
                            self,
                            "Найдено",
                            f"Фальшивая монета найдена({self.li3})",
                        )
                        conn = sqlite3.connect(f'D:\pythonProject1\БД\{name}{surname}.db')

                        cur = conn.cursor()

                        result = cur.execute("""SELECT * FROM users WHERE save > 0""").fetchall()

                        for i in result:
                            cur.execute(f"DELETE FROM users WHERE save = {int(i[3])}")

                        conn.commit()
                        self.flag2 = 1
                    else:
                        self.li = self.li3.split()
                elif self.text == ">":
                    if len(self.li2.split()) == 1:
                        button = QMessageBox.critical(
                            self,
                            "Найдено",
                            f"Фальшивая монета найдена({self.li2})",
                        )
                        conn = sqlite3.connect(f'D:\pythonProject1\БД\{name}{surname}.db')

                        cur = conn.cursor()

                        result = cur.execute("""SELECT * FROM users WHERE save > 0""").fetchall()

                        for i in result:
                            cur.execute(f"DELETE FROM users WHERE save = {int(i[3])}")

                        conn.commit()
                        self.flag2 = 1
                    else:
                        self.li = self.li2.split()
                else:
                    if len(self.li) - len(self.li2.split()) - len(self.li3.split()) == 1:
                        button = QMessageBox.critical(
                            self,
                            "Найдено",
                            f"Фальшивая монета найдёна ({self.li[len(self.li2) - 1]})",
                        )
                        conn = sqlite3.connect(f'D:\pythonProject1\БД\{name}{surname}.db')

                        cur = conn.cursor()

                        result = cur.execute("""SELECT * FROM users WHERE save > 0""").fetchall()

                        for i in result:
                            cur.execute(f"DELETE FROM users WHERE save = {int(i[3])}")

                        conn.commit()
                        self.flag2 = 1
                    else:
                        self.li = self.li[len(self.li2.split()):]
                        self.li = self.li[:len(self.li2.split())]
            global li
            li = self.li
            if self.flag2 != 1:
                self.right_start()
                self.label1.setText(self.li2)
                self.left_start()
                self.label2.setText(self.li3)
            else:
                self.close()
                self.w = SettingsWindow()
                self.w.show()
        self.flag = 1

    def right_start(self):
        if fict_money == 1 or fict_money == 2:
            r = len(self.li) % 3
            self.li1 = []
            if r == 0:
                print(self.li)
                for i in range(len(self.li) // 3):
                    self.li1.append(str(self.li[i]))
                    self.li2 = " ".join(self.li1)
            elif r == 1:
                for i in range(len(self.li) // 3):
                    self.li1.append(str(self.li[i]))
                    self.li2 = " ".join(self.li1)
            else:
                for i in range(len(self.li) // 3 + 1):
                    self.li1.append(str(self.li[i]))
                    self.li2 = " ".join(self.li1)

    def left_start(self):
        if fict_money == 1 or fict_money == 2:
            r = len(self.li) % 3
            self.li1 = []
            if r == 0:
                for i in range(len(self.li) // 3):
                    self.li1.append(str(self.li[-i - 1]))
                    self.li3 = " ".join(self.li1)
            elif r == 1:
                for i in range(len(self.li) // 3):
                    self.li1.append(str(self.li[-i - 1]))
                    self.li3 = " ".join(self.li1)
            else:
                for i in range(len(self.li) // 3 + 1):
                    self.li1.append(str(self.li[-i - 1]))
                    self.li3 = " ".join(self.li1)


class AccWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800, 450)
        self.w = ""
        self.text1 = ""
        self.text2 = ""
        self.text3 = ""
        self.text4 = ""
        self.one_result = ""
        self.flag = 1
        self.flag_1 = 0
        self.name = name
        self.surname = surname

        self.setWindowTitle("Везвешиватель")
        self.setGeometry(450, 300, *SCREEN_SIZE)
        self.pixmap = QPixmap('vesi.jpg')
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(800, 450)
        self.image.setPixmap(self.pixmap)

        uic.loadUi('project_reg.ui', self)

        self.btn_return.clicked.connect(self.returner)
        self.btn_ready.clicked.connect(self.ready)

    def returner(self):
        self.close()
        self.w = MainWindow()
        self.w.show()

    def check(self):
        self.text1 = self.lineEdit.text()
        self.text2 = self.lineEdit2.text()
        self.text3 = self.lineEdit3.text()
        self.text4 = self.lineEdit4.text()

        li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        for i in li:
            if i in self.text4:
                self.flag_1 = 1

        if self.text1.isdigit() is True or len(self.text1) == 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите имя символами алфавита",
            )
        elif self.text2.isdigit() is True or len(self.text2) == 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите фамилию символами алфавита",
            )
        elif len(self.text4) == 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите пароль",
            )

        elif self.text3[:3] != "муж" and self.text3[:3] != "жен" and self.text3 != "м" and self.text3 != "ж":
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Введите свой пол",
            )

        elif len(self.text4) < 10:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "Пароль слишком короткий. Нужно хотя бы 10 символов",
            )

        elif self.text4.isdigit() is True:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "В пароле должна использоваться хотя бы 1 буква",
            )

        elif self.flag_1 == 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                "В пароле должна использоваться хотя бы 1 цифра",
            )

        con = sqlite3.connect("pols.db")

        cur = con.cursor()
        string = "SELECT * FROM users WHERE fname='" + self.text1 + "' and lname='" + self.text2 + "';"
        cur.execute(string)
        self.one_result = cur.fetchone()
        if self.one_result is not None and self.flag != 0:
            self.flag = 0
            button = QMessageBox.critical(
                self,
                "Ошибка",
                'Данный пользователь уже существует',
            )
        if self.flag == 0:
            return False
        return True

    def ready(self):
        if self.check() is True:
            conn = sqlite3.connect(r'D:\pythonProject1\pols.db')

            cur = conn.cursor()

            result = cur.execute(f"SELECT * FROM users WHERE fname = '{self.name}' and lname = '{self.surname}';").fetchall()

            max_id = 0

            for i in result:
                if int(i[0]) > max_id:
                    max_id = int(i[0])

            if self.text3[0] == "м":
                data = [
                    (str(max_id), self.text1, self.text2, "male", self.text4),
                ]
            else:
                data = [
                    (str(max_id), self.text1, self.text2, "female", self.text4),
                ]
            line = "UPDATE users SET fname = '" + str(data[0][1]) + "', lname = '" \
                   + str(data[0][2])
            print(line)
            line += "', gender = '" + str(data[0][3]) + "', pass = '" + str(data[0][4]) + "' WHERE userid = '" \
                    + str(data[0][0]) + "';"
            print(line)
            cur.execute(line)

            conn.commit()

            string = "D:\pythonProject1\БД" + f'\{self.text1}{self.text2}.db'
            print(string)
            conn = sqlite3.connect(string)
            print(1)

            cur = conn.cursor()

            cur.execute("""CREATE TABLE IF NOT EXISTS users(
                                   save INT PRIMARY KEY,
                                   left TEXT,
                                   zn TEXT,
                                   right TEXT);
                                """)
            conn.commit()

            global name
            name = self.text1
            global surname
            surname = self.text2

            self.close()
            self.w = SettingsWindow()
            self.w.show()
        self.flag = 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())