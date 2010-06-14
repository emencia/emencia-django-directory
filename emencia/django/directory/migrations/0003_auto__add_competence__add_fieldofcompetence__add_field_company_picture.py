# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Competence'
        db.create_table('directory_competence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255, db_index=True)),
            ('field_of_competence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.FieldOfCompetence'])),
        ))
        db.send_create_signal('directory', ['Competence'])

        # Adding model 'FieldOfCompetence'
        db.create_table('directory_fieldofcompetence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255, db_index=True)),
        ))
        db.send_create_signal('directory', ['FieldOfCompetence'])

        # Adding field 'Company.picture'
        db.add_column('directory_company', 'picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True), keep_default=False)

        # Adding field 'Company.description_additional'
        db.add_column('directory_company', 'description_additional', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Company.phone'
        db.add_column('directory_company', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True), keep_default=False)

        # Adding field 'Company.fax'
        db.add_column('directory_company', 'fax', self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True), keep_default=False)

        # Adding field 'Company.email'
        db.add_column('directory_company', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True), keep_default=False)

        # Adding field 'Company.website'
        db.add_column('directory_company', 'website', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Company.address_1'
        db.add_column('directory_company', 'address_1', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Company.address_2'
        db.add_column('directory_company', 'address_2', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Company.address_comments'
        db.add_column('directory_company', 'address_comments', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Company.postal_code'
        db.add_column('directory_company', 'postal_code', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True), keep_default=False)

        # Adding field 'Company.city'
        db.add_column('directory_company', 'city', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Company.country'
        db.add_column('directory_company', 'country', self.gf('django.db.models.fields.related.ForeignKey')(default='FR', to=orm['countries.Country']), keep_default=False)

        # Adding field 'Company.lat'
        db.add_column('directory_company', 'lat', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True), keep_default=False)

        # Adding field 'Company.lng'
        db.add_column('directory_company', 'lng', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True), keep_default=False)

        # Adding field 'Company.reference'
        db.add_column('directory_company', 'reference', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Company.nature'
        db.add_column('directory_company', 'nature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['directory.Nature'], null=True, blank=True), keep_default=False)

        # Adding field 'Company.tags'
        db.add_column('directory_company', 'tags', self.gf('tagging.fields.TagField')(default=''), keep_default=False)

        # Adding field 'Company.comments'
        db.add_column('directory_company', 'comments', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Company.creation_date'
        db.add_column('directory_company', 'creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2010, 6, 14, 17, 4, 4, 92654), blank=True), keep_default=False)

        # Adding field 'Company.modification_date'
        db.add_column('directory_company', 'modification_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2010, 6, 14, 17, 4, 15, 856756), blank=True), keep_default=False)

        # Adding field 'Company.visible'
        db.add_column('directory_company', 'visible', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True), keep_default=False)

        # Adding M2M table for field categories on 'Company'
        db.create_table('directory_company_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm['directory.company'], null=False)),
            ('category', models.ForeignKey(orm['directory.category'], null=False))
        ))
        db.create_unique('directory_company_categories', ['company_id', 'category_id'])

        # Adding M2M table for field sections on 'Company'
        db.create_table('directory_company_sections', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm['directory.company'], null=False)),
            ('section', models.ForeignKey(orm['directory.section'], null=False))
        ))
        db.create_unique('directory_company_sections', ['company_id', 'section_id'])

        # Changing field 'Company.slug'
        db.alter_column('directory_company', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255))

        # Adding unique constraint on 'Company', fields ['slug']
        db.create_unique('directory_company', ['slug'])

        # Adding field 'Profile.email_alternative'
        db.add_column('directory_profile', 'email_alternative', self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True), keep_default=False)

        # Adding field 'Profile.website'
        db.add_column('directory_profile', 'website', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding M2M table for field competences on 'Profile'
        db.create_table('directory_profile_competences', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('profile', models.ForeignKey(orm['directory.profile'], null=False)),
            ('competence', models.ForeignKey(orm['directory.competence'], null=False))
        ))
        db.create_unique('directory_profile_competences', ['profile_id', 'competence_id'])

        # Changing field 'Profile.picture'
        db.alter_column('directory_profile', 'picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True))

        # Changing field 'Profile.fax'
        db.alter_column('directory_profile', 'fax', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True))

        # Changing field 'Profile.phone'
        db.alter_column('directory_profile', 'phone', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True))

        # Changing field 'Profile.mobile'
        db.alter_column('directory_profile', 'mobile', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True))

        # Changing field 'Category.slug'
        db.alter_column('directory_category', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255))

        # Adding unique constraint on 'Category', fields ['slug']
        db.create_unique('directory_category', ['slug'])

        # Changing field 'Nature.slug'
        db.alter_column('directory_nature', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255))

        # Adding unique constraint on 'Nature', fields ['slug']
        db.create_unique('directory_nature', ['slug'])

        # Changing field 'Section.slug'
        db.alter_column('directory_section', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=255))

        # Adding unique constraint on 'Section', fields ['slug']
        db.create_unique('directory_section', ['slug'])


    def backwards(self, orm):
        
        # Deleting model 'Competence'
        db.delete_table('directory_competence')

        # Deleting model 'FieldOfCompetence'
        db.delete_table('directory_fieldofcompetence')

        # Deleting field 'Company.picture'
        db.delete_column('directory_company', 'picture')

        # Deleting field 'Company.description_additional'
        db.delete_column('directory_company', 'description_additional')

        # Deleting field 'Company.phone'
        db.delete_column('directory_company', 'phone')

        # Deleting field 'Company.fax'
        db.delete_column('directory_company', 'fax')

        # Deleting field 'Company.email'
        db.delete_column('directory_company', 'email')

        # Deleting field 'Company.website'
        db.delete_column('directory_company', 'website')

        # Deleting field 'Company.address_1'
        db.delete_column('directory_company', 'address_1')

        # Deleting field 'Company.address_2'
        db.delete_column('directory_company', 'address_2')

        # Deleting field 'Company.address_comments'
        db.delete_column('directory_company', 'address_comments')

        # Deleting field 'Company.postal_code'
        db.delete_column('directory_company', 'postal_code')

        # Deleting field 'Company.city'
        db.delete_column('directory_company', 'city')

        # Deleting field 'Company.country'
        db.delete_column('directory_company', 'country_id')

        # Deleting field 'Company.lat'
        db.delete_column('directory_company', 'lat')

        # Deleting field 'Company.lng'
        db.delete_column('directory_company', 'lng')

        # Deleting field 'Company.reference'
        db.delete_column('directory_company', 'reference')

        # Deleting field 'Company.nature'
        db.delete_column('directory_company', 'nature_id')

        # Deleting field 'Company.tags'
        db.delete_column('directory_company', 'tags')

        # Deleting field 'Company.comments'
        db.delete_column('directory_company', 'comments')

        # Deleting field 'Company.creation_date'
        db.delete_column('directory_company', 'creation_date')

        # Deleting field 'Company.modification_date'
        db.delete_column('directory_company', 'modification_date')

        # Deleting field 'Company.visible'
        db.delete_column('directory_company', 'visible')

        # Removing M2M table for field categories on 'Company'
        db.delete_table('directory_company_categories')

        # Removing M2M table for field sections on 'Company'
        db.delete_table('directory_company_sections')

        # Changing field 'Company.slug'
        db.alter_column('directory_company', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

        # Removing unique constraint on 'Company', fields ['slug']
        db.delete_unique('directory_company', ['slug'])

        # Deleting field 'Profile.email_alternative'
        db.delete_column('directory_profile', 'email_alternative')

        # Deleting field 'Profile.website'
        db.delete_column('directory_profile', 'website')

        # Removing M2M table for field competences on 'Profile'
        db.delete_table('directory_profile_competences')

        # Changing field 'Profile.picture'
        db.alter_column('directory_profile', 'picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True))

        # Changing field 'Profile.fax'
        db.alter_column('directory_profile', 'fax', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True))

        # Changing field 'Profile.phone'
        db.alter_column('directory_profile', 'phone', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True))

        # Changing field 'Profile.mobile'
        db.alter_column('directory_profile', 'mobile', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True))

        # Changing field 'Category.slug'
        db.alter_column('directory_category', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

        # Removing unique constraint on 'Category', fields ['slug']
        db.delete_unique('directory_category', ['slug'])

        # Changing field 'Nature.slug'
        db.alter_column('directory_nature', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

        # Removing unique constraint on 'Nature', fields ['slug']
        db.delete_unique('directory_nature', ['slug'])

        # Changing field 'Section.slug'
        db.alter_column('directory_section', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

        # Removing unique constraint on 'Section', fields ['slug']
        db.delete_unique('directory_section', ['slug'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
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
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'directory.company': {
            'Meta': {'object_name': 'Company'},
            'address_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address_2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address_comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.Category']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['countries.Country']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_additional': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Nature']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.Section']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'directory.competence': {
            'Meta': {'object_name': 'Competence'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'field_of_competence': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.FieldOfCompetence']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'directory.fieldofcompetence': {
            'Meta': {'object_name': 'FieldOfCompetence'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'directory.nature': {
            'Meta': {'object_name': 'Nature'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'directory.profile': {
            'Meta': {'object_name': 'Profile', '_ormbases': ['auth.User']},
            'address_1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address_2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'address_comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.Category']", 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'civility': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'companies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.Company']", 'null': 'True', 'blank': 'True'}),
            'competences': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.Competence']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['countries.Country']"}),
            'email_alternative': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'fr'", 'max_length': '10', 'blank': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nature': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['directory.Nature']", 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.Section']", 'null': 'True', 'blank': 'True'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'directory.section': {
            'Meta': {'object_name': 'Section'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'directory.workgroup': {
            'Meta': {'object_name': 'WorkGroup'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.Category']", 'null': 'True', 'blank': 'True'}),
            'companies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.Company']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'directory_workgroup_group'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'natures': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.Nature']", 'null': 'True', 'blank': 'True'}),
            'profiles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.Profile']", 'null': 'True', 'blank': 'True'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['directory.Section']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['directory']
