'''
UI MixIns, utilities.
'''
from PyQt4 import QtGui


class UIUtilsMixin(object):
    '''
    Creates utils mixin.
    '''

    def center(self):
        '''
        Centers the window on the screen.

        :return:
        '''
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
