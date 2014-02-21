# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'public_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'public', ['Address'])

        # Adding model 'Company'
        db.create_table(u'public_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('companyName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('revenue', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('employeeCount', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('productsServices', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('companyDescription', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('companyType', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dateJoined', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'public', ['Company'])

        # Adding model 'CompanyUser'
        db.create_table(u'public_companyuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Company'])),
            ('dateJoined', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'public', ['CompanyUser'])

        # Adding model 'SalesUser'
        db.create_table(u'public_salesuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('productsServices', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('salePriceLow', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('salePriceHigh', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('userDescription', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('contacts', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('dateJoined', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'public', ['SalesUser'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table(u'public_address')

        # Deleting model 'Company'
        db.delete_table(u'public_company')

        # Deleting model 'CompanyUser'
        db.delete_table(u'public_companyuser')

        # Deleting model 'SalesUser'
        db.delete_table(u'public_salesuser')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'public.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'public.company': {
            'Meta': {'object_name': 'Company'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'companyDescription': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'companyName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'companyType': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dateJoined': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'employeeCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'productsServices': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'revenue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'public.companyuser': {
            'Meta': {'object_name': 'CompanyUser'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Company']"}),
            'dateJoined': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'public.salesuser': {
            'Meta': {'object_name': 'SalesUser'},
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'dateJoined': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'productsServices': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'salePriceHigh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'salePriceLow': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'userDescription': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['public']