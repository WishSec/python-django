from django.db import models

class Jurnal(models.Model):
    id = models.AutoField(primary_key=True)
    tanggal = models.DateField()
    skp_tahunan = models.CharField(max_length=100)
    jurnal_harian = models.CharField(max_length=100)
    jumlah = models.IntegerField()
    satuan = models.CharField(max_length=50)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    lampiran = models.FileField(upload_to='lampiran/')
    nilai = models.DecimalField(max_digits=5, decimal_places=2)
    komentar = models.TextField(blank=True, null=True)
    tanggal_isi = models.DateField() 

    class Meta:
        db_table = "jurnal_harian"
