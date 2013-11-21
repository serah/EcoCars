# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CarCount'
        db.create_table(u'tabs_carcount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'tabs', ['CarCount'])

        # Adding model 'CompanyWiseCarCount'
        db.create_table(u'tabs_companywisecarcount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('CompanyName', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('eleven', self.gf('django.db.models.fields.IntegerField')()),
            ('twelve', self.gf('django.db.models.fields.IntegerField')()),
            ('thirteen', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'tabs', ['CompanyWiseCarCount'])

        # Adding model 'Mileage'
        db.create_table(u'tabs_mileage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('costfor25', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('annualcost', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'tabs', ['Mileage'])

        # Adding model 'GasRate'
        db.create_table(u'tabs_gasrate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'tabs', ['GasRate'])

        # Adding model 'GasolineCarCount'
        db.create_table(u'tabs_gasolinecarcount', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('count', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'tabs', ['GasolineCarCount'])


    def backwards(self, orm):
        # Deleting model 'CarCount'
        db.delete_table(u'tabs_carcount')

        # Deleting model 'CompanyWiseCarCount'
        db.delete_table(u'tabs_companywisecarcount')

        # Deleting model 'Mileage'
        db.delete_table(u'tabs_mileage')

        # Deleting model 'GasRate'
        db.delete_table(u'tabs_gasrate')

        # Deleting model 'GasolineCarCount'
        db.delete_table(u'tabs_gasolinecarcount')


    models = {
        u'tabs.carcount': {
            'Meta': {'object_name': 'CarCount'},
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'tabs.companywisecarcount': {
            'CompanyName': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Meta': {'object_name': 'CompanyWiseCarCount'},
            'eleven': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thirteen': ('django.db.models.fields.IntegerField', [], {}),
            'twelve': ('django.db.models.fields.IntegerField', [], {})
        },
        u'tabs.gasolinecarcount': {
            'Meta': {'object_name': 'GasolineCarCount'},
            'count': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        u'tabs.gasrate': {
            'Meta': {'object_name': 'GasRate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'tabs.mileage': {
            'Meta': {'object_name': 'Mileage'},
            'annualcost': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'costfor25': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['tabs']