from django.db import models
from accounts.models import Company

# Create your models here.
class Gardu(models.Model):
    gardu_name = models.CharField(max_length=100)
    long = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    up3 = models.ForeignKey('Up3', on_delete=models.SET_NULL,null=True, blank=True)
    rc_status = models.BooleanField(default=False)
    
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.gardu_name
    
class Rtu(models.Model):
    gardu = models.ForeignKey('Gardu', on_delete=models.SET_NULL, null=True, blank=True) 
    serial_number_rtu = models.CharField(max_length=50, null=True, blank=True)
    brand_rtu = models.CharField(max_length=50, null=True, blank=True)
    model_rtu = models.CharField(max_length=50, null=True, blank=True)
    rtu_status = models.BooleanField(default=False) #RTU STATUS AKTIF/TIDAK AKTIF
    note = models.TextField(null=True, blank=True) 
    
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
       
    def __unicode__(self):
        return self.gardu
    
class Rectifier(models.Model):
    gardu = models.ForeignKey('Gardu', on_delete=models.SET_NULL, null=True, blank=True) 
    serial_number_recti = models.CharField(max_length=50, null=True, blank=True)
    brand_recti = models.CharField(max_length=50, null=True, blank=True)
    model_recti = models.CharField(max_length=50, null=True, blank=True)
    recti_status = models.BooleanField(default=False) #RECTI AKTIF / TIDAK 
    brand_baterai = models.CharField(max_length=50, null=True, blank=True)
    type_baterai = models.CharField(max_length=50, null=True, blank=True)
    jumlah_baterai = models.IntegerField(default=0)
    note = models.TextField(null=True, blank=True)
    
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.gardu

class FaultIndicator(models.Model):
    gardu = models.ForeignKey('Gardu', on_delete=models.SET_NULL, null=True, blank=True) 
    serial_number_fi = models.CharField(max_length=50, null=True, blank=True)
    brand_fi = models.CharField(max_length=50, null=True, blank=True)
    model_fi = models.CharField(max_length=50, null=True, blank=True)
    fi_status = models.BooleanField(default=False) #FI AKTIF / TIDAK 
    brand_ct = models.CharField(max_length=50, null=True, blank=True)
    model_ct = models.CharField(max_length=50, null=True, blank=True)
    ct_status = models.BooleanField(default=False) #CT AKTIF / TIDAK 
    note = models.TextField(null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.gardu
    
class Media(models.Model):
    gardu = models.ForeignKey('Gardu', on_delete=models.SET_NULL, null=True, blank=True) 
    serial_number_media = models.CharField(max_length=50, null=True, blank=True)
    brand_media = models.CharField(max_length=50, null=True, blank=True)
    model_media = models.CharField(max_length=50, null=True, blank=True)
    media_status = models.BooleanField(default=False) #FI AKTIF / TIDAK 
    protokol = models.CharField(max_length=50, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.gardu

class Up3(models.Model):
    up3 = models.CharField(max_length=50, unique=True)
    wilayah_kerja = models.CharField(max_length=50, null=True, blank=True)
    
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.up3
    
    class Meta:
            verbose_name = 'UP3'
            verbose_name_plural = 'UP3'
    
    
    