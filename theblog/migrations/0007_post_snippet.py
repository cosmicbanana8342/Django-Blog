# Generated by Django 2.2 on 2021-07-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20210708_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click the link above to read blog post', max_length=255),
        ),
    ]
