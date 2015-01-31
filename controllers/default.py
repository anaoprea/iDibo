# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to iDibo!")
    #auth.settings.register_onaccept = _add_role()
    return dict()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


def register():
    auth.settings.register_next = 'confirm.html'
    response.title = 'iDibo Registration'
    return dict(form=auth.register())


@auth.requires_login()
def confirm():
    response.title = 'iDibo'
    #count = db(db.campaigns.name).count
    campaigns = db().select(db.campaigns.name)
    return dict(campaigns=campaigns)


@auth.requires_login()
def confirm_html():
    return dict()
    #
    #def _add_role(form):
    #    group_id = auth.id_group(role=form.vars.role)
    #    user_id = form.vars.id
    #    auth.add_membership(group_id,user_id)
    #
    #@auth.requires_login()
    #@auth.requires_membership('Admin user')
    #def confirm_admin():
    #    return dict()