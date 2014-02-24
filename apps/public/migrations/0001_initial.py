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
            ('companyName', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('revenue', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('employeeCount', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('productsServices', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('companyDescription', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('companyType', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('dateJoined', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now, null=True, blank=True)),
        ))
        db.send_create_signal(u'public', ['Company'])

        # Adding model 'CompanyUser'
        db.create_table(u'public_companyuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Company'])),
            ('dateJoined', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'public', ['CompanyUser'])

        # Adding model 'SalesUser'
        db.create_table(u'public_salesuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('productsServices', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('salePriceLow', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('salePriceHigh', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('userDescription', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('contacts', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
            ('dateJoined', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'public', ['SalesUser'])

        # Adding model 'Job'
        db.create_table(u'public_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Company'])),
            ('dateAdded', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('listingTitle', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('startDate', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('totalCost', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('commissionAmount', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('linkUrl', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'public', ['Job'])

        # Adding model 'Application'
        db.create_table(u'public_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Job'])),
            ('dateApplied', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now)),
            ('appTitle', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('appDescription', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('appCost', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'public', ['Application'])

        # Adding model 'Chat'
        db.create_table(u'public_chat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Job'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Company'])),
            ('dateSent', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now, null=True, blank=True)),
            ('chatContent', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal(u'public', ['Chat'])

        # Adding model 'Rating'
        db.create_table(u'public_rating', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Job'])),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Company'])),
            ('dateRated', self.gf('django.db.models.fields.DateField')(default=datetime.datetime.now, null=True, blank=True)),
            ('ratingDetails', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
        ))
        db.send_create_signal(u'public', ['Rating'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table(u'public_address')

        # Deleting model 'Company'
        db.delete_table(u'public_company')

        # Deleting model 'CompanyUser'
        db.delete_table(u'public_companyuser')

        # Deleting model 'SalesUser'
        db.delete_table(u'public_salesuser')

        # Deleting model 'Job'
        db.delete_table(u'public_job')

        # Deleting model 'Application'
        db.delete_table(u'public_application')

        # Deleting model 'Chat'
        db.delete_table(u'public_chat')

        # Deleting model 'Rating'
        db.delete_table(u'public_rating')


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
        u'public.application': {
            'Meta': {'object_name': 'Application'},
            'appCost': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'appDescription': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'appTitle': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'dateApplied': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Job']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'public.chat': {
            'Meta': {'object_name': 'Chat'},
            'chatContent': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Company']"}),
            'dateSent': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Job']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'public.company': {
            'Meta': {'object_name': 'Company'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'companyDescription': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'companyName': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'companyType': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'dateJoined': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            'employeeCount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'productsServices': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'revenue': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        u'public.companyuser': {
            'Meta': {'object_name': 'CompanyUser'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Company']"}),
            'dateJoined': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'public.job': {
            'Meta': {'object_name': 'Job'},
            'commissionAmount': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Company']"}),
            'dateAdded': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'linkUrl': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'listingTitle': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'startDate': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'totalCost': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'public.rating': {
            'Meta': {'object_name': 'Rating'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Company']"}),
            'dateRated': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['public.Job']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'ratingDetails': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'public.salesuser': {
            'Meta': {'object_name': 'SalesUser'},
            'contacts': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'dateJoined': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'productsServices': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'salePriceHigh': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'salePriceLow': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'userDescription': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['public']