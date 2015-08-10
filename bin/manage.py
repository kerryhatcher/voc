# Set the path
import sys

import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server

from voc import app

app.config["MONGODB_SETTINGS"] = {'DB': "voc"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"
app.config["SITE_NAME"] = "VOC"

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

if __name__ == "__main__":
    manager.run()