from _alert import Ui_Dialog, _translate
from basewindow import BaseDialogMixIn
from PyQt4 import QtGui


class BugAlert(Ui_Dialog, BaseDialogMixIn):
    '''
    Alert window.
    '''
    message = None
    title = None

    def set_title(self, title):
        '''
        Set a title of the alert

        :param title:
        :return:
        '''
        self.title = title

    def set_message(self, message):
        '''
        Set a message on the alert window.

        :param message:
        :return:
        '''
        self.message = message

    def on_alert(self):
        '''
        Handler on alert.

        :return:
        '''
        self.hide()

    def retranslateUi(self, Dialog):
        '''
        Set messages

        :param Dialog:
        :return:
        '''
        Ui_Dialog.retranslateUi(self, Dialog)
        Dialog.setWindowTitle(_translate("Dialog", self.title, None))
        self.label.setText(_translate("Dialog", self.message, None))
