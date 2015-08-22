__author__ = 'johnson'
import unittest

from google.appengine.ext import testbed, ndb

from entity.user import User


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()
        self.initData()

    def initData(self):
        user1 = User()
        user1.name = 'Johnson'
        user1.password = User.hash_password('123')
        user1.put()
        user2 = User()
        user2.name = 'john'
        user2.password = User.hash_password('321')
        user2.put()

    def tearDown(self):
        self.testbed.deactivate()

    def testGetUser(self):
        print str(User.get_user('Johnson', '123'))


if __name__ == '__main__':
    unittest.main()
