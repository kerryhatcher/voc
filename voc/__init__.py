__author__ = 'khatcher'


from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask_bootstrap import Bootstrap
from flask.ext.elasticsearch import FlaskElasticsearch
from flask_menu import Menu, register_menu



app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "inventory"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
es = FlaskElasticsearch(app)
db = MongoEngine(app)
Bootstrap(app)
Menu(app=app)

def register_blueprints(app):
    # Prevents circular imports
    from voc.inventory import inventory
    from voc.qrservice import qrservice
    from voc.activation_status import StatusApp
    app.register_blueprint(inventory, url_prefix='/inventory')
    app.register_blueprint(qrservice, url_prefix='/qrservice')
    app.register_blueprint(StatusApp, url_prefix='/status')
    from voc.views import IndexView
    IndexView.register(app)




register_blueprints(app)



if __name__ == "__main__":
    app.debug=True
    app.run()