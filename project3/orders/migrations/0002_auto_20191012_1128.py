# Generated by Django 2.2.5 on 2019-10-12 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('category', 'name', 'size')},
        ),
    ]
