# Generated by Django 3.2.10 on 2022-12-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_post_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ip',
            field=models.GenericIPAddressField(blank=True, editable=False, null=True),
        ),
    ]
