from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import JurnalForm, ExcelUploadForm
from .models import Jurnal
import pandas as pd

def jurnal(request):
    jurnals = Jurnal.objects.all()
    return render(request, 'jurnal.html', {'jurnals': jurnals})

def add_jurnal(request):
    if request.method == 'POST':
        form = JurnalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jurnal')
    else:
        form = JurnalForm()
    return render(request, 'jurnal.html', {'form': form})

# def edit_jurnal(request, id):
#     jurnal = get_object_or_404(Jurnal, id=id)
#     form = JurnalForm(instance=jurnal)
#     return render(request, 'jurnal.html', {'jurnal': form})

def edit_jurnal(request, id):  
    jurnal = Jurnal.objects.get(id=id)  
    return render(request,'jurnal.html', {'jurnal':jurnal})  


def delete_jurnal(request, jurnal_id):
    jurnal = get_object_or_404(Jurnal, pk=jurnal_id)
    if request.method == 'POST':
        jurnal.delete()
        return redirect('jurnal')  # Redirect ke halaman dashboard setelah berhasil menghapus jurnal
    return render(request, 'jurnal.html', {'jurnal': jurnal})

def import_jurnal(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['excelFile']
            if excel_file.name.endswith('.xlsx'):
                df = pd.read_excel(excel_file)
                # Lakukan proses import data dari DataFrame 'df'
                jurnal_data = []
                for index, row in df.iterrows():
                    jurnal = Jurnal(
                        tanggal=row['tanggal'],
                        skp_tahunan=row['skp_tahunan'],
                        jurnal_harian=row['jurnal_harian'],
                        jumlah=row['jumlah'],
                        satuan=row['satuan'],
                        jam_mulai=row['jam_mulai'],
                        jam_selesai=row['jam_selesai'],
                        nilai=row['nilai'],
                        komentar=row['komentar'],
                        tanggal_isi=row['tanggal_isi']
                    )
                    jurnal_data.append(jurnal)
                
                # Simpan data ke dalam model Jurnal menggunakan bulk_create
                Jurnal.objects.bulk_create(jurnal_data)

                return HttpResponseRedirect('/jurnal/')  # Redirect ke halaman dashboard setelah import berhasil
            else:
                form.add_error('excelFile', 'Format file harus .xlsx')
    else:
        form = ExcelUploadForm()
    return render(request, 'jurnal.html', {'form': form})
