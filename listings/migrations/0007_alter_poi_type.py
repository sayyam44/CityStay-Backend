# Generated by Django 5.1.4 on 2025-01-15 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_poi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poi',
            name='type',
            field=models.CharField(choices=[('University', 'University'), ('Hospital', 'Hospital'), ('Stadium', 'Stadium'), ('Mall', 'Mall'), ('College', 'College')], max_length=50),
        ),
    ]
