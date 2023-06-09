# Generated by Django 4.1.7 on 2023-04-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_auto_20230403_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='lu le'),
        ),
        migrations.AddField(
            model_name='message',
            name='recipient_deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='effacé par destinataire'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender_deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='effacé par expéditeur le'),
        ),
    ]
