# Generated by Django 4.2.9 on 2024-01-06 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofile',
            name='belge_yukle',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='profil_onay_durumu',
        ),
        migrations.RemoveField(
            model_name='clientprofile',
            name='uzmanlik_alani',
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='education',
            field=models.CharField(blank=True, choices=[('1', 'İlkokul'), ('2', 'Ortaokul'), ('3', 'Lise'), ('4', 'Üniversite'), ('5', 'Yüksek Lisans'), ('6', 'Doktora')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clientprofile',
            name='location',
            field=models.CharField(blank=True, choices=[('IST', 'İstanbul'), ('ANK', 'Ankara'), ('IZM', 'İzmir'), ('ADN', 'Adana'), ('ANT', 'Antalya'), ('BAL', 'Balıkesir'), ('BRS', 'Bursa'), ('ESK', 'Eskişehir'), ('KOC', 'Kocaeli'), ('KON', 'Konya'), ('MRS', 'Mersin'), ('SIV', 'Sivas'), ('TRB', 'Trabzon'), ('ZNG', 'Zonguldak'), ('OTH', 'Diğer')], max_length=50, null=True),
        ),
    ]
