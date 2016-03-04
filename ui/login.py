import sys

from _login import Ui_LoginDialog
from basewindow import BaseDialogMixIn


class LoginWindow(Ui_LoginDialog, BaseDialogMixIn):
    '''
    Login window.
    '''
    state = False

    def __init__(self, is_private_machine, **kwargs):
        self._kwargs = kwargs
        self.is_private_machine = is_private_machine
        Ui_LoginDialog.__init__(self)
        BaseDialogMixIn.__init__(self)

    def setupUi(self, panel):
        '''
        Set up ui.

        :param LoginDialog:
        :return:
        '''
        Ui_LoginDialog.setupUi(self, panel)
        self.private_computer_check.setChecked(self.is_private_machine)
        self.uid_field.setText(self._kwargs.get('user', ''))
        self.password_field.setText(self._kwargs.get('password', ''))

    def on_login(self):
        '''
        Set login state.

        :return:
        '''
        self.state = True
        self.hide()

    def on_exit(self):
        '''
        Exit.

        :return:
        '''
        sys.exit(1)