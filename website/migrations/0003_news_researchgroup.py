# Generated by Django 3.1 on 2020-08-19 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200819_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='researchGroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='News', to='website.researchgroups'),
        ),
    ]