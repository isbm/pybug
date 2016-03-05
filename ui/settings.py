from _settings import Ui_SettingsDialog
from basewindow import BaseDialogMixIn
import yaml
from yaml.scanner import ScannerError


class SettingsWindow(Ui_SettingsDialog, BaseDialogMixIn):
    '''
    Settings window.
    '''

    def __init__(self, config):
        '''
        Constructor requires a global config.

        :param config:
        :return:
        '''
        BaseDialogMixIn.__init__(self)
        self.config = config

    def on_save(self):
        '''
        Action on save.

        :return:
        '''
        print "Saved something"
        print self.p
        print self.config

    def _validate_query(self, data):
        '''
        Validate YAML query.

        :param data:
        :return: (Validity, Error Code, Error Message)
        '''
        data = data.strip()
        try:
            return data == yaml.dump(yaml.load(data), default_flow_style=False).strip(), 0, None
        except ScannerError as yaml_error:
            return False, 1, str(yaml_error)
        except Exception as yaml_exception:
            return False, 127, str(yaml_exception)

    def retranslateUi(self, window):
        '''
        Set messages

        :param Dialog:
        :return:
        '''
        Ui_SettingsDialog.retranslateUi(self, window)
