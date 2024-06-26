# Generated by Django 4.1.3 on 2024-04-26 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_project_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='about.skillcategory'),
        ),
    ]
