'''
Bugzilla API connection
'''

import bugzilla
from ui.settings import SettingsWindow

class BugzillaOperations(object):
    '''
    Operations over bugzilla
    '''
    def __init__(self, url, config):
        self.config = config
        self.bz = bugzilla.Bugzilla(url=url,
                                    user=self.config['bugzilla']['user'],
                                    password=self.config['bugzilla']['password'])

    def get_my_bugs(self):
        ret = list()
        query_params = self.config.get('search', dict()).get(SettingsWindow.ASSIGNED_BUGS, dict()).get('data', dict())
        if not query_params:
            return ret

        query = self.bz.build_query(**query_params)
        for bug in self.bz.query(query):
            ret.append({
                'id': bug.bug_id,
                'priority': bug.priority,
                'status': bug.bug_status,
                'title': bug.summary,
            })

        return ret
