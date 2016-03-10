'''
Bugzilla API connection
'''

import urllib2
import xmlrpclib
import urlparse
from ui.settings import SettingsWindow


class Url(object):
    '''
    Operations on the URL.
    '''
    def __init__(self, url):
        self._url = urlparse.urlparse(url)
        self._user = None
        self._password = None

    @property
    def user(self):
        '''
        Get user name

        :return:
        '''
        return self._user

    @user.setter
    def user(self, value):
        '''
        Set user name.

        :param value:
        :return:
        '''
        self._user = urllib2.quote(value)

    @property
    def password(self):
        '''
        Get password.

        :return:
        '''
        return self._password

    @password.setter
    def password(self, value):
        '''
        Set password.

        :param value:
        :return:
        '''
        self._password = urllib2.quote(value)

    def geturl(self):
        '''
        Get string URL.

        :return:
        '''
        return "{scheme}://{auth}{netloc}/{path}{query}{fragment}".format(
            scheme=self._url.scheme, auth=self._user and self._password and "{user}:{password}@".format(
                user=self._user, password=self._password) or '',
            netloc=self._url.netloc, path=self._url.path,
            query=self._url.query and '?{0}'.format(self._url.query) or '',
            fragment=self._url.fragment and '#{0}'.format(self._url.fragment) or '')

    def __getattr__(self, item):
        '''
        Return an item that belongs either to self or to url or return just None

        :param item:
        :return:
        '''
        return self.__dict__.get(item,  self._url.__dict__.get(item))


class Bugzilla(xmlrpclib.Server):
    '''
    Bugzilla server connection.
    '''
    def __init__(self, url, username, password):
        self.url = Url(url)
        self.url.user, self.url.password = username, password
        self.user_id = {'id': 0}

        xmlrpclib.Server.__init__(self, self.url.geturl())

    def login(self):
        '''
        Login into Bugzilla.

        :return:
        '''
        self.user_id = self.User.login(dict(login=self.url.user,
                                            password=self.url.password))
        return self

    def search(self, query):
        '''
        Search Bugzilla.

        :return:
        '''
        return (self.Bug.search(query) or dict()).get('bugs', list())


class BugzillaOperations(object):
    '''
    Operations over bugzilla
    '''
    def __init__(self, url, config):
        self.config = config
        self.bz = Bugzilla(url, self.config['bugzilla']['user'],
                           self.config['bugzilla']['password']).login()

    def get_my_bugs(self):
        '''
        Return a set of bugs, assigned to the logged in person.

        :return:
        '''

        ret = list()
        query_set = self.config.get('search', dict()).get(
            SettingsWindow.ASSIGNED_BUGS, dict()).get('data', dict())
        if not query_set:
            return ret

        for query_id, query_compound in query_set.items():
            print "Processing query", query_id
            if not query_compound.get('query'):
                continue
            for bug in self.bz.search(query_compound.get('query')):
                if not self._filter(bug, query_compound.get('filter')):
                    ret.append({
                        'id': bug['id'],
                        'priority': bug['priority'],
                        'status': bug['status'],
                        'resolution': bug['resolution'],
                        'title': bug['summary'],
                    })
        return ret

    def _filter(self, bug, q_filter):
        '''
        Return true, if data needs to be filtered out.

        :param q_filter:
        :return:
        '''
        if q_filter:
            if 'status' in q_filter and bug['status'] in q_filter.get('status'):
                return True
            if 'resolution' in q_filter:
                if not q_filter['resolution'] and bug['resolution']:
                    return True
                elif q_filter['resolution'] and bug['resolution'] in q_filter['resolution']:
                    return True

        return False
