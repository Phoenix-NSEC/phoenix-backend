# Generated by Django 4.1.2 on 2022-10-31 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_alter_member_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=254),
        ),
    ]
