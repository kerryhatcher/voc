__author__ = 'khatcher'

import datetime
import time

from flask import Blueprint, request, render_template, make_response

from PIL import ImageFont

from flask import send_file
from StringIO import StringIO



from helpers import serve_pil_image, make_image
from forms import ChangeStatusForm
from models import Status

StatusApp = Blueprint('StatusApp', __name__,
                    template_folder='templates')

bp_path = StatusApp.root_path



@StatusApp.route('/status.jpg')
def serve_img():
    img = make_image("full", bp_path)

    return serve_pil_image(img)


@StatusApp.route('/status.svg')
def templated_svg():
    status=Status.objects.order_by("-date").first().status
    if status == "montering":
        bgcolor = "green"
    elif status == "partial":
        bgcolor = "yellow"
    elif status == "full":
        bgcolor = "red"
    width = request.args.get('width', '800')
    height = request.args.get('height', '600')
    svg = render_template('status.svg', width=width, height=height, bgcolor=bgcolor, status=status)
    response = make_response(svg)
    response.content_type = 'image/svg+xml'
    return response



@StatusApp.route('/', methods=('GET', 'POST'))
def status_change():
    form = ChangeStatusForm()
    if request.method == 'POST':
        NewStaus = Status(status=form.status.data, date=time.time()).save()
    return render_template('statuschange.html', form=form)