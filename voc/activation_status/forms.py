__author__ = 'khatcher'




from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators, TextAreaField, SelectField

class ChangeStatusForm (Form):
    status = SelectField(u'Status', choices=[('montering', '1-Montering'), ('partial', '2-Partial'), ('full', '3-Full')])