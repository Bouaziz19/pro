# *-* coding: utf8 *-*

        #    cur = sqlite3.connect("donne.db")
        #    
        #    def get_val(name ):
        #        re = cur.execute('SELECT val FROM donne WHERE  name = "%s"' % (name))
        #        val=eval(str(re.fetchone()[0]))
        #        return val
        #    
        #    def set_val(name,val):
        #        cur.execute('UPDATE donne SET val="%s" WHERE  name = "%s"' % (str(val),name))
        #        cur.commit()
        #    cur.close()

#   read
def red_f():
    data_f= open("data.txt","r")
    data= eval(data_f.read())
    data_f.close
    return data
 # data

data =red_f()


# print data
#    write
def write_f(data):
    w_data= open("data.txt","w")
    s_data=str(data)
    w_data.write(s_data)
    w_data.close

produits = data['produits']

depots = data['depots']

nprod = data['nprod']

ndepo = data['ndepo']
# Les conditions initiales des anciens batchs avec ses localisations en volume

# cap max pipeline
volumebatch = data['volumebatch']
# par jour  hmax
temps_sum = data['temps_sum']
#  number of batch
nb = data['nb']
# type0 = data['type0']
 #old batch  autre sense
# Volume0 = data['Volume0']
bathint = data['bathint']
# Localisation des dépôts en volume par rapport à la raffinerie


debu = data['debu']
fin = data['fin']

Localdep = data['Localdep']
# Localdep =fonction.lis(2,ndepo,volumebatch)  

# lLocalisation des dépôts soit pts or []

# Les conditions pompage max et min injection et reception 
# m3 condition d'injection refinery
co_inj = data['co_inj']
#3/h  pom_inj  = inj/tempe_inj cond d'injection refinery
co_pom_inj = data['co_pom_inj']
    #[[min_d1,min_d2],[max_d1,min_d2]]
    #co_pom_rec=[[10,20],[10,20]]
# Demandes journalières par dépôt
# Demdepo=fonction.lis(ndepo,nprod,10)
# Demdepo[0]=[1200,400,80,0]#demand jrs d1[p1,p2,p3]
# Demdepo[1]=[3000,800,150,150]
Demdepo = data['Demdepo']
# print type(Demdepo)
# La capacité et le volume initial des produits et du contaminât par dépôt avec le stock de sécurité
#capacite = fonction.lis(ndepo,nprod,99999)
# capacite[0]=[99999,99999,99999]
# capacite[1]=[99999,99999,99999]


#stokint = fonction.lis(ndepo,nprod,0)
# print "stokint",stokint
# stokint[0]=[0,0,0]
# stokint[1]=[0,0,0]

#stoksec = fonction.lis(ndepo,nprod,5)
# stoksec[0]=[5,5,5]
# stoksec[1]=[5,5,5]

# Volume moyen du contaminât qui résulte entre deux produits différents et les séquences interdites 'n'
# cont_entr = fonction.lis(nprod,nprod,1) # seq interdit
# cont_entr[0]=['n',28,30,'n']
# cont_entr[1]=[28,'n','n',0]
# cont_entr[2]=[30,'n','n','n']
# cont_entr[3]=[30,'n','n','n']
cont_entr = data['cont_entr']
#pas
pas = data['pas']
# duré de stop d'exution EN MIN
delai_fin = data['delai_fin']
#parmetr  AG  



# print type(p_c_c)
t_population = data['t_population']

crit_dar = data['crit_dar']

cont_dem = data['cont_dem']


# set_val('produits',produits)
# set_val('depots',depots)
# set_val('nprod',nprod)
# set_val('ndepo',ndepo)
# set_val('volumebatch',volumebatch)
# set_val('temps_sum',temps_sum)
# set_val('nb',nb)
# set_val('type0',type0)
# set_val('Volume0',Volume0)
# set_val('bathint',bathint)
# set_val('debu',debu)
# set_val('fin',fin)
# set_val('Localdep',Localdep)
# set_val('co_inj',co_inj)
# set_val('co_pom_inj',co_pom_inj)
# set_val('Demdepo',Demdepo)
# set_val('cont_entr',cont_entr)
# set_val('pas',pas)
# set_val('delai_fin',delai_fin)
# set_val('n_c_a',n_c_a)
# set_val('p_c_c',p_c_c)
# set_val('t_population',t_population)
# set_val('crit_dar',crit_dar)
# set_val('cont_dem',cont_dem)


