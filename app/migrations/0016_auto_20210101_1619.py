# Generated by Django 3.1 on 2021-01-01 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_draw_retry_used'),
    ]

    operations = [
        migrations.RenameField(
            model_name='draw',
            old_name='rotation',
            new_name='reel1',
        ),
        migrations.AddField(
            model_name='draw',
            name='reel2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='draw',
            name='reel3',
            field=models.IntegerField(default=0),
        ),
    ]