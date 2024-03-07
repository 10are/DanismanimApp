# Generated by Django 4.2.9 on 2024-03-07 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, choices=[('IST', 'İstanbul'), ('ANK', 'Ankara'), ('IZM', 'İzmir'), ('ADN', 'Adana'), ('ANT', 'Antalya'), ('BAL', 'Balıkesir'), ('BRS', 'Bursa'), ('ESK', 'Eskişehir'), ('KOC', 'Kocaeli'), ('KON', 'Konya'), ('MRS', 'Mersin'), ('SIV', 'Sivas'), ('TRB', 'Trabzon'), ('ZNG', 'Zonguldak'), ('OTH', 'Diğer')], max_length=50, null=True)),
                ('education', models.CharField(blank=True, choices=[('1', 'İlkokul'), ('2', 'Ortaokul'), ('3', 'Lise'), ('4', 'Üniversite'), ('5', 'Yüksek Lisans'), ('6', 'Doktora')], max_length=50, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
