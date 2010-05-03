# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'WorkGroup'
        db.create_table('directory_workgroup', (
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='directory_workgroup_group', to=orm['auth.Group'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('directory', ['WorkGroup'])

        # Adding M2M table for field companies on 'WorkGroup'
        db.create_table('directory_workgroup_companies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workgroup', models.ForeignKey(orm['directory.workgroup'], null=False)),
            ('company', models.ForeignKey(orm['directory.company'], null=False))
        ))
        db.create_unique('directory_workgroup_companies', ['workgroup_id', 'company_id'])

        # Adding M2M table for field sections on 'WorkGroup'
        db.create_table('directory_workgroup_sections', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workgroup', models.ForeignKey(orm['directory.workgroup'], null=False)),
            ('section', models.ForeignKey(orm['directory.section'], null=False))
        ))
        db.create_unique('directory_workgroup_sections', ['workgroup_id', 'section_id'])

        # Adding M2M table for field profiles on 'WorkGroup'
        db.create_table('directory_workgroup_profiles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workgroup', models.ForeignKey(orm['directory.workgroup'], null=False)),
            ('profile', models.ForeignKey(orm['directory.profile'], null=False))
        ))
        db.create_unique('directory_workgroup_profiles', ['workgroup_id', 'profile_id'])

        # Adding M2M table for field categories on 'WorkGroup'
        db.create_table('directory_workgroup_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workgroup', models.ForeignKey(orm['directory.workgroup'], null=False)),
            ('category', models.ForeignKey(orm['directory.category'], null=False))
        ))
        db.create_unique('directory_workgroup_categories', ['workgroup_id', 'category_id'])

        # Adding M2M table for field natures on 'WorkGroup'
        db.create_table('directory_workgroup_natures', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workgroup', models.ForeignKey(orm['directory.workgroup'], null=False)),
            ('nature', models.ForeignKey(orm['directory.nature'], null=False))
        ))
        db.create_unique('directory_workgroup_natures', ['workgroup_id', 'nature_id'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'WorkGroup'
        db.delete_table('directory_workgroup')

        # Removing M2M table for field companies on 'WorkGroup'
        db.delete_table('directory_workgroup_companies')

        # Removing M2M table for field sections on 'WorkGroup'
        db.delete_table('directory_workgroup_sections')

        # Removing M2M table for field profiles on 'WorkGroup'
        db.delete_table('directory_workgroup_profiles')

        # Removing M2M table for field categories on 'WorkGroup'
        db.delete_table('directory_workgroup_categories')

        # Removing M2M table for field natures on 'WorkGroup'
        db.delete_table('directory_workgroup_natures')
    
    
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
        },
        'directory.workgroup': {
            'Meta': {'object_name': 'WorkGroup'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.Category']", 'null': 'True', 'blank': 'True'}),
            'companies': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.Company']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'directory_workgroup_group'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'natures': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.Nature']", 'null': 'True', 'blank': 'True'}),
            'profiles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.Profile']", 'null': 'True', 'blank': 'True'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['directory.Section']", 'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['directory']
