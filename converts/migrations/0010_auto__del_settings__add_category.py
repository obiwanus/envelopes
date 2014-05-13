# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Settings'
        db.delete_table('converts_settings')

        # Adding model 'Category'
        db.create_table('converts_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('converts', ['Category'])


    def backwards(self, orm):
        # Adding model 'Settings'
        db.create_table('converts_settings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('period_length', self.gf('django.db.models.fields.CharField')(default='f', max_length=2)),
            ('start_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 5, 4, 0, 0))),
        ))
        db.send_create_signal('converts', ['Settings'])

        # Deleting model 'Category'
        db.delete_table('converts_category')


    models = {
        'converts.actualexpense': {
            'Meta': {'object_name': 'ActualExpense'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'db_index': 'True', 'max_length': '255'}),
            'regular_expense': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actual_expenses'", 'blank': 'True', 'null': 'True', 'to': "orm['converts.Expense']"}),
            'size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'decimal_places': '2', 'max_digits': '20'})
        },
        'converts.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'converts.expense': {
            'Meta': {'object_name': 'Expense'},
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'default': "'f'", 'max_length': '50'}),
            'size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'decimal_places': '2', 'max_digits': '20'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)'})
        },
        'converts.fund': {
            'Meta': {'object_name': 'Fund'},
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200'}),
            'payment_periodicity': ('django.db.models.fields.CharField', [], {'default': "'f'", 'max_length': '50'}),
            'payment_size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'decimal_places': '2', 'max_digits': '20'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'decimal_places': '2', 'max_digits': '20'}),
            'saved': ('django.db.models.fields.DecimalField', [], {'default': '0', 'decimal_places': '2', 'max_digits': '20'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)'})
        },
        'converts.income': {
            'Meta': {'object_name': 'Income'},
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'default': "'f'", 'max_length': '50'}),
            'size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'decimal_places': '2', 'max_digits': '20'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)'})
        }
    }

    complete_apps = ['converts']