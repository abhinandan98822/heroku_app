# Generated by Django 3.2.12 on 2022-06-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_alter_assesment_qutient'),
    ]

    operations = [
        migrations.AddField(
            model_name='assesment',
            name='test_admin',
            field=models.CharField(blank=True, choices=[('DST', 'DST'), ('VSMS', 'VSMS'), ('MISIC', 'MISIC')], max_length=100, null=True),
        ),
    ]