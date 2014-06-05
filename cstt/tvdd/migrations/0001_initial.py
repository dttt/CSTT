# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserGroup'
        db.create_table(u'tvdd_usergroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('begin_age', self.gf('django.db.models.fields.IntegerField')()),
            ('end_age', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'tvdd', ['UserGroup'])

        # Adding model 'Macronutrient'
        db.create_table(u'tvdd_macronutrient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('equal_calories', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'tvdd', ['Macronutrient'])

        # Adding model 'DishType'
        db.create_table(u'tvdd_dishtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'tvdd', ['DishType'])

        # Adding model 'Ingredient'
        db.create_table(u'tvdd_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'tvdd', ['Ingredient'])

        # Adding model 'Dish'
        db.create_table(u'tvdd_dish', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tvdd.DishType'])),
            ('vegan', self.gf('django.db.models.fields.BooleanField')()),
            ('calories', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('protein', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('fat', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('carbohydrate', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('dietary_fiber', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('main_ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tvdd.Ingredient'])),
        ))
        db.send_create_signal(u'tvdd', ['Dish'])


    def backwards(self, orm):
        # Deleting model 'UserGroup'
        db.delete_table(u'tvdd_usergroup')

        # Deleting model 'Macronutrient'
        db.delete_table(u'tvdd_macronutrient')

        # Deleting model 'DishType'
        db.delete_table(u'tvdd_dishtype')

        # Deleting model 'Ingredient'
        db.delete_table(u'tvdd_ingredient')

        # Deleting model 'Dish'
        db.delete_table(u'tvdd_dish')


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
        u'tvdd.usergroup': {
            'Meta': {'object_name': 'UserGroup'},
            'begin_age': ('django.db.models.fields.IntegerField', [], {}),
            'end_age': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['tvdd']