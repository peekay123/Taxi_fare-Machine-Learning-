# Generated by Django 4.1.3 on 2022-12-02 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tppApp', '0002_feedback_alter_predresults_from_source_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]