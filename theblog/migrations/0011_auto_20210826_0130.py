# Generated by Django 2.2 on 2021-08-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_auto_20210825_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='media/images/profile/profile_pic_default', null=True, upload_to='images/profile/'),
        ),
    ]
