from web2py_utils import test_runner
import unittest
import datetime


class TestDb(unittest.TestCase):
    def setUp(self):
        test_runner._PATH = ''
        self.env = test_runner.new_env(app='iDibo', controller='default')
        self.db = test_runner.copy_db(self.env, db_name='db',
                                      db_link='sqlite:memory')
        self.populate_database()

    def test_post_registration(self):
        # build the request with the data a user would add in register.html
        test_runner.set_crudform('auth_user',
                                 {'first_name': 'Jane',
                                  'last_name': 'Doe',
                                  'voters_registration_number': '123456',
                                  'role': '1',
                                  'email': 'pp@gmail.com',
                                  'password': 'mySecurePassword124'
                                  },
                                 self.env['request'],
                                 action="create",
                                 record_id=None)
        self.env['register']()

        self.print_tables()

        # assert the data has been saved in the database
        rows = self.db((self.db.auth_user.id != None) |
                       (self.db.auth_user.first_name == 'Jane')).select()
        # should currently fail, the select is not working properly
        assert rows is not None

    def populate_database(self):
        self.populate_roles()
        self.populate_users()
        self.populate_campaigns()

    def populate_roles(self):
        self.db.roles.insert(role='admin')
        self.db.roles.insert(role='user')

    def populate_users(self):
        self.db.auth_user.insert(first_name='The',
                                 last_name='Admin',
                                 voters_registration_number='12378919',
                                 role='1',
                                 email='test@test.com',
                                 password='the1234')

    def populate_campaigns(self):
        now = datetime.datetime.now()
        now_plus_a_week = now + datetime.timedelta(days=7)
        self.db.campaigns.insert(name='Lunch choice',
                                 start_date=now,
                                 end_date=now_plus_a_week,
                                 campaign_admin='1')

    def print_tables(self):
        print '\n roles: \n'
        rows = self.db(self.db.roles.id != None).select()
        for row in rows:
            print row
        print '\n users: \n'
        rows = self.db(self.db.auth_user.id != None).select()
        for row in rows:
            print row
        print '\n campaigns: \n'
        rows = self.db(self.db.campaigns.id != None).select()
        for row in rows:
            print row

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestDb))
unittest.TextTestRunner(verbosity=2).run(suite)