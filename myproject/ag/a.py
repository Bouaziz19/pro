# *-* coding: utf8 *-*
import eel,time
import output
eel.init('web')

def red_f():
    data_f= open("data.txt","r")
    data= eval(data_f.read())
    data_f.close
    return data

#    write
@eel.expose
def write_f(data):
    data=data.replace('false', 'False')
    data =data.replace('true', 'True')
    w_data= open("data.txt","w")
    s_data=str(data)
    w_data.write(s_data)
    w_data.close



 # data

type_data={'id_cont_dem': 'bool',
     'id_nb': 'int',
     'id_ndepo': 'int',
     'id_temps_sum': 'int',
     'id_pas': 'int',
     'id_nprod': 'int',
     'id_t_population': 'int',
     'id_crit_dar': 'int',
     'id_volumebatch': 'double',
     'id_delai_fin': 'double',
     'id_produits': 'list',
     'id_fin': 'list',
     'id_debu': 'list',
     'id_depots': 'list',
     'id_co_pom_inj': 'list',
     'id_co_inj': 'list',
     'id_cont_entr': 'matrix',
     'id_Demdepo': 'matrix',
     'id_bathint': 'matrix',
     'id_Localdep': 'matrix', }
@eel.expose
def lode_data():
    data = red_f()
    for id_d, type_d in type_data.items():
        eel.setdata(id_d,type_d,data[id_d[3:]])

@eel.expose
def save_data():
    for id_d, type_d in type_data.items():
        eel.getdata(id_d[3:],type_d)
    eel.write_f()

@eel.expose
def getres():
    res = output.get_res()
    eel.setStatut('<h1> start </h1>')
    eel.setres(res)
    # for i in xrange(14):
    #     res=res
    #
    #     time.sleep(1)
    eel.setStatut('<h1> stop </h1>')
    # data_f = open("output\index.html", "r")
    # res = data_f.read()
    # eel.setres(res)
web_app_options = {
    'mode': "chrome-app",
    'port': 8080,
    'chromeFlags': ["--start-fullscreen", "--browser-startup-dialog"]
}

eel.start('main.html', )

