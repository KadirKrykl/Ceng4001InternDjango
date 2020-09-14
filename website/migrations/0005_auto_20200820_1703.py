# Generated by Django 3.1 on 2020-08-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchgroups',
            name='slug',
            field=models.SlugField(default='empty', editable=False, max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='researchgroups',
            name='title',
            field=models.CharField(max_length=245),
        ),
        migrations.AlterField(
            model_name='researchgroups',
            name='title_en',
            field=models.CharField(max_length=245, null=True),
        ),
        migrations.AlterField(
            model_name='researchgroups',
            name='title_tr',
            field=models.CharField(max_length=245, null=True),
        ),
    ]