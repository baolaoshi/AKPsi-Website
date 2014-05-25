# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Brother.major'
        db.add_column(u'portal_brother', 'major',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Brother.major'
        db.delete_column(u'portal_brother', 'major')


    models = {
        u'portal.brother': {
            'Meta': {'object_name': 'Brother'},
            'bro_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'family': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'grad_class': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_alumni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pledge_class': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'quote': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'quote_author': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'})
        }
    }

    complete_apps = ['portal']