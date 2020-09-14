# Generated by Django 3.1 on 2020-08-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_tr', models.CharField(max_length=255, null=True)),
                ('content', models.TextField()),
                ('content_en', models.TextField(null=True)),
                ('content_tr', models.TextField(null=True)),
                ('excerpt', models.TextField()),
                ('excerpt_en', models.TextField(null=True)),
                ('excerpt_tr', models.TextField(null=True)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updateDate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]