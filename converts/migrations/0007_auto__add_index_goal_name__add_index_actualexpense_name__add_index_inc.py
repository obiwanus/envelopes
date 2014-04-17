# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'Goal', fields ['name']
        db.create_index('converts_goal', ['name'])

        # Adding index on 'ActualExpense', fields ['name']
        db.create_index('converts_actualexpense', ['name'])

        # Adding index on 'Income', fields ['name']
        db.create_index('converts_income', ['name'])

        # Adding index on 'Expense', fields ['name']
        db.create_index('converts_expense', ['name'])


    def backwards(self, orm):
        # Removing index on 'Expense', fields ['name']
        db.delete_index('converts_expense', ['name'])

        # Removing index on 'Income', fields ['name']
        db.delete_index('converts_income', ['name'])

        # Removing index on 'ActualExpense', fields ['name']
        db.delete_index('converts_actualexpense', ['name'])

        # Removing index on 'Goal', fields ['name']
        db.delete_index('converts_goal', ['name'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'converts.actualexpense': {
            'Meta': {'object_name': 'ActualExpense'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 17, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'db_index': 'True'}),
            'regular_expense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['converts.Expense']", 'related_name': "'actual_expenses'", 'blank': 'True', 'null': 'True'}),
            'size': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'default': '0', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'actual_expenses'"})
        },
        'converts.expense': {
            'Meta': {'object_name': 'Expense'},
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'default': "'f'", 'max_length': '50'}),
            'size': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'default': '0', 'decimal_places': '2'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 17, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'expenses'"})
        },
        'converts.goal': {
            'Meta': {'object_name': 'Goal'},
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'payment_periodicity': ('django.db.models.fields.CharField', [], {'default': "'f'", 'max_length': '50'}),
            'payment_size': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'default': '0', 'decimal_places': '2'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'default': '0', 'decimal_places': '2'}),
            'saved': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'default': '0', 'decimal_places': '2'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 17, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'goals'"})
        },
        'converts.income': {
            'Meta': {'object_name': 'Income'},
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'default': "'f'", 'max_length': '50'}),
            'size': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'default': '0', 'decimal_places': '2'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 17, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'incomes'"})
        },
        'converts.settings': {
            'Meta': {'object_name': 'Settings'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period_length': ('django.db.models.fields.CharField', [], {'default': "'f'", 'max_length': '2'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 17, 0, 0)'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'related_name': "'settings'"})
        }
    }

    complete_apps = ['converts']