from django.shortcuts import render


def auth(request):
    return render(request, 'authorization/auth_page/auth.html')


def reg(request):
    return render(request, 'authorization/reg_page/reg.html')
