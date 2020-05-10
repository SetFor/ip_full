# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ip_full.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from tkinter import *
import ip_address as ip
import socket

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip

def copy_text(self):
    c = Tk()
    c.withdraw()
    c.clipboard_clear()
    c.clipboard_append(self)
    c.update()
    c.destroy()

class Ui_ip_informer(object):
    def setupUi(self, ip_informer):
        ip_informer.setObjectName("ip_informer")
        ip_informer.resize(173, 121)
        self.pushButton = QtWidgets.QPushButton(ip_informer)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ip_informer)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(ip_informer)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(ip_informer)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 60, 121, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(ip_informer)
        self.label.setGeometry(QtCore.QRect(10, 0, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ip_informer)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.label_2.setObjectName("label_2")
        self.toolButton = QtWidgets.QToolButton(ip_informer)
        self.toolButton.setGeometry(QtCore.QRect(140, 19, 25, 22))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(ip_informer)
        self.toolButton_2.setGeometry(QtCore.QRect(140, 59, 25, 22))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton.clicked.connect(self.buttonClicked)
        self.toolButton_2.clicked.connect(self.buttonClicked1)
        self.pushButton.clicked.connect(self.buttonClicked_info)
        self.pushButton_2.clicked.connect(self.save_to_file)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)

        self.retranslateUi(ip_informer)
        QtCore.QMetaObject.connectSlotsByName(ip_informer)
    def buttonClicked(self):
        copy_text(self.lineEdit.text())
    def buttonClicked1(self):
        copy_text(self.lineEdit_2.text())
    def buttonClicked_info(self):
        self.lineEdit.setText(ip.get())
        self.lineEdit_2.setText(get_lan_ip())
    def save_to_file(self):
        if self.lineEdit_2.text()!="":
            my_file = open("ip.txt", "w")
            my_file.write(self.lineEdit.text()+"\n")
            my_file.write(self.lineEdit_2.text()+"\n")
            my_file.close()

    def retranslateUi(self, ip_informer):
        _translate = QtCore.QCoreApplication.translate
        ip_informer.setWindowTitle(_translate("ip_informer", "Узнать IP"))
        ip_informer.setWindowIcon(QIcon('icon.ico'))
        self.pushButton.setText(_translate("ip_informer", "Узнать"))
        self.pushButton_2.setText(_translate("ip_informer", "Сохранить"))
        self.label.setText(_translate("ip_informer", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Внешний IP</span></p></body></html>"))
        self.label_2.setText(_translate("ip_informer", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Локальный IP</span></p></body></html>"))
        self.toolButton.setText(_translate("ip_informer", "К"))
        self.toolButton_2.setText(_translate("ip_informer", "К"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ip_informer = QtWidgets.QDialog()
    ui = Ui_ip_informer()
    ui.setupUi(ip_informer)
    ip_informer.show()
    sys.exit(app.exec_())
