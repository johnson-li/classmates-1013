import hashlib
from logging import getLogger

from google.appengine.ext import ndb

__author__ = 'johnson'
logger = getLogger()


class User(ndb.Model):
    """ Simple user class

    Attributes:
        |priority    1 for root user
        |            5 for normal user
    """
    name = ndb.StringProperty(indexed=True)
    password = ndb.StringProperty()
    priority = ndb.IntegerProperty()
    type = ndb.IntegerProperty()

    def __init__(self, *args, **kwargs):
        ndb.Model.__init__(self)
        self.__authenticated = True
        self.name = kwargs.get('name', None)
        self.password = kwargs.get('password', None)
        self.type = kwargs.get('user_type', 5)

    def is_authenticated(self):
        return self.__authenticated

    def is_active(self):
        return self.type > 0

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.name

    @staticmethod
    def user_key(user_id=0):
        return ndb.Key('User', user_id)

    @staticmethod
    def hash_password(password):
        password = str(password)
        return hashlib.sha224(password).hexdigest()

    @staticmethod
    def get_user(name, password=None):
        logger.info("get user: " + name + " " + User.hash_password(password))
        user_query = User.query().filter(User.name == name)
        if password:
            password = str(password)
            user_query = user_query.filter(User.password == User.hash_password(password))
        users = user_query.fetch(1)
        logger.info("user query res: " + str(users))
        if users and len(users) > 0:
            return users[0]
        return None
