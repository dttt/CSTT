# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MacronutrientUserGroup'
        db.create_table(u'tvdd_macronutrientusergroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('macronutrient_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tvdd.Macronutrient'])),
            ('user_group_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tvdd.UserGroup'])),
        ))
        db.send_create_signal(u'tvdd', ['MacronutrientUserGroup'])


    def backwards(self, orm):
        # Deleting model 'MacronutrientUserGroup'
        db.delete_table(u'tvdd_macronutrientusergroup')


    models = {
        u'tvdd.dish': {
            'Meta': {'object_name': 'Dish'},
            'calories': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'carbohydrate': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'dietary_fiber': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'fat': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tvdd.Ingredient']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'protein': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tvdd.DishType']"}),
            'vegan': ('django.db.models.fields.BooleanField', [], {})
        },
        u'tvdd.dishtype': {
            'Meta': {'object_name': 'DishType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'tvdd.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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

    complete_apps = ['tvdd']