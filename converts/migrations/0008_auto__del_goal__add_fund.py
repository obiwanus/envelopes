# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Goal'
        db.delete_table('converts_goal')

        # Adding model 'Fund'
        db.create_table('converts_fund', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='goals')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=0, decimal_places=2, max_digits=20)),
            ('saved', self.gf('django.db.models.fields.DecimalField')(default=0, decimal_places=2, max_digits=20)),
            ('start_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 4, 24, 0, 0))),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('payment_size', self.gf('django.db.models.fields.DecimalField')(default=0, decimal_places=2, max_digits=20)),
            ('payment_periodicity', self.gf('django.db.models.fields.CharField')(max_length=50, default='f')),
        ))
        db.send_create_signal('converts', ['Fund'])


    def backwards(self, orm):
        # Adding model 'Goal'
        db.create_table('converts_goal', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], related_name='goals')),
            ('payment_periodicity', self.gf('django.db.models.fields.CharField')(max_length=50, default='f')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 4, 17, 0, 0))),
            ('payment_size', self.gf('django.db.models.fields.DecimalField')(default=0, decimal_places=2, max_digits=20)),
            ('saved', self.gf('django.db.models.fields.DecimalField')(default=0, decimal_places=2, max_digits=20)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=0, decimal_places=2, max_digits=20)),
        ))
        db.send_create_signal('converts', ['Goal'])

        # Deleting model 'Fund'
        db.delete_table('converts_fund')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'db_table': "'django_content_type'", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'converts.actualexpense': {
            'Meta': {'object_name': 'ActualExpense'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 24, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''", 'db_index': 'True'}),
            'regular_expense': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['converts.Expense']", 'null': 'True', 'blank': 'True', 'related_name': "'actual_expenses'"}),
            'size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'decimal_places': '2', 'max_digits': '20'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'actual_expenses'"})
        },
        'converts.expense': {
            'Meta': {'object_name': 'Expense'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'f'"}),
            'size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'decimal_places': '2', 'max_digits': '20'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 24, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'expenses'"})
        },
        'converts.fund': {
            'Meta': {'object_name': 'Fund'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'payment_periodicity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'f'"}),
            'payment_size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'decimal_places': '2', 'max_digits': '20'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'decimal_places': '2', 'max_digits': '20'}),
            'saved': ('django.db.models.fields.DecimalField', [], {'default': '0', 'decimal_places': '2', 'max_digits': '20'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 24, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'goals'"})
        },
        'converts.income': {
            'Meta': {'object_name': 'Income'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'periodicity': ('django.db.models.fields.CharField', [], {'max_length': '50', 'default': "'f'"}),
            'size': ('django.db.models.fields.DecimalField', [], {'default': '0', 'decimal_places': '2', 'max_digits': '20'}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 24, 0, 0)'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'related_name': "'incomes'"})
        },
        'converts.settings': {
            'Meta': {'object_name': 'Settings'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period_length': ('django.db.models.fields.CharField', [], {'max_length': '2', 'default': "'f'"}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 24, 0, 0)'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']", 'related_name': "'settings'"})
        }
    }

    complete_apps = ['converts']