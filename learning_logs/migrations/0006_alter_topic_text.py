# Generated by Django 4.1.1 on 2022-10-11 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_alter_entry_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
