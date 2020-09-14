# Generated by Django 3.1 on 2020-08-20 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0008_news_draft'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-createDate']},
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='News', to=settings.AUTH_USER_MODEL),
        ),
    ]