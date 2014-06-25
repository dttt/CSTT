# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MFMG'
        db.create_table(u'member_function_mfmg', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('macronutrient_user_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tvdd.MacronutrientUserGroup'])),
        ))
        db.send_create_signal(u'member_function', ['MFMG'])

        # Adding model 'MFEnergy'
        db.create_table(u'member_function_mfenergy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'member_function', ['MFEnergy'])

        # Adding model 'MFStatus'
        db.create_table(u'member_function_mfstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'member_function', ['MFStatus'])

        # Adding model 'ParameterMG'
        db.create_table(u'member_function_parametermg', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('min', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('max', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('member_function', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member_function.MFMG'])),
        ))
        db.send_create_signal(u'member_function', ['ParameterMG'])

        # Adding model 'ParameterEnergy'
        db.create_table(u'member_function_parameterenergy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('min', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('max', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('member_function', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member_function.MFEnergy'])),
        ))
        db.send_create_signal(u'member_function', ['ParameterEnergy'])

        # Adding model 'ParameterStatus'
        db.create_table(u'member_function_parameterstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('min', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('max', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('member_function', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['member_function.MFStatus'])),
        ))
        db.send_create_signal(u'member_function', ['ParameterStatus'])


    def backwards(self, orm):
        # Deleting model 'MFMG'
        db.delete_table(u'member_function_mfmg')

        # Deleting model 'MFEnergy'
        db.delete_table(u'member_function_mfenergy')

        # Deleting model 'MFStatus'
        db.delete_table(u'member_function_mfstatus')

        # Deleting model 'ParameterMG'
        db.delete_table(u'member_function_parametermg')

        # Deleting model 'ParameterEnergy'
        db.delete_table(u'member_function_parameterenergy')

        # Deleting model 'ParameterStatus'
        db.delete_table(u'member_function_parameterstatus')


    models = {
        u'member_function.mfenergy': {
            'Meta': {'object_name': 'MFEnergy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'member_function.mfmg': {
            'Meta': {'object_name': 'MFMG'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'macronutrient_user_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tvdd.MacronutrientUserGroup']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'member_function.mfstatus': {
            'Meta': {'object_name': 'MFStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'member_function.parameterenergy': {
            'Meta': {'object_name': 'ParameterEnergy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'member_function': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member_function.MFEnergy']"}),
            'min': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        u'member_function.parametermg': {
            'Meta': {'object_name': 'ParameterMG'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'member_function': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member_function.MFMG']"}),
            'min': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        u'member_function.parameterstatus': {
            'Meta': {'object_name': 'ParameterStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'member_function': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['member_function.MFStatus']"}),
            'min': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
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

    complete_apps = ['member_function']