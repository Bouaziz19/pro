import traceback, os
from django.shortcuts import render,redirect
from .models import data,log_res
from django.http import HttpResponse
from ag import output,AG
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# res = data.objects.all()
# res = data.objects.filter(name='valeur')
# res = data.objects.exclude(name='valeur')
# col_list = ['col1', 'col2', 'col3']
# Obj.objects.all().values_list(col_list)
# data.objects.filter(name='nb').update(value='8')
# return HttpResponse(msg, content_type='text/plain')
@csrf_exempt
def stop_pros(request):
    os.system('killall python3')
    return HttpResponse('', content_type='text/plain')
@csrf_exempt
def save_page(request):
    data = { 'is_valid': False,}
    if request.is_ajax() and request.method =='POST':
        aa = request.POST.get('aa')
        write_f(aa)
        return HttpResponse('SAVE', content_type='text/plain')
    else:
        return HttpResponse('', content_type='text/plain')
    

@csrf_exempt
def str_ag(request):
    AG.update_star_date(datetime.now())
    
    AG.update_res("run")
    try:
        res = output.get_res()
    except Exception as e:
        strr=str(traceback.format_exc())
        AG.update_res(strr)
    AG.update_stop_date(datetime.now())
    
    return HttpResponse('', content_type='text/plain')
from string import Template
class DeltaTemplate(Template):
    delimiter = '%'
def strfdelta(td, fmt):

    # Get the timedelta’s sign and absolute number of seconds.
    sign = "-" if td.days < 0 else "+"
    secs = abs(td).total_seconds()

    # Break the seconds into more readable quantities.
    days, rem = divmod(secs, 86400)  # Seconds per day: 24 * 60 * 60
    hours, rem = divmod(rem, 3600)  # Seconds per hour: 60 * 60
    mins, secs = divmod(rem, 60)

    # Format (as per above answers) and return the result string.
    t = DeltaTemplate(fmt)
    return t.substitute(
        s=sign,
        D="{:d}".format(int(days)),
        H="{:02d}".format(int(hours)),
        M="{:02d}".format(int(mins)),
        S="{:02d}".format(int(secs)),
        )


@csrf_exempt
def get_res_page(request):
    b=log_res.objects.filter(id_page=1)
    dif=b[0].stop_date-b[0].star_date
    # dif=dif.strftime('%H:%M:%S')
    dif=strfdelta(dif, "%H:%M:%S")
    return JsonResponse({'res':b[0].res,"dif":str(dif)}, safe=False)


@csrf_exempt
def page_ac(request):
    AG.update_num_prob_p()
    context= get_context()
    return render(request, 'static_pages/index.html', context)

@csrf_exempt
def page2_ac(request):
    AG.update_num_prob_p()
    context= get_context()
    return render(request, 'static_pages/index2.html', context)

@csrf_exempt
def write_f(data_e):
    data_e=data_e.replace('false', 'False')
    data_e =data_e.replace('true', 'True')
    data_e=eval(data_e)
    for key, value in data_e.items():
        data.objects.filter(name=key).update(value=value)
    return True

@csrf_exempt
def get_context():
    type_data={
        'id_cont_dem': 'bool',
     'id_nb': 'int',
     'id_ndepo': 'int',
     'id_temps_sum': 'int',
     'id_nprod': 'int',
     'id_t_population': 'int',
     'id_crit_dar': 'int',
     'id_num_prob': 'int',
     'id_volumebatch': 'double',
     'id_delai_fin': 'double',
     'id_produits': 'list',
     'id_Localdep': 'list',
     'id_depots': 'list',
     'id_co_pom_inj': 'list',
     'id_co_inj': 'list',
     'id_cont_entr': 'matrix',
     'id_Demdepo': 'matrix',
     'id_stok_in': 'matrix',
     'id_bathint': 'matrix',}
    Demdepo = data.objects.all()
    d_data={}
    for x in Demdepo:
        d_data[x.name] = x.value
    msg = str(d_data)
    context={'d_data':d_data,'type_data':type_data}
    return context
