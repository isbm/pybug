from _settings import Ui_SettingsDialog
from basewindow import BaseDialogMixIn
from pybug import UtilsMixIn
import yaml
from yaml.scanner import ScannerError
from PyQt4 import QtGui


class SettingsWindow(Ui_SettingsDialog, BaseDialogMixIn, UtilsMixIn):
    '''
    Settings window.
    '''
    ASSIGNED_BUGS = 'assigned'
    IMPORTANT_BUGS = 'important'
    COMMON_BUGS = 'common'

    def __init__(self, config):
        '''
        Constructor requires a global config.

        :param config:
        :return:
        '''
        BaseDialogMixIn.__init__(self)
        self.config = config
        self._load_config()

    def _load_config(self):
        '''
        Load an existing configuration.

        :return:
        '''

    def on_save(self):
        '''
        Action on save.

        :return:
        '''
        errors = list()
        if 'search' not in self.config:
            self.config['search'] = dict()

        for result, err_code, err_msg, title, cnt in [self._validate_query(self.my_bugs_query.toPlainText(),
                                                                           self.ASSIGNED_BUGS,
                                                                           self.my_bugs_title.text() or 'N/A'),
                                                      self._validate_query(self.important_bugs_query.toPlainText(),
                                                                           self.IMPORTANT_BUGS,
                                                                           self.important_bugs_title.text() or 'N/A'),
                                                      self._validate_query(self.common_bugs_query.toPlainText(),
                                                                           self.COMMON_BUGS,
                                                                           self.common_bugs_title.text() or 'N/A')]:
            if result and not err_code and not err_msg:
                self.config['search'][cnt] = result
            else:
                errors.append(dict(message=err_msg, code=err_code, title=title))

        if errors:
            error_msg = ["<p>The following sections had an errors in the configuration:</p>", "<ul>"]
            for error in errors:
                error_msg.append("<li><b>{0}</b><br/>Reason:<br/><i>{1}</i></li>".format(error['title'], error['message']))
            error_msg.append("</ul>")
            reply = QtGui.QMessageBox.question(self, 'Message', "".join(error_msg),
                                               QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.save_config(self.config)
                self.close()

    def _validate_query(self, data, container, title):
        '''
        Validate YAML query.

        :param data:
        :param container:
        :param title:
        :return: (Config chunk with a title, Error Code or 0, Error Message or None,
                   title if invalid or None, container)
        '''
        data = self.to_str(data)
        title = self.to_str(title)
        try:
            # Poor's man YAML validator
            _ld = yaml.load(data)
            return (_ld and yaml.load(yaml.dump(_ld, default_flow_style=False)) == _ld
                    and {'data': _ld, 'title': title} or None, (_ld and 1 or 2) - 1,
                    not _ld and 'Data N/A' or None, not _ld and title or None, container)
        except ScannerError as yaml_error:
            return None, 1, str(yaml_error), title, None
        except Exception as yaml_exception:
            return None, 127, str(yaml_exception), title, None

    def retranslateUi(self, window):
        '''
        Set messages

        :param Dialog:
        :return:
        '''
        Ui_SettingsDialog.retranslateUi(self, window)
