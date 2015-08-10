__author__ = 'khatcher'

import datetime

from flask import url_for

from voc import db


class InventoryEvent(db.EmbeddedDocument):
    inventoried_date = db.DateTimeField(default=datetime.datetime.now)
    taken_by = db.StringField()
    condition = db.StringField()

class InventoryItem(db.Document):
    url = db.StringField()
    name = db.StringField()
    category = db.StringField()
    manufacture_serial = db.StringField()
    location = db.StringField()
    inventoried_date = db.ListField(db.EmbeddedDocumentField('InventoryEvent'))
    purchase_date = db.DateTimeField(default=datetime.datetime.now)
    owner_serial = db.StringField()

    def get_absolute_url(self):
        return url_for('item', kwargs={"url": self.url})

    def __unicode__(self):
        return self.name


    meta = {
        'allow_inheritance': True,
        'indexes': ['-owner_serial', 'url'],
        'ordering': ['-owner_serial']
    }

