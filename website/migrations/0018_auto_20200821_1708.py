# Generated by Django 3.1 on 2020-08-21 14:08

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20200821_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='information',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='information_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='information_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='links',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='pdf',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
