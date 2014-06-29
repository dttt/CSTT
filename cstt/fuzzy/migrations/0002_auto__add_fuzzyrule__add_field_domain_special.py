# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FuzzyRule'
        db.create_table(u'fuzzy_fuzzyrule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supposition', self.gf('django.db.models.fields.related.ForeignKey')(related_name='supposition', to=orm['fuzzy.FuzzySet'])),
            ('result', self.gf('django.db.models.fields.related.ForeignKey')(related_name='result', to=orm['fuzzy.FuzzySet'])),
        ))
        db.send_create_signal(u'fuzzy', ['FuzzyRule'])

        # Adding field 'Domain.special'
        db.add_column(u'fuzzy_domain', 'special',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tvdd.MacronutrientUserGroup'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'FuzzyRule'
        db.delete_table(u'fuzzy_fuzzyrule')

        # Deleting field 'Domain.special'
        db.delete_column(u'fuzzy_domain', 'special_id')


    models = {
        u'fuzzy.domain': {
            'Meta': {'object_name': 'Domain'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'special': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tvdd.MacronutrientUserGroup']", 'null': 'True', 'blank': 'True'})
        },
        u'fuzzy.fuzzyrule': {
            'Meta': {'object_name': 'FuzzyRule'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'result'", 'to': u"orm['fuzzy.FuzzySet']"}),
            'supposition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'supposition'", 'to': u"orm['fuzzy.FuzzySet']"})
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
        },
        u'tvdd.macronutrient': {
            'Meta': {'object_name': 'Macronutrient'},
            'equal_calories': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'tvdd.macronutrientusergroup': {
            'Meta': {'object_name': 'MacronutrientUserGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'macronutrient_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tvdd.Macronutrient']"}),
            'user_group_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tvdd.UserGroup']"})
        },
        u'tvdd.usergroup': {
            'Meta': {'object_name': 'UserGroup'},
            'begin_age': ('django.db.models.fields.IntegerField', [], {}),
            'end_age': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['fuzzy']