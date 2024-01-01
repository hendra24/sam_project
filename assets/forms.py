from django import forms
from .models import Gardu, Rectifier, Media, Rtu, FaultIndicator, Up3
from django.core.exceptions import ValidationError


#example custom widget unused
class MaskedBooleanWidget(forms.CheckboxInput):
    def render(self, name, value, attrs=None, renderer=None):
        if value is True:
            html = super().render(name, value, attrs, renderer)
            html += '<span style="color: green;"> Active</span>'
        else:
            html = super().render(name, value, attrs, renderer)
            html += '<span style="color: red;"> Inactive</span>'
        return html

class GarduForm(forms.ModelForm):
    up3 = forms.ModelChoiceField(queryset=Up3.objects.all(), empty_label="PILIH UP3",widget=forms.Select, 
                                         required=False, to_field_name="up3")
    rc_status = forms.TypedChoiceField(
        coerce=lambda x: bool(int(x)),
        choices=((1, 'Aktif'), (0, 'Tidak Aktif')),
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=0  # Set the initial value (0 or 1)
    )
    
    class Meta:
        model = Gardu
        fields = ['gardu_name', 'up3', 'long', 'lat', 'rc_status']
        
    def __init__(self, *args, **kwargs):
        super(GarduForm, self).__init__(*args, **kwargs)
        self.fields['gardu_name'].widget.attrs['class'] = 'form-control'
        self.fields['up3'].widget.attrs['class'] = 'form-select'
        self.fields['long'].widget.attrs['class'] = 'form-control'
        self.fields['lat'].widget.attrs['class'] = 'form-control'
        
class EditGarduForm(forms.ModelForm):
    up3 = forms.ModelChoiceField(queryset=Up3.objects.all(), empty_label="PILIH UP3",widget=forms.Select, 
                                         required=False, to_field_name="up3")
    rc_status = forms.TypedChoiceField(
        coerce=lambda x: bool(int(x)),
        choices=((0, 'Tidak Aktif'),(1, 'Aktif')),
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=0  # Set the initial value (0 or 1)
    )
    
    class Meta:
        model = Gardu
        fields = ['gardu_name', 'up3', 'long', 'lat', 'rc_status']
        
    def __init__(self, *args, **kwargs):
        super(EditGarduForm, self).__init__(*args, **kwargs)
        self.fields['gardu_name'].widget.attrs['class'] = 'form-control'
        self.fields['up3'].widget.attrs['class'] = 'form-select'
        self.fields['long'].widget.attrs['class'] = 'form-control'
        self.fields['lat'].widget.attrs['class'] = 'form-control'

class RtuForm(forms.ModelForm):
    gardu = forms.ModelChoiceField(queryset=Gardu.objects.all(), empty_label="PILIH GARDU",widget=forms.Select, 
                                         required=False, to_field_name="gardu_name")
    rtu_status = forms.TypedChoiceField(
        coerce=lambda x: bool(int(x)),
        choices=((1, 'Aktif'), (0, 'Tidak Aktif')),
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=0  # Set the initial value (0 or 1)
    )
    
    class Meta:
        model = Rtu
        fields = ['gardu', 'serial_number_rtu', 'brand_rtu', 'model_rtu', 'rtu_status', 'note']
        
    def __init__(self, *args, **kwargs):
        super(RtuForm, self).__init__(*args, **kwargs)
        self.fields['gardu'].widget.attrs['class'] = 'form-select'
        self.fields['serial_number_rtu'].widget.attrs['class'] = 'form-control'
        self.fields['brand_rtu'].widget.attrs['class'] = 'form-control'
        self.fields['model_rtu'].widget.attrs['class'] = 'form-control'
        self.fields['note'].widget.attrs['class'] = 'form-control'
        
class RectifierForm(forms.ModelForm):
    gardu = forms.ModelChoiceField(queryset=Gardu.objects.all(), empty_label="PILIH GARDU",widget=forms.Select, 
                                         required=False, to_field_name="gardu_name")
    recti_status = forms.TypedChoiceField(
        coerce=lambda x: bool(int(x)),
        choices=((1, 'Aktif'), (0, 'Tidak Aktif')),
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=0  # Set the initial value (0 or 1)
    )
    
    class Meta:
        model = Rectifier
        fields = ['gardu', 'serial_number_recti', 'brand_recti', 'model_recti', 'recti_status', 'brand_baterai', 'type_baterai', 'jumlah_baterai','note']
        
    def __init__(self, *args, **kwargs):
        super(RectifierForm, self).__init__(*args, **kwargs)
        self.fields['gardu'].widget.attrs['class'] = 'form-select'
        self.fields['serial_number_recti'].widget.attrs['class'] = 'form-control'
        self.fields['brand_recti'].widget.attrs['class'] = 'form-control'
        self.fields['model_recti'].widget.attrs['class'] = 'form-control'
        self.fields['brand_baterai'].widget.attrs['class'] = 'form-control'
        self.fields['type_baterai'].widget.attrs['class'] = 'form-control'
        self.fields['jumlah_baterai'].widget.attrs['class'] = 'form-control'
        self.fields['note'].widget.attrs['class'] = 'form-control'
        
class MediaForm(forms.ModelForm):
    gardu = forms.ModelChoiceField(queryset=Gardu.objects.all(), empty_label="PILIH GARDU",widget=forms.Select, 
                                         required=False, to_field_name="gardu_name")
    media_status = forms.TypedChoiceField(
        coerce=lambda x: bool(int(x)),
        choices=((1, 'Aktif'), (0, 'Tidak Aktif')),
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=0  # Set the initial value (0 or 1)
    )
    
    class Meta:
        model = Media
        fields = ['gardu', 'serial_number_media', 'brand_media', 'model_media', 'protokol','media_status','note']
    
    def __init__(self, *args, **kwargs):
        super(MediaForm, self).__init__(*args, **kwargs)
        self.fields['gardu'].widget.attrs['class'] = 'form-select'
        self.fields['serial_number_media'].widget.attrs['class'] = 'form-control'
        self.fields['brand_media'].widget.attrs['class'] = 'form-control'
        self.fields['model_media'].widget.attrs['class'] = 'form-control'
        self.fields['protokol'].widget.attrs['class'] = 'form-control'
        self.fields['note'].widget.attrs['class'] = 'form-control'

class FaultIndicatorForm(forms.ModelForm):
    gardu = forms.ModelChoiceField(queryset=Gardu.objects.all(), empty_label="PILIH GARDU",widget=forms.Select, 
                                         required=False, to_field_name="gardu_name")
    fi_status = forms.TypedChoiceField(
        coerce=lambda x: bool(int(x)),
        choices=((1, 'Aktif'), (0, 'Tidak Aktif')),
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=0  # Set the initial value (0 or 1)
    )
    
    ct_status = forms.TypedChoiceField(
        coerce=lambda x: bool(int(x)),
        choices=((1, 'Aktif'), (0, 'Tidak Aktif')),
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=0  # Set the initial value (0 or 1)
    )
    
    class Meta:
        model = FaultIndicator
        fields = ['gardu', 'serial_number_fi', 'brand_fi', 'model_fi', 'fi_status','brand_ct','model_ct','ct_status','note']
    
    def __init__(self, *args, **kwargs):
        super(FaultIndicatorForm, self).__init__(*args, **kwargs)
        self.fields['gardu'].widget.attrs['class'] = 'form-select'
        self.fields['serial_number_fi'].widget.attrs['class'] = 'form-control'
        self.fields['brand_fi'].widget.attrs['class'] = 'form-control'
        self.fields['model_fi'].widget.attrs['class'] = 'form-control'
        self.fields['brand_ct'].widget.attrs['class'] = 'form-control'
        self.fields['model_ct'].widget.attrs['class'] = 'form-control'
        self.fields['note'].widget.attrs['class'] = 'form-control'
       
