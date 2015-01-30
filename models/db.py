from gluon.tools import Auth

db = DAL('sqlite://storage.sqlite', pool_size=1, check_reserved=['all'])
auth = Auth(db)

"""Role Table"""
db.define_table('roles',
                Field('role'), format='%(role)s')

"""User Table"""
# This allows using the web2py auth module while still customising properly the fields
db.define_table('auth_user',
                Field('first_name', length=128, default=''),
                Field('last_name', length=128, default=''),
                Field('voters_registration_number', ),
                Field('role', db.roles),
                Field('email', length=128, default='', unique=True),
                Field('password', 'password', length=512, readable=False, label='Password'),
                Field('registration_key', length=512, writable=False, readable=False, default=''),
                Field('reset_password_key', length=512, writable=False, readable=False, default=''),
                Field('registration_id', length=512, writable=False, readable=False, default=''),
                format='%(email)s')

#validators
custom_auth_table = db['auth_user'] # get the custom_auth_table
custom_auth_table.first_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
custom_auth_table.last_name.requires = IS_NOT_EMPTY(error_message=auth.messages.is_empty)
custom_auth_table.password.requires = [IS_STRONG(special=0, upper=0, min=6),
                                       CRYPT()]#CRYPT validator here handles salting of the password
custom_auth_table.email.requires = [
    IS_EMAIL(error_message=auth.messages.invalid_email),
    IS_NOT_EMPTY(),
    IS_NOT_IN_DB(db, custom_auth_table.email, error_message='Email already exists')]
custom_auth_table.voters_registration_number.requires = [
    IS_NOT_EMPTY(),
    IS_NOT_IN_DB(db, custom_auth_table.voters_registration_number)
]
#custom_auth_table.role.requires = IS_IN_SET(['Regular User', 'Admin User'])

auth.settings.table_user = custom_auth_table # tell auth to use custom_auth_table
auth.settings.login_next = URL('confirm') #This helps to change the redirected url on user registration or login
auth.define_tables(signature=True)

"""Campaign Table"""

db.define_table('campaigns',
                Field('name'),
                Field('start_date', type='date'),
                Field('end_date', type='date'),
                Field('campaign_admin'),
                format='%(name)s')#this should be aidated to ensussre admin actually has role admin
"""Options Table (options for each campaign)"""
db.define_table('campaign_options',
                Field('name', unique=True),
                Field('counter', type='integer', default=0),
                Field('campaign', db.campaigns))

"""Participation Table"""
db.define_table('participation',
                Field('user_id',db.auth_user),
                Field('campaign',db.campaigns),
                Field('has_voted',default='False'),
                )



#test database that's laid out just like the "real" database
#import copy
#
#test_db = DAL('sqlite://testing.sqlite')
#for tablename in db.tables:
#    table_copy = [copy.copy(f) for f in db[tablename]]
#    test_db.define_table(tablename, *table_copy)





