import unittest
from gluon.globals import Request

db = test_db

execfile("applications/iDibo/controllers/default.py", globals())
db(db.auth_user.id > 0).delete()
db.commit()


class TestRegister(unittest.TestCase):
    def setup(self):
        request = Request()


    def test_register_title(self):
        request.vars['email'] = 'lala@gmail.com'
        resp = register()
        for key in resp.iteritems():
            print key
        self.assertEquals(1, len(resp["auth_user"]))
        #my_title = self.request.register.response.title
        #self.assertEqual(my_title, 'iDibo Registration')


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestRegister))
unittest.TextTestRunner(verbosity=2).run(suite)