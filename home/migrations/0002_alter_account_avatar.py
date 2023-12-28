# Generated by Django 4.2.7 on 2023-11-26 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, default='/static/images/default-avatar.jpg', max_length=254, null=True, upload_to='upload/avatar/%Y/%m'),
        ),
    ]
