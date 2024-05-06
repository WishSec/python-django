from django import forms
from .models import Jurnal

class JurnalForm(forms.ModelForm):
    class Meta:
        model = Jurnal
        fields = ['id', 'tanggal', 'skp_tahunan', 'jurnal_harian', 'jumlah', 'satuan', 'jam_mulai', 'jam_selesai', 'lampiran', 'nilai', 'komentar', 'tanggal_isi']

class ExcelUploadForm(forms.Form):
    excelFile = forms.FileField(label="Select Excel File", required=True)
