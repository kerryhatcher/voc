__author__ = 'khatcher'

from werkzeug.local import LocalProxy
from flask import current_app


class SiteName(object):
    def __init__(self, app):
        if app is not None:
            self.init_app(app)

    def init_app(self, app, *args, **kwargs):
        app.context_processor(SiteName.site_name_context_processor)

        self.app = app
        if not hasattr(app, 'extensions'):
            app.extensions = {}

    @staticmethod
    def site_name():
        """Backend function for weather proxy
        :return: A list of weather items
        """


        return current_app.config.get('SITE_NAME')

    @staticmethod
    def site_name_context_processor():
        """add variable ''site_name'' to template context
        It contains the name of the website
        """

        return dict(site_name=site_name)

site_name = LocalProxy(SiteName.site_name)
