# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Fund.payment_periodicity'
        db.alter_column('converts_fund', 'payment_periodicity', self.gf('django.db.models.fields.CharField')(null=True, max_length=50))

    def backwards(self, orm):

        # Changing field 'Fund.payment_periodicity'
        db.alter_column('converts_fund', 'payment_periodicity', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        'converts.actualexpense': {
            'Meta': {'object_name': 'ActualExpense'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'db_index': 'True'}),
            'regular_expense': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['converts.Expense']", 'related_name': "'actual_expenses'", 'blank': 'True'}),
            'size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'})
        },
        'converts.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'converts.expense': {
            'Meta': {'object_name': 'Expense'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'f'"}),
            'size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)'})
        },
        'converts.fund': {
            'Meta': {'object_name': 'Fund'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'payment_periodicity': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'default': "'f'", 'blank': 'True'}),
            'payment_size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'saved': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)'})
        },
        'converts.income': {
            'Meta': {'object_name': 'Income'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'f'"}),
            'size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 13, 0, 0)'})
        }
    }

    complete_apps = ['converts']