from _pybugui import Ui_MainWindow, _translate
from ui.uimix import UIUtilsMixin
from PyQt4 import QtGui
import sys


class MainWindow(QtGui.QMainWindow, Ui_MainWindow, UIUtilsMixin):
    '''
    Main window.
    '''
    def __init__(self):
        '''
        Constructor.

        :return:
        '''
        QtGui.QWidget.__init__(self, None)
        self.setupUi(self)
        self.retranslateUi(self)

    def retranslateUi(self, window):
        '''
        Set messages

        :param Dialog:
        :return:
        '''
        Ui_MainWindow.retranslateUi(self, window)

    def double_clicked(self):
        print "Fixup"

    def open_in_browser(self):
        '''
        Open a bug in the browser.

        :return:
        '''
        try:
            import webbrowser
        except ImportError as error:
            print >> sys.stderr, "Cannot open web browser: no module 'webbrowser' is available."
            return

        bug_item = self.my_bugs_table.selectedItems()  ## Select the last selected table. #somehow (an event on focus?)
        if bug_item:
            print "Opening bsc#%s" % bug_item[0].text()
            webbrowser.open_new_tab('https://bugzilla.suse.com/{0}'.format(bug_item[0].text()))
        else:
            from ui.alert import BugAlert
            alert = BugAlert()
            alert.set_title("Select a bug")
            alert.set_message("Please select some bug first.")
            alert.showDialog()
            print >> sys.stderr, "Please select some bug, perhaps?"
