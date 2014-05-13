# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Expense.floating'
        db.add_column('converts_expense', 'floating',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Expense.floating'
        db.delete_column('converts_expense', 'floating')


    models = {
        'converts.actualexpense': {
            'Meta': {'object_name': 'ActualExpense'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'default': "''"}),
            'regular_expense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['converts.Expense']", 'blank': 'True', 'related_name': "'actual_expenses'", 'null': 'True'}),
            'size': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'default': '0', 'decimal_places': '2'})
        },
        'converts.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'converts.expense': {
            'Meta': {'object_name': 'Expense'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['converts.Category']", 'null': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'floating': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'f'"}),
            'size': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'default': '0', 'decimal_places': '2'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)'})
        },
        'converts.fund': {
            'Meta': {'object_name': 'Fund'},
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200'}),
            'payment_periodicity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True', 'default': "'f'"}),
            'payment_size': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'default': '0', 'decimal_places': '2'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'default': '0', 'decimal_places': '2'}),
            'saved': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'default': '0', 'decimal_places': '2'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)'})
        },
        'converts.income': {
            'Meta': {'object_name': 'Income'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['converts.Category']", 'null': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'f'"}),
            'size': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'default': '0', 'decimal_places': '2'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)'})
        }
    }

    complete_apps = ['converts']