from PyQt4 import QtGui


class BaseDialogMixIn(QtGui.QDialog, object):
    '''
    Base dialog mixin
    '''

    def showDialog(self):
        '''
        Show the dialog.

        :return:
        '''
        self.setupUi(self)
        self.retranslateUi(self)
        self.show()
        self.exec_()
