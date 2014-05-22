# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Brother'
        db.create_table(u'portal_brother', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('pledge_class', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('grad_class', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('hometown', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('family', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('quote', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('quote_author', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('is_alumni', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bro_pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'portal', ['Brother'])


    def backwards(self, orm):
        # Deleting model 'Brother'
        db.delete_table(u'portal_brother')


    models = {
        u'portal.brother': {
            'Meta': {'object_name': 'Brother'},
            'bro_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'family': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'grad_class': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_alumni': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pledge_class': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'quote': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'quote_author': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['portal']