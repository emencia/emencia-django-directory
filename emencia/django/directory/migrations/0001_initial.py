# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('directory_category', (
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('directory', ['Category'])

        # Adding model 'Nature'
        db.create_table('directory_nature', (
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('directory', ['Nature'])

        # Adding model 'Section'
        db.create_table('directory_section', (
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('directory', ['Section'])

        # Adding model 'Company'
        db.create_table('directory_company', (
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('directory', ['Company'])

        # Adding model 'Profile'
        db.create_table('directory_profile', (
            ('reference', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('lng', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('modification_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('nature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Nature'], null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address_comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True, primary_key=True)),
            ('tags', self.gf('tagging.fields.TagField')(default='')),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('language', self.gf('django.db.models.fields.CharField')(default='fr', max_length=10, blank=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['countries.Country'])),
            ('civility', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('address_1', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address_2', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('directory', ['Profile'])

        # Adding M2M table for field sections on 'Profile'
        db.create_table('directory_profile_sections', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['directory.profile'], null=False)),
            ('section', models.ForeignKey(orm['directory.section'], null=False))
        ))
        db.create_unique('directory_profile_sections', ['profile_id', 'section_id'])

        # Adding M2M table for field companies on 'Profile'
        db.create_table('directory_profile_companies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['directory.profile'], null=False)),
            ('company', models.ForeignKey(orm['directory.company'], null=False))
        ))
        db.create_unique('directory_profile_companies', ['profile_id', 'company_id'])

        # Adding M2M table for field categories on 'Profile'
        db.create_table('directory_profile_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['directory.profile'], null=False)),
            ('category', models.ForeignKey(orm['directory.category'], null=False))
        ))
        db.create_unique('directory_profile_categories', ['profile_id', 'category_id'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('directory_category')

        # Deleting model 'Nature'
        db.delete_table('directory_nature')

        # Deleting model 'Section'
        db.delete_table('directory_section')

        # Deleting model 'Company'
        db.delete_table('directory_company')

        # Deleting model 'Profile'
        db.delete_table('directory_profile')

        # Removing M2M table for field sections on 'Profile'
        db.delete_table('directory_profile_sections')

        # Removing M2M table for field companies on 'Profile'
        db.delete_table('directory_profile_companies')

        # Removing M2M table for field categories on 'Profile'
        db.delete_table('directory_profile_categories')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'countries.country': {
            'Meta': {'object_name': 'Country', 'db_table': "'country'"},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'iso3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'numcode': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'printable_name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'directory.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'directory.company': {
            'Meta': {'object_name': 'Company'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'directory.nature': {
            'Meta': {'object_name': 'Nature'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'directory.profile': {
            'Meta': {'object_name': 'Profile', '_ormbases': ['auth.User']},
            'address_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address_2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address_comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.Category']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'civility': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'companies': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.Company']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['countries.Country']"}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'fr'", 'max_length': '10', 'blank': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Nature']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.Section']", 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {'default': "''"}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'})
        },
        'directory.section': {
            'Meta': {'object_name': 'Section'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }
    
    complete_apps = ['directory']
