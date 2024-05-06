from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)
    # Redirect to a page after logout, for example, the login page
    return redirect('admin')
