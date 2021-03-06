# Generated by Django 3.2 on 2022-03-31 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='BlogSystem.Tag'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tags',
            field=models.ManyToManyField(blank=True, to='BlogSystem.Tag'),
        ),
    ]
