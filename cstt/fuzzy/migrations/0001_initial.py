# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Domain'
        db.create_table(u'fuzzy_domain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'fuzzy', ['Domain'])

        # Adding model 'FuzzySet'
        db.create_table(u'fuzzy_fuzzyset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('domain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuzzy.Domain'])),
        ))
        db.send_create_signal(u'fuzzy', ['FuzzySet'])

        # Adding model 'Parameter'
        db.create_table(u'fuzzy_parameter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fuzzy_set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fuzzy.FuzzySet'])),
            ('min', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('max', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'fuzzy', ['Parameter'])


    def backwards(self, orm):
        # Deleting model 'Domain'
        db.delete_table(u'fuzzy_domain')

        # Deleting model 'FuzzySet'
        db.delete_table(u'fuzzy_fuzzyset')

        # Deleting model 'Parameter'
        db.delete_table(u'fuzzy_parameter')


    models = {
        u'fuzzy.domain': {
            'Meta': {'object_name': 'Domain'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'fuzzy.fuzzyset': {
            'Meta': {'object_name': 'FuzzySet'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fuzzy.Domain']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'fuzzy.parameter': {
            'Meta': {'object_name': 'Parameter'},
            'fuzzy_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fuzzy.FuzzySet']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'min': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['fuzzy']