# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Fund.user'
        db.delete_column('converts_fund', 'user_id')

        # Deleting field 'Settings.user'
        db.delete_column('converts_settings', 'user_id')

        # Deleting field 'Expense.user'
        db.delete_column('converts_expense', 'user_id')

        # Deleting field 'Income.user'
        db.delete_column('converts_income', 'user_id')

        # Deleting field 'ActualExpense.user'
        db.delete_column('converts_actualexpense', 'user_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Fund.user'
        raise RuntimeError("Cannot reverse this migration. 'Fund.user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Fund.user'
        db.add_column('converts_fund', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='goals', to=orm['auth.User']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Settings.user'
        raise RuntimeError("Cannot reverse this migration. 'Settings.user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Settings.user'
        db.add_column('converts_settings', 'user',
                      self.gf('django.db.models.fields.related.OneToOneField')(unique=True, related_name='settings', to=orm['auth.User']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Expense.user'
        raise RuntimeError("Cannot reverse this migration. 'Expense.user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Expense.user'
        db.add_column('converts_expense', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='expenses', to=orm['auth.User']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Income.user'
        raise RuntimeError("Cannot reverse this migration. 'Income.user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Income.user'
        db.add_column('converts_income', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='incomes', to=orm['auth.User']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'ActualExpense.user'
        raise RuntimeError("Cannot reverse this migration. 'ActualExpense.user' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ActualExpense.user'
        db.add_column('converts_actualexpense', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='actual_expenses', to=orm['auth.User']),
                      keep_default=False)


    models = {
        'converts.actualexpense': {
            'Meta': {'object_name': 'ActualExpense'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 4, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'db_index': 'True', 'max_length': '255'}),
            'regular_expense': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'actual_expenses'", 'null': 'True', 'blank': 'True', 'to': "orm['converts.Expense']"}),
            'size': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'default': '0', 'max_digits': '20'})
        },
        'converts.expense': {
            'Meta': {'object_name': 'Expense'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'default': "'f'", 'max_length': '50'}),
            'size': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'default': '0', 'max_digits': '20'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 4, 0, 0)'})
        },
        'converts.fund': {
            'Meta': {'object_name': 'Fund'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200'}),
            'payment_periodicity': ('django.db.models.fields.CharField', [], {'default': "'f'", 'max_length': '50'}),
            'payment_size': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'default': '0', 'max_digits': '20'}),
            'price': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'default': '0', 'max_digits': '20'}),
            'saved': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'default': '0', 'max_digits': '20'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 4, 0, 0)'})
        },
        'converts.income': {
            'Meta': {'object_name': 'Income'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'default': "'f'", 'max_length': '50'}),
            'size': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'default': '0', 'max_digits': '20'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 4, 0, 0)'})
        },
        'converts.settings': {
            'Meta': {'object_name': 'Settings'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period_length': ('django.db.models.fields.CharField', [], {'default': "'f'", 'max_length': '2'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 5, 4, 0, 0)'})
        }
    }

    complete_apps = ['converts']