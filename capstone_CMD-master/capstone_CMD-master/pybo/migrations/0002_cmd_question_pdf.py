# Generated by Django 3.1.7 on 2021-06-07 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmd_question',
            name='pdf',
            field=models.FileField(default=1, upload_to='books/pdfs/'),
            preserve_default=False,
        ),
    ]
