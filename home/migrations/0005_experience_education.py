# Generated by Django 4.0.5 on 2024-01-17 23:59

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_about2_homepage_education_homepage_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('position', models.CharField(max_length=96)),
                ('provider', models.CharField(max_length=96)),
                ('description_j', wagtail.fields.RichTextField(blank=True, null=True)),
                ('start_date_d', models.DateTimeField(verbose_name='Start date')),
                ('finished_date_d', models.DateTimeField(verbose_name='Finished date')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('degree', models.CharField(max_length=96)),
                ('university', models.CharField(max_length=96)),
                ('description_u', wagtail.fields.RichTextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(verbose_name='Start date')),
                ('finished_date_e', models.DateTimeField(verbose_name='Finished date')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='studies', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
