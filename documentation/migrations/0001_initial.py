# Generated by Django 5.1.5 on 2025-01-31 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(verbose_name='Data di Emissione')),
                ('expiration_date', models.DateField(verbose_name='Data di Scadenza')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='medical_certificates', to='profiles.athlete', verbose_name='Atleta')),
                ('sport_doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='certificates', to='profiles.sportdoctor', verbose_name='Medico')),
            ],
            options={
                'verbose_name': 'Certificato Medico Sportivo',
                'verbose_name_plural': 'Certificati Medico Sportivi',
            },
        ),
    ]
