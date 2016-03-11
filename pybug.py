#!/usr/bin/python

import sys
import os
import yaml

from PyQt4 import QtCore, QtGui

from ui.pybugui import MainWindow
from ui.login import LoginWindow
import bugop


class UtilsMixIn(object):
    '''
    System utils
    '''

    CONFIG = '.pybugrc'
    CONFIG_PATH = os.path.join(os.path.expanduser('~'), CONFIG)

    def to_str(self, value):
        '''
        To string.

        :param qstring:
        :return:
        '''
        return (str(value) or '').strip()

    def delete_config(self):
        '''
        Removes config, if exists.

        :return:
        '''
        if self.config_exists():
            os.unlink(self.CONFIG_PATH)

    def config_exists(self):
        '''
        Returns True if config exists.

        :return:
        '''
        return os.path.exists(self.CONFIG_PATH)

    def get_config(self):
        '''
        Get configuration file.

        :return:
        '''
        return self.config_exists() and yaml.load(open(self.CONFIG_PATH).read()) or dict()

    def save_config(self, config):
        '''
        Save configuration file.

        :return:
        '''
        conf_data = yaml.dump(config, default_flow_style=False)
        conf = open(self.CONFIG_PATH, 'w')
        conf.write(conf_data)
        conf.close()


class RecordParamsMixIn(object):
    '''
    Takes care of the record status
    '''

    FOREGROUNDS = {
        'P0': QtGui.QColor(0xff, 0, 0),
        'P1': QtGui.QColor(0x88, 0, 0),
        'P2': QtGui.QColor(0xe6, 0x73, 0),
        'P3': QtGui.QColor(0, 0x66, 0),
        'P4': QtGui.QColor(0, 0x2d, 0xb3),
        'P5': QtGui.QColor(0, 0, 0),
    }

    BACKGROUNDS =  {
        'changed': QtGui.QColor(0xff, 0xff, 0x99),
    }

    def set_item_changed(self):
        '''
        Create font with bold.

        :return:
        '''

    def set_item_priority(self, table, data, row_id):
        '''
        Set item priority.

        :return:
        '''
        for cidx in range(3):
            table.item(row_id, cidx).setForeground(self.FOREGROUNDS[data[row_id]['priority'][:2]])

    def set_item_data(self, table, data, row_id):
        '''
        Set item data

        :param table:
        :param data:
        :param row_id:
        :return:
        '''
        table.setItem(row_id, 0, QtGui.QTableWidgetItem())
        table.item(row_id, 0).setText(str(data[row_id]['id']))
        table.setItem(row_id, 1, QtGui.QTableWidgetItem())
        table.item(row_id, 1).setText(data[row_id]['status'])
        table.setItem(row_id, 2, QtGui.QTableWidgetItem())
        table.item(row_id, 2).setText(data[row_id]['title'])


class StartQT4(RecordParamsMixIn, UtilsMixIn):
    def __init__(self, parent=None):
        self.config = self.get_config()
        self.ui = MainWindow(self.config).center()
        self.reset_table()

        error_title, error_message = None, None
        try:
            self.login()
        except Exception as error:
            error_title, error_message = "Login Error", str(error)

        try:
            self.load_bugs()
        except Exception as error:
            print sys.stderr, error
            error_title, error_message = "Loading Bugs Error", "Unhandled exception occurred while loading bug list."

        if error_message:
            QtGui.QMessageBox.critical(None, error_title, error_message, QtGui.QMessageBox.Abort)
            sys.exit(1)

        self.ui_fixup()

        # Widget fix-up
        self.ui.my_bugs_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

    def login(self):
        '''
        Ask for password/uid.

        :return:
        '''
        self.login_window = LoginWindow(self.config_exists(),
                                        user=self.config.get('bugzilla', {}).get('user'),
                                        password=self.config.get('bugzilla', {}).get('password'))
        self.login_window.showDialog()
        if self.login_window.state:
            if 'bugzilla' not in self.config:
                self.config['bugzilla'] = dict()
            uid = self.to_str(self.login_window.uid_field.text())
            pwd = self.to_str(self.login_window.password_field.text())

            if self.config['bugzilla'].get('user') != uid:
                self.config['bugzilla']['user'] = uid
            if self.config['bugzilla'].get('password') != pwd:
                self.config['bugzilla']['password'] = pwd
            if self.login_window.private_computer_check.isChecked():
                self.save_config(self.config)
            self.bugop = bugop.BugzillaOperations('https://apibugzilla.novell.com/xmlrpc.cgi', self.config)

    def ui_fixup(self):
        '''
        Post-loading UI parts

        :return:
        '''
        self.ui.my_bugs_table.horizontalHeader().setStretchLastSection(True)

    def reset_table(self):
        '''
        Removes everything from the table.
        '''
        self.ui.my_bugs_table.setColumnCount(3)
        self.ui.my_bugs_table.setRowCount(0)

    def load_bugs(self):
        '''
        Load bugs
        '''
        data = self.bugop.get_my_bugs()
        self.ui.my_bugs_table.setRowCount(len(data))

        _sorting = self.ui.my_bugs_table.isSortingEnabled()
        self.ui.my_bugs_table.setSortingEnabled(False)
        
        for ridx in range(len(data)):
            self.set_item_data(self.ui.my_bugs_table, data, ridx)
            self.set_item_priority(self.ui.my_bugs_table, data, ridx)

        self.ui.my_bugs_table.setSortingEnabled(_sorting)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.ui.show()
    sys.exit(app.exec_())
