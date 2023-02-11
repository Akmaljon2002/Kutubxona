from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bosh_sahifa),

    path('talabalar/', talabalar),
    path('mualliflar/', mualliflar),
    path('kitoblar/', kitoblar),
    path('recordlar/', recordlar),
    path('adminlar/', adminlar),

    path('talaba/<int:son>/', talaba), # talaba/5/
    path('muallif/<int:son>/', muallif),
    path('kitob/<int:son>/', kitob),
    path('record/<int:son>/', record),
    path('admins/<int:son>/', admins),

    path('talaba_ochirish/<int:son>/', talaba_ochirish),
    path('record_ochirish/<int:son>/', record_ochirish),
    path('muallif_ochirish/<int:son>/', muallif_ochirish),
    path('kitob_ochirish/<int:son>/', kitob_ochirish),
    path('admin_ochirish/<int:son>/', admin_ochirish),


]
