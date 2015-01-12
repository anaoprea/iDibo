from nose.tools import *

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
        self.controller.register()
        my_title = self.controller.register.response.title
        self.assertEqual(my_title, 'iDibo Registration')


if __name__ == '__main__':
    unittest.main()