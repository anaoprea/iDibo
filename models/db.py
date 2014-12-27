from gluon.tools import Auth
db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'])
auth = Auth(db)


auth.settings.extra_fields['auth_user']= [
    Field('Voters Identification Number', 'string')
    ]
auth.define_tables(username=True)