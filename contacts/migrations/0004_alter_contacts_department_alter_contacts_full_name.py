# Generated by Django 4.1.5 on 2023-02-23 11:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_rename_relationship_contacts_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='department',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[A-Z_]*$', 'Only uppercase letters and underscores allowed.')]),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='full_name',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
