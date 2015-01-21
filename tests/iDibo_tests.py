import unittest
from gluon.shell import exec_environment
from gluon.contrib.test_helpers import form_postvars

from gluon.globals import Request


db = test_db

#execfile("applications/iDibo/controllers/default.py", globals())
db(db.auth_user.id > 0).delete()
db.commit()


class TestRegister(unittest.TestCase):
    def setUp(self):
        #request = Request()
        self.controller = exec_environment('applications/iDibo/controllers/default.py')

    def test_register_title(self):
        form_postvars('auth_user', {'email': 'pp@gmail.com', 'first_name': 'Ana'}, request, action='create',
                      record_id=None)
        resp = self.controller.register()


        for key in resp.iteritems():
            print key
        self.assertEquals('Ana', resp['first_name'])




suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestRegister))
unittest.TextTestRunner(verbosity=2).run(suite)