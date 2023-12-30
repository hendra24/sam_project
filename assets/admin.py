from django.contrib import admin
from .models import Gardu, Rtu, Rectifier, Media, FaultIndicator, Up3
# Register your models here.

class GarduAdmin(admin.ModelAdmin):
    list_display = ('gardu_name', 'up3', 'rc_status', 'date_added', 'date_modified')
    readonly_fields = ('date_added', 'date_modified')
    
class RtuAdmin(admin.ModelAdmin):
    list_display = ('gardu', 'brand_rtu', 'model_rtu','date_added', 'date_modified')
    readonly_fields = ('date_added', 'date_modified')
    
class RectifierAdmin(admin.ModelAdmin):
    list_display = ('gardu', 'brand_recti', 'model_recti', 'jumlah_baterai','date_added', 'date_modified')
    readonly_fields = ('date_added', 'date_modified')
    
class MediaAdmin(admin.ModelAdmin):
    list_display = ('gardu', 'brand_media', 'model_media','date_added', 'date_modified')
    readonly_fields = ('date_added', 'date_modified')
    
class FaultIndicatorAdmin(admin.ModelAdmin):
    list_display = ('gardu', 'brand_fi', 'model_fi','date_added', 'date_modified')
    readonly_fields = ('date_added', 'date_modified')
    
class Up3Admin(admin.ModelAdmin):
    list_display = ('up3', 'wilayah_kerja','date_added', 'date_modified')
    readonly_fields = ('date_added', 'date_modified')

admin.site.register(Gardu, GarduAdmin)
admin.site.register(Rtu, RtuAdmin)
admin.site.register(Rectifier, RectifierAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(FaultIndicator, FaultIndicatorAdmin)
admin.site.register(Up3, Up3Admin)