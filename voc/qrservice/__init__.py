__author__ = 'khatcher'

from flask import Blueprint, render_template, request
from flask.views import MethodView

qrservice = Blueprint('qrservice', __name__, template_folder='templates')


class QRView(MethodView):

    def get(self, url):

        return render_template('qrservice/main.html', url=url)


qrservice.add_url_rule('/<url>/', view_func=QRView.as_view('qrview'))
