__author__ = 'khatcher'
from flask import Blueprint, render_template
from flask.views import MethodView
from flask_admin import Admin
from voc.inventory import InventoryModelView
from voc.inventory.models import InventoryItem
from voc import app
from flask_menu import register_menu
from voc import Menu
from flask_classy import FlaskView
from flask_menu import classy


admin = Admin(app, name='NetEOC', template_mode='bootstrap3')

admin.add_view(InventoryModelView(InventoryItem))


class IndexView(FlaskView):
    route_base = '/'

    def index(self):
        return render_template('eoc/index.html')


