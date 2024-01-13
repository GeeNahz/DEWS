# Generated by Django 4.2.6 on 2024-01-10 19:05

from django.db import migrations, models
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('temperature', models.FloatField(db_index=True)),
                ('humidity', models.FloatField(db_index=True)),
                ('precipitation', models.FloatField(db_index=True)),
                ('soil_moisture', models.FloatField(db_index=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
