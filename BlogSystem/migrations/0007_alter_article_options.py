# Generated by Django 3.2 on 2022-03-31 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogSystem', '0006_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('created',)},
        ),
    ]
