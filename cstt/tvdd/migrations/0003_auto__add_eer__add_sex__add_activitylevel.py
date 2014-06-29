# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EER'
        db.create_table(u'tvdd_eer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('min_age', self.gf('django.db.models.fields.IntegerField')()),
            ('max_age', self.gf('django.db.models.fields.IntegerField')()),
            ('sex', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tvdd.Sex'])),
            ('calories', self.gf('django.db.models.fields.IntegerField')()),
            ('activity_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tvdd.ActivityLevel'])),
        ))
        db.send_create_signal(u'tvdd', ['EER'])

        # Adding model 'Sex'
        db.create_table(u'tvdd_sex', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal(u'tvdd', ['Sex'])

        # Adding model 'ActivityLevel'
        db.create_table(u'tvdd_activitylevel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'tvdd', ['ActivityLevel'])


    def backwards(self, orm):
        # Deleting model 'EER'
        db.delete_table(u'tvdd_eer')

        # Deleting model 'Sex'
        db.delete_table(u'tvdd_sex')

        # Deleting model 'ActivityLevel'
        db.delete_table(u'tvdd_activitylevel')


    models = {
        u'tvdd.activitylevel': {
            'Meta': {'object_name': 'ActivityLevel'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
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
        u'tvdd.eer': {
            'Meta': {'object_name': 'EER'},
            'activity_level': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tvdd.ActivityLevel']"}),
            'calories': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_age': ('django.db.models.fields.IntegerField', [], {}),
            'min_age': ('django.db.models.fields.IntegerField', [], {}),
            'sex': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tvdd.Sex']"})
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
        u'tvdd.sex': {
            'Meta': {'object_name': 'Sex'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '5'})
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