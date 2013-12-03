# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GrowthPerYear'
        db.create_table(u'tabs_growthperyear', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('count', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'tabs', ['GrowthPerYear'])

        # Adding model 'ElectricitySources'
        db.create_table(u'tabs_electricitysources', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('percentage', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'tabs', ['ElectricitySources'])


    def backwards(self, orm):
        # Deleting model 'GrowthPerYear'
        db.delete_table(u'tabs_growthperyear')

        # Deleting model 'ElectricitySources'
        db.delete_table(u'tabs_electricitysources')


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
        u'tabs.electricitysources': {
            'Meta': {'object_name': 'ElectricitySources'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.FloatField', [], {}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        u'tabs.growthperyear': {
            'Meta': {'object_name': 'GrowthPerYear'},
            'count': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
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