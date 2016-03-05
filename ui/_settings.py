# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xml/settings.ui'
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

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName(_fromUtf8("SettingsDialog"))
        SettingsDialog.resize(487, 473)
        self.verticalLayout_2 = QtGui.QVBoxLayout(SettingsDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.my_bugs_title = QtGui.QLineEdit(self.tab)
        self.my_bugs_title.setObjectName(_fromUtf8("my_bugs_title"))
        self.horizontalLayout_2.addWidget(self.my_bugs_title)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.my_bugs_query = QtGui.QPlainTextEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Input Mono"))
        self.my_bugs_query.setFont(font)
        self.my_bugs_query.setObjectName(_fromUtf8("my_bugs_query"))
        self.verticalLayout.addWidget(self.my_bugs_query)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.important_bugs_title = QtGui.QLineEdit(self.tab_2)
        self.important_bugs_title.setObjectName(_fromUtf8("important_bugs_title"))
        self.horizontalLayout_3.addWidget(self.important_bugs_title)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.important_bugs_query = QtGui.QPlainTextEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Input Mono"))
        self.important_bugs_query.setFont(font)
        self.important_bugs_query.setObjectName(_fromUtf8("important_bugs_query"))
        self.verticalLayout_3.addWidget(self.important_bugs_query)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.common_bugs_title = QtGui.QLineEdit(self.tab_3)
        self.common_bugs_title.setObjectName(_fromUtf8("common_bugs_title"))
        self.horizontalLayout_4.addWidget(self.common_bugs_title)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.common_bugs_query = QtGui.QPlainTextEdit(self.tab_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Input Mono"))
        self.common_bugs_query.setFont(font)
        self.common_bugs_query.setObjectName(_fromUtf8("common_bugs_query"))
        self.verticalLayout_4.addWidget(self.common_bugs_query)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(SettingsDialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(SettingsDialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(SettingsDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), SettingsDialog.close)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), SettingsDialog.on_save)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings", None))
        self.label.setText(_translate("SettingsDialog", "Title:", None))
        self.my_bugs_title.setText(_translate("SettingsDialog", "My Bugs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SettingsDialog", "\"My Bugs\" Query", None))
        self.label_2.setText(_translate("SettingsDialog", "Title:", None))
        self.important_bugs_title.setText(_translate("SettingsDialog", "Important Issues", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SettingsDialog", "\"L3 Bugs\" Query", None))
        self.label_3.setText(_translate("SettingsDialog", "Title:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("SettingsDialog", "\"Team Bugs\" Query", None))
        self.pushButton.setText(_translate("SettingsDialog", "Save", None))
        self.pushButton_2.setText(_translate("SettingsDialog", "Cancel", None))

