'''
Bugzilla API connection
'''

import bugzilla

class BugzillaOperations(object):
    '''
    Operations over bugzilla
    '''
    def __init__(self, url, user, password):
        self.bz = bugzilla.Bugzilla(url=url, user=user, password=password)

    def get_my_bugs(self):
        ret = list()
        query = self.bz.build_query(assigned_to=self.bz.user + '@suse.com')
        for bug in self.bz.query(query):
            ret.append({
                'id': bug.bug_id,
                'priority': bug.priority,
                'status': bug.bug_status,
                'title': bug.summary,
            })

        return ret
