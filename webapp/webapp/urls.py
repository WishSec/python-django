from django.urls import path
from account import views as account_views
from dashboard import views as dashboard_views
from jurnal import views as jurnal_views
from rekapulasi import views as rekapulasi_views
from history import views as history_views
from login import views as login_views
from logout import views as logout_views
from dashboard.views import custom_permission_denied_view

urlpatterns = [
    path('account/', account_views.account, name='account'),  
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
    path('jurnal/', jurnal_views.jurnal, name='jurnal'),  
    path('rekapulasi/', rekapulasi_views.rekapulasi, name='rekapulasi'), 
    path('history/', history_views.history, name='history'),  
    path('admin/', login_views.user_login, name='admin'),
    path('logout/', logout_views.user_logout, name='logout'),
    path('403-forbidden/', custom_permission_denied_view, name='403-forbidden'),

    # Tambahkan path untuk menambahkan, mengedit, dan menghapus jurnal
    path('add-jurnal/', jurnal_views.add_jurnal, name='add_jurnal'),
    path('edit-jurnal/<int:id>/', jurnal_views.edit_jurnal, name='edit_jurnal'),
    # path('edit-jurnal/<int:id>/', jurnal_views, name='edit_jurnal'),
    path('delete-jurnal/<int:jurnal_id>/', jurnal_views.delete_jurnal, name='delete_jurnal'),
    path('import-jurnal/', jurnal_views.import_jurnal, name='import_jurnal'), 
]
