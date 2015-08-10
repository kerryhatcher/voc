__author__ = 'khatcher'


from flask import Blueprint, render_template
from flask.views import MethodView

from flask_admin.contrib.mongoengine import ModelView
from flask.ext.qrcode import QRcode

from voc.inventory.models import InventoryItem
from voc import app

inventory = Blueprint('inventory', __name__, template_folder='templates')

QRcode(app)

class ListView(MethodView):

    def get(self):
        items = InventoryItem.objects.all()
        return render_template('items/list.html', items=items)


class DetailView(MethodView):

    def get(self, url):
        post = InventoryItem.objects.get_or_404(url=url)
        return render_template('items/detail.html', item=post)


class InventoryModelView(ModelView):
    # edit_template = 'inventory_list.html'
    # create_template = 'microblog_create.html'
    list_template = 'inventory_list.html'



# Register the urls
inventory.add_url_rule('/', view_func=ListView.as_view('list'))
inventory.add_url_rule('/<url>/', view_func=DetailView.as_view('detail'))