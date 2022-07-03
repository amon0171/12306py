from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
import sys
import time
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
from _12306.main_ui_demo import Ui_MainWindow
from _12306.login_text import Ui_Dialog
from _12306.Login import APITool_Main


class MyThread(threading.Thread):
    def __init__(self, username, password):
        # super(MyThread, self).__init__()
        threading.Thread.__init__(self)
        self.username = username
        self.password = password

    def run(self):
        self.usr = APITool_Main.check_login(self.username, self.password)

    def get_result(self):
        return self.usr


class Main_Windows(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)


class login_pane(QWidget, Ui_Dialog):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.setupUi(self)

    def jump_to_demo1(self):           #  这一块注意，是重点从主界面跳转到Demo1界面，主界面隐藏，如果关闭Demo界面，主界面进程会触发self.form.show()会再次显示主界面
        self.hide()
        form1 = QtWidgets.QDialog()
        ui = Ui_MainWindow()
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        self.form.show()


    def check_login(self):
        UserName = self.lineEdit.text()
        Password = self.lineEdit_2.text()
        # show_MainWindow()
        print(UserName, Password)
        thread_login = MyThread(UserName, Password)
        thread_login.start()
        thread_login.join()
        usr = thread_login.get_result()
        print(usr)
        if usr == 'https://kyfw.12306.cn/otn/resources/login.html':
            self.show_message()
        elif usr == 'https://kyfw.12306.cn/otn/view/index.html':
            self.jump_to_demo1()

    def auto_enable_login(self):
        UserName = self.lineEdit.text()
        Password = self.lineEdit_2.text()
        APITool_Main.UserName = UserName
        APITool_Main.PassWord = Password
        if len(UserName) == 0 or len(Password) == 0:
            self.pushButton.setEnabled(False)
        else:
            self.pushButton.setEnabled(True)


def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)  # 实例化QApplication,作为GUI主程序入口
    MainWindow = QtWidgets.QDialog()  # 创app = QtWidgets.QApplication(sys.argv)建QMainWindow
    ui = Ui_MainWindow()  # 实例UI类
    ui.setupUi(MainWindow)  # 设置窗体UI
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 当窗口创建完成后需要结束主循环


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # 实例化QApplication,作为GUI主程序入口
    MainWindow = QtWidgets.QDialog()  # 创app = QtWidgets.QApplication(sys.argv)建QMainWindow
    login_window = login_pane()
    login_window.show()

    # login_window.pushButton.clicked.connect(show_MainWindow())
    sys.exit(app.exec_())
