from django.shortcuts import render, redirect
from .models import Gardu, Rtu, Rectifier, FaultIndicator, Media
from django.shortcuts import get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import GarduForm, EditGarduForm, RtuForm, RectifierForm, MediaForm, FaultIndicatorForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
import logging
# Create your views here.

#GARDU VIEW HANDLER
def all_gardu(request):
    gardus = Gardu.objects.all().order_by('gardu_name')
    paginator = Paginator(gardus, 50)
    page= request.GET.get('page')
    paged_gardus = paginator.get_page(page)
    jumlah = gardus.count()
    context = {
        'gardus' : paged_gardus,
        'jumlah' : jumlah,
    }
    return render(request, 'assets/all_gardu.html', context)

def create_gardu(request):
    if request.method == 'POST':
        form = GarduForm(request.POST)
        if form.is_valid():
            gardu_name = form.cleaned_data['gardu_name']
            up3 = form.cleaned_data['up3']
            long = form.cleaned_data['long']
            lat = form.cleaned_data['lat']
            rc_status = form.cleaned_data['rc_status']
            gardu = Gardu.objects.create(gardu_name=gardu_name, up3=up3, long=long, lat=lat, rc_status=rc_status)
            gardu.save()
            messages.success(request, 'Gardu berhasil di buat !!')
            return redirect('all_gardu')
        else:
            messages.warning(request, form.errors)
            return redirect('create_gardu')
    else:
      form = GarduForm()  
    return render(request, 'assets/create_gardu.html', {'form': form})



def detail_gardu(request, gardu_name):
    gardu = get_object_or_404(Gardu, gardu_name=gardu_name)
    return render(request, 'assets/gardu_detail.html', {'gardu' : gardu })

def edit_gardu(request, id):
    gardu = get_object_or_404(Gardu, id=id)
   
    form = GarduForm(initial={'gardu_name': gardu.gardu_name, 'up3' : gardu.up3, 'long': gardu.long, 'lat': gardu.lat, 'rc_status': int(gardu.rc_status)})
    if request.method == 'POST':
        form = GarduForm(request.POST)
        if form.is_valid():
            gardu_name = form.cleaned_data['gardu_name']
            up3 = form.cleaned_data['up3']
            long = form.cleaned_data['long']
            lat = form.cleaned_data['lat']
            rc_status = form.cleaned_data['rc_status']
            gardu = Gardu.objects.filter(id=id).update(gardu_name=gardu_name, up3=up3, long=long, lat=lat, rc_status=rc_status)
            messages.success(request, "Update data berhasil")
            return redirect('detail_gardu', gardu_name)
        else:
            messages(request, form.errors)
            
    return render(request, 'assets/gardu_edit.html', {'form' : form, 'gardu': gardu })
    

def delete_gardu(request, gardu_name):
    Gardu.objects.filter(gardu_name=gardu_name).delete()
    return redirect('all_gardu')
# END GARDU VIEW HANDLER
    
    
#RTU VIEW HANDLER
def all_rtu(request):
    if request.resolver_match.url_name == 'inventory_all_rtu':
        rtus = Rtu.objects.filter(gardu=None).order_by('gardu')
    else:
        rtus = Rtu.objects.all().order_by('gardu').exclude(gardu=None)
    paginator = Paginator(rtus, 50)
    page= request.GET.get('page')
    paged_rtus = paginator.get_page(page)
    jumlah = rtus.count()
    context = {
        'rtus' : paged_rtus,
        'jumlah' : jumlah,
    }
    return render(request, 'assets/all_rtu.html',context)

def create_rtu(request):
    if request.method == 'POST':
        form = RtuForm(request.POST)
        if form.is_valid():
            gardu = form.cleaned_data['gardu']
            serial_number_rtu = form.cleaned_data['serial_number_rtu']
            brand_rtu = form.cleaned_data['brand_rtu']
            model_rtu = form.cleaned_data['model_rtu']
            rtu_status = form.cleaned_data['rtu_status']
            note = form.cleaned_data['note']
            rtu = Rtu.objects.create(gardu=gardu, serial_number_rtu=serial_number_rtu, brand_rtu=brand_rtu, model_rtu=model_rtu, rtu_status=rtu_status, note=note)
            rtu.save()
            messages.success(request, 'RTU berhasil di buat !!')
            return redirect('all_rtu')
        else:
            messages.warning(request, form.errors)
            return redirect('create_rtu')
    else:
      form = RtuForm()
    return render(request, 'assets/create_rtu.html', {'form': form})

def detail_rtu(request, id):
    rtu = get_object_or_404(Rtu, id=id)
    print(rtu)
    return render(request, 'assets/rtu_detail.html', {'rtu' : rtu })

def edit_rtu(request, id):
    rtu = get_object_or_404(Rtu, id=id)
   
    form = RtuForm(initial={
        'gardu': rtu.gardu, 
        'serial_number_rtu' : rtu.serial_number_rtu, 
        'brand_rtu': rtu.brand_rtu, 
        'model_rtu': rtu.model_rtu,
        'rtu_status': int(rtu.rtu_status),
        'note' : rtu.note
        })
    if request.method == 'POST':
        form = RtuForm(request.POST)
        if form.is_valid():
            gardu = form.cleaned_data['gardu']
            serial_number_rtu = form.cleaned_data['serial_number_rtu']
            brand_rtu = form.cleaned_data['brand_rtu']
            model_rtu = form.cleaned_data['model_rtu']
            rtu_status = form.cleaned_data['rtu_status']
            note = form.cleaned_data['note']
            rtu = Rtu.objects.filter(id=id).update(gardu=gardu, serial_number_rtu=serial_number_rtu, brand_rtu=brand_rtu, model_rtu=model_rtu, rtu_status=rtu_status, note=note)
            messages.success(request, "Update data berhasil")
            return redirect('detail_rtu', id)
        else:
            messages(request, form.errors)
            return redirect('edit_gardu', id)
    return render(request, 'assets/rtu_edit.html', {'form' : form, 'rtu': rtu })

def delete_rtu(request, id):
    Rtu.objects.filter(id=id).delete()
    return redirect('all_rtu')
#END RTU HANDLER

#recti view handler
def all_rectifier(request):
    if request.resolver_match.url_name == 'inventory_all_rectifier':
        rectis = Rectifier.objects.filter(gardu=None).order_by('gardu')
    else:
        rectis = Rectifier.objects.all().order_by('gardu').exclude(gardu=None)
    paginator = Paginator(rectis, 50)
    page= request.GET.get('page')
    paged_rectis = paginator.get_page(page)
    jumlah = rectis.count()
    context = {
        'rectis' : paged_rectis,
        'jumlah' : jumlah,
    }
    return render(request, 'assets/all_rectifier.html', context)

def create_rectifier(request):
    if request.method == 'POST':
        form = RectifierForm(request.POST)
        if form.is_valid():
            gardu = form.cleaned_data['gardu']
            serial_number_recti = form.cleaned_data['serial_number_recti']
            brand_recti = form.cleaned_data['brand_recti']
            model_recti = form.cleaned_data['model_recti']
            brand_baterai = form.cleaned_data['brand_baterai']
            model_baterai = form.cleaned_data['type_baterai']
            jumlah_baterai = form.cleaned_data['jumlah_baterai']
            recti_status = form.cleaned_data['recti_status']
            note = form.cleaned_data['note']
            recti = Rectifier.objects.create(gardu=gardu, serial_number_recti=serial_number_recti, brand_recti=brand_recti,model_recti=model_recti,
                                             brand_baterai=brand_baterai, jumlah_baterai=jumlah_baterai, recti_status=recti_status, note=note)
            recti.save()
            messages.success(request, 'Recti berhasil di buat !!')
            return redirect('all_rectifier')
        else:
            messages.warning(request, form.errors)
            return redirect('create_rectifier')
    else:
      form = RectifierForm()  
    return render(request, 'assets/create_rectifier.html', {'form': form})

def detail_rectifier(request, id):
    recti = get_object_or_404(Rectifier, id=id)
    return render(request, 'assets/rectifier_detail.html', {'recti' : recti })

def delete_rectifier(request, id):
    Rectifier.objects.filter(id=id).delete()
    return redirect('all_rectifier')

def edit_rectifier(request, id):
    recti = get_object_or_404(Rectifier, id=id)
   
    form = RectifierForm(initial={
        'gardu': recti.gardu, 
        'serial_number_recti' : recti.serial_number_recti, 
        'brand_recti': recti.brand_recti, 
        'model_recti': recti.model_recti,
        'brand_baterai': recti.brand_baterai, 
        'type_baterai': recti.type_baterai,
        'jumlah_baterai': recti.jumlah_baterai,
        'recti_status': int(recti.recti_status),
        'note' : recti.note
        })
    if request.method == 'POST':
        form = RectifierForm(request.POST)
        if form.is_valid():
            gardu = form.cleaned_data['gardu']
            serial_number_recti = form.cleaned_data['serial_number_recti']
            brand_recti = form.cleaned_data['brand_recti']
            model_recti = form.cleaned_data['model_recti']
            brand_baterai = form.cleaned_data['brand_baterai']
            type_baterai = form.cleaned_data['type_baterai']
            jumlah_baterai = form.cleaned_data['jumlah_baterai']
            recti_status = form.cleaned_data['recti_status']
            note = form.cleaned_data['note']
            recti = Rectifier.objects.filter(id=id).update(gardu=gardu, serial_number_recti=serial_number_recti, brand_recti=brand_recti, 
                                                           model_recti=model_recti, brand_baterai=brand_baterai, type_baterai=type_baterai
                                                           ,jumlah_baterai=jumlah_baterai, recti_status=recti_status,note=note)
            messages.success(request, "Update data berhasil")
            return redirect('detail_rectifier', id)
        else:
            messages(request, form.errors)
            return redirect('edit_rectifier', id)
    return render(request, 'assets/rectifier_edit.html', {'form' : form, 'recti': recti })

#end recti view handler

#media handler view
def all_media(request):
    if request.resolver_match.url_name == 'inventory_all_media':
        media = Media.objects.filter(gardu=None).order_by('gardu')
    else:
        media = Media.objects.all().order_by('gardu').exclude(gardu=None)
    paginator = Paginator(media, 50)
    page= request.GET.get('page')
    paged_media = paginator.get_page(page)
    jumlah = media.count()
    context = {
        'medias' : paged_media,
        'jumlah' : jumlah,
    }
    return render(request, 'assets/all_media.html', context)

def create_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            gardu = form.cleaned_data['gardu']
            serial_number_media = form.cleaned_data['serial_number_media']
            brand_media = form.cleaned_data['brand_media']
            model_media = form.cleaned_data['model_media']
            protokol = form.cleaned_data['protokol']
            media_status = form.cleaned_data['media_status']
            note = form.cleaned_data['note']
            media = Media.objects.create(gardu=gardu, serial_number_media=serial_number_media, brand_media=brand_media,
                                             model_media=model_media, protokol=protokol, media_status=media_status,note=note)
            media.save()
            messages.success(request, 'Media berhasil di buat !!')
            return redirect('all_media')
        else:
            messages.warning(request, form.errors)
            return redirect('create_media')
    else:
      form = MediaForm()  
    return render(request, 'assets/create_media.html', {'form': form})

def detail_media(request, id):
    media = get_object_or_404(Media, id=id)
    return render(request, 'assets/media_detail.html', {'media' : media })

def delete_media(request, id):
    Media.objects.filter(id=id).delete()
    return redirect('all_media')

def edit_media(request, id):
    media = get_object_or_404(Media, id=id)
   
    form = MediaForm(initial={
        'gardu': media.gardu, 
        'serial_number_media' : media.serial_number_media, 
        'brand_media': media.brand_media, 
        'model_media': media.model_media,
        'protokol': media.protokol, 
        'media_status': int(media.media_status),
        'note' : media.note
        })
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            gardu = form.cleaned_data['gardu']
            serial_number_media = form.cleaned_data['serial_number_media']
            brand_media = form.cleaned_data['brand_media']
            model_media = form.cleaned_data['model_media']
            protokol = form.cleaned_data['protokol']
            media_status = form.cleaned_data['media_status']
            note = form.cleaned_data['note']
            media = Media.objects.filter(id=id).update(
                gardu=gardu, serial_number_media=serial_number_media, brand_media=brand_media,
                model_media=model_media, protokol=protokol, media_status=media_status,note=note)
            messages.success(request, "Update data media berhasil")
            return redirect('detail_media', id)
        else:
            messages(request, form.errors)
            return redirect('edit_media', id)
    return render(request, 'assets/media_edit.html', {'form' : form, 'media': media })

#handler view fi assets
def all_fi(request):
    if request.resolver_match.url_name == 'inventory_all_fi':
        fis = FaultIndicator.objects.filter(gardu=None).order_by('gardu')
    else:
        fis = FaultIndicator.objects.all().order_by('gardu').exclude(gardu=None)
    paginator = Paginator(fis, 50)
    page= request.GET.get('page')
    paged_fis = paginator.get_page(page)
    jumlah = fis.count()
    context = {
        'fis' : paged_fis,
        'jumlah' : jumlah,
    }
    return render(request, 'assets/all_fi.html', context)

def create_fi(request):
    if request.method == 'POST':
        form = FaultIndicatorForm(request.POST)
        if form.is_valid():
            gardu = form.cleaned_data['gardu']
            serial_number_fi = form.cleaned_data['serial_number_fi']
            brand_fi = form.cleaned_data['brand_fi']
            model_fi = form.cleaned_data['model_fi']
            fi_status = form.cleaned_data['fi_status']
            brand_ct = form.cleaned_data['brand_ct']
            model_ct = form.cleaned_data['model_ct']
            ct_status = form.cleaned_data['ct_status']
            note = form.cleaned_data['note']
            fi = FaultIndicator.objects.create(gardu=gardu,serial_number_fi=serial_number_fi, brand_fi=brand_fi,model_fi=model_fi, fi_status=fi_status,
                                               brand_ct=brand_ct,model_ct=model_ct, ct_status=ct_status,note=note)
            fi.save()
            messages.success(request, 'Fault Indicator berhasil di buat !!')
            return redirect('all_fi')
        else:
            messages.warning(request, form.errors)
            return redirect('create_fi')
    else:
      form = FaultIndicatorForm() 
    return render(request, 'assets/create_fi.html', {'form': form})

def detail_fi(request, id):
    fi = get_object_or_404(FaultIndicator, id=id)
    return render(request, 'assets/fi_detail.html', {'fi' : fi })

def edit_fi(request, id):
    fi = get_object_or_404(FaultIndicator, id=id)
   
    form = FaultIndicatorForm(initial={
        'gardu': fi.gardu, 
        'serial_number_fi' : fi.serial_number_fi, 
        'brand_fi': fi.brand_fi, 
        'model_fi': fi.model_fi,
        'fi_status': int(fi.fi_status),
        'brand_ct': fi.brand_ct, 
        'model_ct': fi.model_ct,
        'ct_status': int(fi.ct_status),
        'note' : fi.note
        })
    if request.method == 'POST':
        form = FaultIndicatorForm(request.POST)
        if form.is_valid():
            gardu = form.cleaned_data['gardu']
            serial_number_fi = form.cleaned_data['serial_number_fi']
            brand_fi = form.cleaned_data['brand_fi']
            model_fi = form.cleaned_data['model_fi']
            fi_status = form.cleaned_data['fi_status']
            brand_ct = form.cleaned_data['brand_ct']
            model_ct = form.cleaned_data['model_ct']
            ct_status = form.cleaned_data['ct_status']
            note = form.cleaned_data['note']
            fi = FaultIndicator.objects.create(gardu=gardu,serial_number_fi=serial_number_fi, brand_fi=brand_fi,model_fi=model_fi, fi_status=fi_status,
                                               brand_ct=brand_ct,model_ct=model_ct, ct_status=ct_status,note=note)
            fi.save()
            messages.success(request, "Update data berhasil")
            return redirect('detail_fi', id)
        else:
            messages.warning(request, form.errors)
            return redirect('edit_fi', id)
    return render(request, 'assets/fi_edit.html', {'form' : form, 'fi': fi })

def delete_fi(request, id):
    FaultIndicator.objects.filter(id=id).delete()
    return redirect('all_fi')


#end handler for fi assets

#move to inventory action
def move_to_inventory(request, asset ,id):

    if asset == 'rtu':
        rtu = Rtu.objects.get(pk=id)
        rtu.gardu = None
        rtu.save()
        messages.success(request, 'Rtu berhasil di pindahkan ke inventory')
        return redirect('all_rtu')
    elif asset == 'rectifier':
        rectifier = Rectifier.objects.get(pk=id)
        rectifier.gardu = None
        messages.success(request, 'Rectifier berhasil di pindahkan ke inventory')
        return redirect('all_rectifier')
    elif asset == 'media':
        media = Media.objects.get(pk=id)
        media.gardu = None
        media.save()      
        messages.success(request, 'Media berhasil di pindahkan ke inventory')  
        return redirect('all_media')
    elif asset == 'fault_indicator':
        fi = FaultIndicator.objects.get(pk=id)
        fi.gardu = None
        fi.save()      
        messages.success(request, 'Fault Indicator berhasil di pindahkan ke inventory')  
        return redirect('all_fi')
    else:
        messages.warning(request, 'Terjadi kesalahan, coba lagi')
        return redirect('home')
    
def cari(request, asset):
    #variabel to check jika url sebelumnya ada inventory jika ada maka buat kondisi untuk pencarian di invenrtory
    refer = request.META.get('HTTP_REFERER')
    
    if asset == 'gardus' :
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                result = Gardu.objects.order_by('gardu_name').filter(
                    Q(gardu_name__icontains=keyword) |
                    Q(up3__up3__icontains=keyword)
                    )
                paginator = Paginator(result, 50)
                page= request.GET.get('page')
                paged_result = paginator.get_page(page)
                jumlah = result.count()
                context = {
                    'gardus' : paged_result,
                    'jumlah' : jumlah,
                }
                return render(request, 'assets/all_gardu.html', context)
        return redirect('all_gardu')
    elif asset == 'rtus':
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                result = Rtu.objects.order_by('gardu').filter(
                    Q(gardu__gardu_name__icontains=keyword) |
                    Q(gardu__up3__up3__icontains=keyword) |
                    Q(brand_rtu__icontains=keyword)|
                    Q(model_rtu__icontains=keyword)
                    ).exclude(gardu=None)
                paginator = Paginator(result, 50)
                page= request.GET.get('page')
                paged_result = paginator.get_page(page)
                jumlah = result.count()
                context = {
                    'rtus' : paged_result,
                    'jumlah' : jumlah,
                }
                return render(request, 'assets/all_rtu.html', context)
        
        return redirect('all_rtu')
    elif asset == 'rectifiers':
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                result = Rectifier.objects.order_by('gardu').filter(
                    Q(gardu__gardu_name__icontains=keyword) |
                    Q(gardu__up3__up3__icontains=keyword) |
                    Q(brand_recti__icontains=keyword)|
                    Q(model_recti__icontains=keyword)|
                    Q(brand_baterai__icontains=keyword) |
                    Q(type_baterai__icontains=keyword)
                    ).exclude(gardu=None)
                paginator = Paginator(result, 50)
                page= request.GET.get('page')
                paged_result = paginator.get_page(page)
                jumlah = result.count()
                context = {
                    'rectis' : paged_result,
                    'jumlah' : jumlah,
                }
                return render(request, 'assets/all_rectifier.html', context)
        return redirect('all_rectifier')
    elif asset == 'medias':
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                result = Media.objects.order_by('gardu').filter(
                    Q(gardu__gardu_name__icontains=keyword) |
                    Q(gardu__up3__up3__icontains=keyword) |
                    Q(brand_media__icontains=keyword)|
                    Q(model_media__icontains=keyword)|
                    Q(protokol__icontains=keyword) 
                    ).exclude(gardu=None)
                paginator = Paginator(result, 50)
                page= request.GET.get('page')
                paged_result = paginator.get_page(page)
                jumlah = result.count()
                context = {
                    'medias' : paged_result,
                    'jumlah' : jumlah,
                }
                return render(request, 'assets/all_media.html', context)
        return redirect('all_media')
    elif asset == 'fis':
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                result = FaultIndicator.objects.order_by('gardu').filter(
                    Q(gardu__gardu_name__icontains=keyword) |
                    Q(gardu__up3__up3__icontains=keyword) |
                    Q(brand_fi__icontains=keyword)|
                    Q(model_fi__icontains=keyword)|
                    Q(brand_ct__icontains=keyword) 
                    ).exclude(gardu=None)
                paginator = Paginator(result, 50)
                page= request.GET.get('page')
                paged_result = paginator.get_page(page)
                jumlah = result.count()
                context = {
                    'fis' : paged_result,
                    'jumlah' : jumlah,
                }
                return render(request, 'assets/all_fi.html', context)
        return redirect('all_fi')
    
    
    