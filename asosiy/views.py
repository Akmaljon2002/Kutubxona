from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from.forms import *


def bosh_sahifa(request):
    return render(request, 'bosh_sahifa.html')

# 1
class LoginView(View):
    def post(self, request):
        user = authenticate(
            username = request.POST.get('l'),
            password = request.POST.get('p')
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/home/")
    def get(self, request):
        return render(request, 'login.html')



class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")
#
class RegisterView(View):
    def post(self, request):
        if request.POST.get('p') == request.POST.get('cp'):
            User.objects.create_user(
                username = request.POST.get('l'),
                password = request.POST.get('p')
            )
        return redirect("/")
    def get(self, request):
        return render(request, 'register.html')
########################################################################################################################
def talabalar(request):
    if request.method == "POST":
        forma = TalabaForm(request.POST)
        if forma.is_valid():
            Talaba.objects.create(
                ism = forma.cleaned_data.get('name'),
                kurs = forma.cleaned_data.get('course'),
                kitob_soni = forma.cleaned_data.get('nums_of_books'),
                bitiruvchi = forma.cleaned_data.get('senior')
            )
        return redirect("/talabalar/")
    soz = request.GET.get('talaba_qidirish')
    if soz is None:
        tb = Talaba.objects.all()
    else:
        tb = Talaba.objects.filter(ism__contains=soz)
    data = {
        "talabalar":tb,
        "forma":TalabaForm()
    }
    return render(request, "talabalar.html", data)

#
def mualliflar(request):
    if request.method == "POST":
        form = MuallifForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/mualliflar/")
    soz = request.GET.get('muallif_qidirish')
    if soz is None:
        mf = Muallif.objects.all()
    else:
        mf = Muallif.objects.filter(ism__contains=soz)
    data = {
        'mualliflar':mf,
        "muallif":MuallifForm
    }
    return render(request, 'mualliflar.html', data)


def kitoblar(request):
    if request.method == "POST":
        form = KitobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/kitoblar/')
    soz = request.GET.get('kitob_qidirish')
    if soz is None:
        kitob = Kitob.objects.all()
    else:
        kitob = Kitob.objects.filter(nom__contains=soz)
    data = {
        'kitoblar':kitob,
        'mualliflar':Muallif.objects.all(),
        'kitob':KitobForm()
    }
    return render(request, 'kitoblar.html', data)

#
def recordlar(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = RecordForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("/recordlar/")
        soz = request.GET.get('record_qidirish')
        if soz is None:
            record = Record.objects.all()
        else:
            record = Record.objects.filter(talaba__ism__contains=soz)
        data = {
            "recordlar":record,
            "talabalar":Talaba.objects.all(),
            "kitoblar":Kitob.objects.all(),
            "adminlar":Admin.objects.all(),
            "record":RecordForm()
        }
        return render(request, 'recordlar.html', data)
    return redirect("/home/")

# 3
def adminlar(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/adminlar/")
    soz = request.GET.get('admin_qidirish')
    if soz is None:
        admin = Admin.objects.all()
    else:
        admin = Admin.objects.filter(ism__contains=soz)
    data = {
        "adminlar":admin,
        "admin":AdminForm()
    }
    return render(request, 'adminlar.html', data)

########################################################################################################################

def talaba(request, son):
    if request.method == "POST":
        if request.POST.get('b') == 'on':
            qiymat = True
        else:
            qiymat = False
        Talaba.objects.filter(id=son).update(
            ism = request.POST.get('i'),
            kurs = request.POST.get('k'),
            kitob_soni = request.POST.get('k_s'),
            bitiruvchi = qiymat
        )
        return redirect("/talabalar/")
    data = {
        "talaba": Talaba.objects.get(id=son)
    }
    return render(request, 'talaba.html', data)

# 2
def muallif(request, son):
    if request.method == "POST":
        if request.POST.get('t') == 'on':
            qiymat = True
        else:
            qiymat = False
        Muallif.objects.filter(id=son).update(
            ism = request.POST.get('i'),
            tugilgan_yili = request.POST.get('t_y'),
            kitob_soni = request.POST.get('k_s'),
            tirik = qiymat,
            jins = request.POST.get('j')
        )
        return redirect("/mualliflar/")
    data = {
        "muallif":Muallif.objects.get(id=son),
        "jins":["Erkak", "Ayol"]
    }
    return render(request, 'muallif.html', data)
#

def kitob(request, son):
    if request.method == "POST":
        Kitob.objects.filter(id=son).update(
            nom = request.POST.get('n'),
            sahifa = request.POST.get('s'),
            janr = request.POST.get('janr'),
            muallif = Muallif.objects.get(id=request.POST.get('muallif'))
        )
        return redirect("/kitoblar/")
    data = {
        "kitob":Kitob.objects.get(id=son),
        "muallif":Muallif.objects.all()
    }
    return render(request, 'kitob.html', data)

# 3
def record(request, son):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST.get('q') == 'on':
                qiymat = True
            else:
                qiymat = False
            Record.objects.filter(id=son).update(
                qaytardi = qiymat,
                qaytargan_sana = request.POST.get('q_sana')
            )
            return redirect("/recordlar/")
        data = {
            "record":Record.objects.get(id=son)
        }
        return render(request, 'record.html', data)
    return redirect("/home")

#
def admins(request, son):
    if request.method == "POST":
        Admin.objects.filter(id=son).update(
            ism = request.POST.get('i'),
            ish_vaqti = request.POST.get('i_v')
        )
        return redirect("/adminlar/")
    data = {
        "admin":Admin.objects.get(id=son),
        "ish_vaqtlari":["8:00 - 14:00", "14:00 - 16:00", "16:00 - 19:00"]
    }
    return render(request, 'admin.html', data)

########################################################################################################################
def talaba_ochirish(request, son):
    talaba = Talaba.objects.get(id=son)
    talaba.delete()

    return redirect( '/talabalar/')

def muallif_ochirish(request, son):
    muallif = Muallif.objects.get(id=son)
    muallif.delete()

    return redirect('/mualliflar/')
def kitob_ochirish(request, son):
    kitob = Kitob.objects.get(id=son)
    kitob.delete()

    return redirect('/kitoblar/')

def record_ochirish(request, son):
    if request.user.is_authenticated:
        record = Record.objects.get(id=son)
        record.delete()

        return redirect('/recordlar/')
    return redirect("/")

def admin_ochirish(request, son):
    admin = Admin.objects.get(id=son)
    admin.delete()

    return redirect('/adminlar/')

########################################################################################################################




