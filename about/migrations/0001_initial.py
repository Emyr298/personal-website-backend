# Generated by Django 4.1.3 on 2022-11-18 15:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image_url', models.URLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(max_length=20)),
                ('platform_image_url', models.URLField(default='')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image_url', models.URLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('level', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='ProjectUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('url', models.URLField(default='')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.project')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=20)),
                ('affiliation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.affiliation')),
                ('skills', models.ManyToManyField(to='about.skill')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=20, null=True)),
                ('field', models.CharField(max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('affiliation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.affiliation')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('credential_id', models.CharField(max_length=30)),
                ('affiliation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.affiliation')),
            ],
        ),
    ]
