from django.db import models
class Muallif(models.Model):
    Jins = [
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol')
    ]
    ism = models.CharField(max_length=50)
    tugilgan_yili = models.DateField()
    tirik = models.BooleanField(default=True)
    kitob_soni = models.SmallIntegerField()
    jins = models.CharField(max_length=10, choices=Jins)
    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=100)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=30, choices=[
        ("Badiiy", "Badiiy"),
        ("Ilmiy", "Ilmiy"),
        ("Hujjatli", "Hujjatli")
    ])
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    kurs = models.PositiveSmallIntegerField()
    bitiruvchi = models.BooleanField(default=False)
    def __str__(self):
        return self.ism

class Admin(models.Model):
    ish_v = [("8:00 - 14:00", "8:00 - 14:00"), ("14:00 - 16:00","14:00 - 16:00"), ("16:00 - 19:00", "16:00 - 19:00")]
    ism = models.CharField(max_length=30)
    ish_vaqti = models.CharField(max_length=30, choices=ish_v)
    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytardi = models.BooleanField(default=False)
    qaytargan_sana = models.DateField(blank=True, null=True)
    def __str__(self):
        return f"{self.talaba} ({self.kitob})"