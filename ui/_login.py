# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xml/login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName(_fromUtf8("LoginDialog"))
        LoginDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        LoginDialog.resize(332, 192)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginDialog.sizePolicy().hasHeightForWidth())
        LoginDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(LoginDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(LoginDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.uid_field = QtGui.QLineEdit(LoginDialog)
        self.uid_field.setEchoMode(QtGui.QLineEdit.Normal)
        self.uid_field.setObjectName(_fromUtf8("uid_field"))
        self.gridLayout.addWidget(self.uid_field, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(LoginDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.password_field = QtGui.QLineEdit(LoginDialog)
        self.password_field.setEchoMode(QtGui.QLineEdit.Password)
        self.password_field.setObjectName(_fromUtf8("password_field"))
        self.gridLayout.addWidget(self.password_field, 1, 1, 1, 1)
        self.private_computer_check = QtGui.QCheckBox(LoginDialog)
        self.private_computer_check.setObjectName(_fromUtf8("private_computer_check"))
        self.gridLayout.addWidget(self.private_computer_check, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.login_btn = QtGui.QPushButton(LoginDialog)
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        self.horizontalLayout.addWidget(self.login_btn)
        self.exit_btn = QtGui.QPushButton(LoginDialog)
        self.exit_btn.setObjectName(_fromUtf8("exit_btn"))
        self.horizontalLayout.addWidget(self.exit_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(LoginDialog)
        QtCore.QObject.connect(self.login_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), LoginDialog.on_login)
        QtCore.QObject.connect(self.exit_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), LoginDialog.on_exit)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Login To Mozilla", None))
        self.label.setText(_translate("LoginDialog", "Login:", None))
        self.label_2.setText(_translate("LoginDialog", "Password:", None))
        self.private_computer_check.setText(_translate("LoginDialog", "Private computer", None))
        self.login_btn.setText(_translate("LoginDialog", "Login", None))
        self.exit_btn.setText(_translate("LoginDialog", "Close", None))

