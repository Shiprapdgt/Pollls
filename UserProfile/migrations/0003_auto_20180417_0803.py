# Generated by Django 2.0.3 on 2018-04-17 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0002_auto_20180417_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='key',
            field=models.CharField(max_length=100),
        ),
    ]
