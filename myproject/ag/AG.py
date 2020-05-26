###!/usr/bin/env python
# *-* coding: utf8 *-*
import traceback, os
from app.models import log_res
import time
import random, sys, time
from ag import fonction
from copy import deepcopy
from app.models import data as m_data
from datetime import datetime

def random_dist(min_v,max_v):
    r_v=random.randint(min_v,max_v)
    #r_v=int(random.uniform(min_v,max_v))
    
    return deepcopy(r_v)
def prin(st,va):
    print(st," = ",va)
def red_f(m_data):
    Demdepo = m_data.objects.all()
    d_data={}
    for x in Demdepo:
        d_data[x.name] = eval(x.value)
    return d_data
def tempe_depas(strr=''):
        if delai_fin <= time.clock():
            st="le temp depase delai_fin doncdd problem d'entr "+strr
            update_res(st)
            sys.exit(st)
class individu:
    def __init__(self, Batch_n=None, flag_g=0):
        tempe_depas('  1')
        
        fin_in=True
        if Batch_n==None:
            
            Batch_n = self.geniri_Batch()
        vald=False
        while vald==False:
                vald=self.seq_inter(Batch_n)
                if vald==False:
                    Batch_n = self.geniri_Batch()
        while fin_in:
            update_stop_date(datetime.now())
            j=0
            while j<n_c_a:
                a = self.genirisolition(Batch_n, flag_g)
                self.fo = self.evalutation(a)
                self.solition = self.add_temps(a)
                self.cont_demend= True
                self.solition =self.add_stok()
                j+=1
                if cont_dem==False:
                    fin_in=False
                elif self.cont_demend:
                    fin_in=False
            Batch_n = self.geniri_Batch()
       
    def seq_inter(self, Batch):
        v = True
        for j in r_nb_1:
            if cont_entr[Batch[1][j]][Batch[1][j + 1]] == 'n':
                v = False
                break
        return deepcopy(v)
    def generater_inject_qent(self):
        Batch=[]
        for i in r_nb:
            Batch.append(random_dist(co_inj[0], co_inj[1]))
            
        return deepcopy(Batch)
    def generater_inject_typ(self):
        Batch=[]
        i0=random_dist(0, nprod-1)
        Batch.append(i0)
        j=1
        while j<nb:
            i1=random_dist(0, nprod-1)
            if cont_entr[i0][i1]!="n":
                Batch.append(i1)
                i0=i1
                j+=1
        return deepcopy(Batch)
    # A
    def geniri_Batch(self):
        Batch = [self.generater_inject_qent(), self.generater_inject_typ()]
        return deepcopy(Batch)
    # convert Batch to Batch {Batch[0] qentiti/ l[1] type de produit } sans doublen
    def sup_double_2(self, Batch):
        rang = list(range(0, len(Batch[1])))
        order = [[], [], []]
        for i in rang:
            if Batch[0][i] != 0:
                order[0].append(Batch[0][i])
                order[1].append(Batch[1][i])
                order[2].append(Batch[2][i])
        Batch = order
        return deepcopy(Batch)
    # add  temps to Batch {Batch[3] temps}
    def add_temps(self, Batch):
        # tempe d'injection
        tem_inj = []
        for i in Batch[0]:
            #   tempe_inj = inj / pom_inj
            temp = int(i *temp_moy)
            tem_inj.append(round(float(temp) / 100, 2))
        Batch.append(tem_inj)
        return deepcopy(Batch)
    def add_stok(self):
        sol=self.solition
        stok = deepcopy(stok_in)
        l = sol[2]
        l_tem = sol[4]
        l_stok = []
        temp=0
        jour=24
        i_jou=0
        for n in range(0,len(l)):

            temp+=deepcopy(l_tem[n])
            val_r=int(temp/jour)
            if val_r>0:
                temp=temp%jour
                i_jou+=val_r
            for i in r_ndepo:
                for j in r_nprod:
                    s = 0
                    for k in l[n][i][j]:
                        s += k[0]
                    stok[i][j] += deepcopy(s)
                    if val_r>0 and i_jou<=temps_sum:
                        stok[i][j]-=val_r*Demdepo[i][j]
                        if stok[i][j] <0:
                            self.cont_demend= False
            l_stok.append(deepcopy(stok))
        sol.append(l_stok)
        return deepcopy(sol)
    def evalutation(self, Batch):
        s = 0
        for i in range(0, len(Batch[1]) - 2):
            s = s + cont_entr[Batch[1][i]][Batch[1][i + 1]]
        return deepcopy(s)
    def get_qnti_ran(self, qnti_local):
        return random_dist(1,qnti_local)
    def get_dep_ran(self, ndepo):
        return random_dist(0,ndepo-1) 
    def act_bath_en(self, qnti, bath_en,  qnti_resp, Localdep, ndepo):
        qnti_local =deepcopy(qnti)
        len_b = len(bath_en[0])
        las_b=[]
        ty_p_r_zero=[]
        for ii in r_ndepo:
            las_b.append(-1)
            ty_p_r_zero.append(-1)
        # seqense 
        sq=0
        while qnti_local != 0 :
            # qnti_ran random qantit
            qnti_ran = self.get_qnti_ran(qnti_local)
            # dep_ran random depo
            dep_ran = self.get_dep_ran(ndepo) 
            while qnti_ran != 0 :
                
                s=0
                i=0
                while i < len_b :
                    
                    s+=bath_en[0][i]
                    if Localdep[dep_ran]<=s:
                        ty_p_r=bath_en[1][i]
                        nb_p_r=bath_en[2][i]
                        if i!=0:
                            #qr_ar qantiti acsepti areseptioni de type
                            
                            qr_ar=bath_en[0][i]
                            if qr_ar<=qnti_ran:
                                qr_ar=deepcopy(min(qr_ar,qnti_ran))
                                bath_en[0].pop(i)
                                bath_en[1].pop(i)
                                bath_en[2].pop(i) 
                                len_b-=1
                            else:
                                qr_ar=deepcopy(qnti_ran)
                                bath_en[0][i]-= qr_ar

                        else:
                            # qr_ar qantiti acsepti areseptioni
                            qr_ar=deepcopy(qnti_ran)
                            bath_en[0][i]-= qr_ar
                        bath_en[0][0]+= qr_ar

                        if las_b[dep_ran]==nb_p_r or nb_p_r==0:
                            if nb_p_r!=0:
                                qnti_resp[dep_ran][ty_p_r][-1][0]+=qr_ar
                            else :
                                if ty_p_r_zero[dep_ran] == ty_p_r:
                                    qnti_resp[dep_ran][ty_p_r][-1][0]+=qr_ar
                                else :
                                    qnti_resp[dep_ran][ty_p_r].append([qr_ar,nb_p_r,sq])
                                    sq+=1
                                    las_b[dep_ran]=nb_p_r
                                    ty_p_r_zero[dep_ran] = ty_p_r
                        else :
                            qnti_resp[dep_ran][ty_p_r].append([qr_ar,nb_p_r,sq])
                            sq+=1
                            las_b[dep_ran]=nb_p_r
                        qnti_ran -= qr_ar
                        qnti_local -= qr_ar
                        i=deepcopy(len_b)
                    i+=1


        return deepcopy(bath_en), deepcopy(qnti_resp)
    def genirisolition(self, Batch_n, flag_g):
        fin = False
        j = 0
        # afficahe chromosome A
        Batch = deepcopy(Batch_n)
        self.solition = Batch
        # add line de respstio
        Batch.append([])
        # add line de temps
        Batch.append([])
        bath_en = deepcopy(bathint)
        le = len(Batch[0])
        for i in range(0, le):
            qnti = Batch[0][i]
            typ = Batch[1][i]
            bath_en[0].insert(0, 0)
            bath_en[1].insert(0, typ)
            bath_en[2].insert(0, i + 1)
            
            qnti_resp=deepcopy(qnti_resp_def) 
            bath_en, qnti_resp = self.act_bath_en(qnti, bath_en, qnti_resp, Localdep, ndepo)
            bath_en = self.sup_double_2(bath_en)
            Batch[2].append(deepcopy(qnti_resp))
            Batch[3].append(deepcopy(bath_en))
        return deepcopy(Batch)
class population:
    def __init__(self, nombre_initial_population=50, Batch_ns=None, flag_gs=0, dely=33):
        self.nombre_initial_population = nombre_initial_population
        self.individus = self.genu_individus(Batch_ns, flag_gs)
        self.classement_po = self.classement_ind()
        self.p = self.calcu_prob()
    # fin delivery cnstr
    def classement_ind(self):
        ll = []
        for i in self.individus:
            ll.append(i.fo)
        ll = list(zip(ll, list(range(len(ll)))))
        ll.sort()
        sorted_l = [x for (x, y) in ll]
        sorted_idx = [y for (x, y) in ll]
        return sorted_idx
    def genu_individus(self, Batch_ns, flag_gs):
        individus = []
        if Batch_ns == None:
            for v in range(self.nombre_initial_population):
                sol = individu()
                individus.append(sol)
        else:
            for v in range(self.nombre_initial_population):
                sol = individu(Batch_ns[v], flag_gs)
                individus.append(sol)
        return individus
    def new_population(self):
        new_individus = []
        ta = int(round(t_population * 0.01))
        ta2 = t_population - ta
        t = 0
        while t < ta:
            ii = random_dist(0, t_population - 1)
            kk = [self.individus[ii].solition[0], self.individus[ii].solition[1]]
            new_individus.append(self.mutation(kk));
            t += 1

        rang = list(range(int(ta2 / 2)))
        if ta2 % 2 != 0:
            ppp = self.individus[self.classement_po[0]].solition
            new_individus.append([ppp[0], ppp[1]])
        sec = self.selection()
        for i in rang:
            i1 = self.individus[self.classement_po[sec[2 * i]]].solition
            i2 = self.individus[self.classement_po[sec[2 * i + 1]]].solition
            i3 = [deepcopy(i1[0]), deepcopy(i1[1])]
            i4 = [deepcopy(i2[0]), deepcopy(i2[1])]
            new_individus.append(self.croisement_deux(i3, i4))
            new_individus.append(self.croisement_deux(i4, i3))
        self.individus = self.genu_individus(new_individus, 1)
        return deepcopy(self)
    def calcu_prob(self):
        pr_t_pop = int(round(t_population * 0.6))
        p = []
        s = 1.0
        n = 1.0 / t_population
        pp = 0
        for i in range(pr_t_pop - 1):
            pp = s * n
            p.append(pp)
            s -= pp
        p.append(pp)
        p[0] += s - pp
        for i in range(1, pr_t_pop):
            p[i] += p[i - 1]
        return p
    def selection(self):
        sec = []
        rang = range(t_population)
        rang2 = range(len(self.p))
        for i in rang:
            aa = random_dist(0, 1)
            for j in reversed(rang2):

                if aa > self.p[j]:
                    sec.append(j)
                    break
                elif j == 0:
                    sec.append(j)
                    break

        return deepcopy(sec)
    def croisement_deux(self, i1, i2):
        l1 = [deepcopy(i1[0]), deepcopy(i1[1])]
        l2 = deepcopy(i2[1])
        l3 = [[], []]
        for i in range(len(l2)-1):
            try:
                if l2[i] in l1[1]:
                    j = l1[1][:-1].index(l2[i])
                    l3[0].append(l1[0][j])
                    l3[1].append(l1[1][j])
                    l1[0].pop(j)
                    l1[1].pop(j)

            except :
                pass
        l1[0] = l3[0] + l1[0]
        l1[1] = l3[1] + l1[1]
        return deepcopy(l1)
    def mutation(self, i1):
        ta = int(round(nb * 0.1))
        f = 0
        while f < ta:
            i = random_dist(0, nb)
            j = random_dist(0, nb)
            n = i1[1][i]
            m = i1[0][i]
            i1[1][i] = i1[1][j]
            i1[0][i] = i1[0][j]
            i1[1][j] = n
            i1[0][j] = m
            f += 1
        return deepcopy(i1)
def update_res(st):
    b=log_res.objects.filter(id_page=1)
    b.update(res=st)
def update_star_date(st):
    b=log_res.objects.filter(id_page=1)
    b.update(star_date=st)
def update_stop_date(st):
    b=log_res.objects.filter(id_page=1)
    b.update(stop_date=st)
def update_num_prob_p():
    b=m_data.objects.filter(name="id_num_prob")
    st=str(int(b[0].value)+1)
    b.update(value=st)
def get_res():
    b=log_res.objects.filter(id_page=1)
    for bb in b:
        bbb=bb
    return bbb.res
def gin_AG():
    

    global n_c_a
    n_c_a=50
    global p_c_c
    p_c_c=0.2

    data_entr =red_f(m_data)
    global produits
    produits = data_entr['id_produits']
    global nprod
    nprod = data_entr['id_nprod']
    global r_nprod
    r_nprod = range(nprod)
    global in_r_nprod
    in_r_nprod = r_nprod[::-1]
    global ndepo
    ndepo = data_entr['id_ndepo']
    global r_ndepo
    r_ndepo = range(ndepo)
    global in_r_ndepo
    in_r_ndepo = r_ndepo[::-1]
    global nb
    nb = data_entr['id_nb']
    global r_nb
    r_nb = range(nb)
    global r_nb_1
    r_nb_1 = range(nb-1)
    global t_population
    t_population = data_entr['id_t_population']
    global crit_dar
    crit_dar = data_entr['id_crit_dar']
    global delai_fin
    delai_fin = data_entr['id_delai_fin']
    global temps_sum
    temps_sum = data_entr['id_temps_sum']  # par jour  hmax
    # global r_temps_sum
    # r_temps_sum = range(temps_sum)
    global Demdepo
    Demdepo = data_entr['id_Demdepo']
    global stok_in
    stok_in= data_entr['id_stok_in']
    global bathint
    bathint = data_entr['id_bathint']
    bathint.append([])
    for i in range(len(bathint[0])):
        bathint[2].append(0)

    global cont_dem
    cont_dem = data_entr['id_cont_dem']

    global co_inj
    co_inj = data_entr['id_co_inj']

    global cont_entr
    cont_entr = data_entr['id_cont_entr']
    global Localdep
    Localdep = data_entr['id_Localdep']
    global co_pom_inj
    co_pom_inj = data_entr['id_co_pom_inj']
    global temp_moy
    temp_moy=100/((co_pom_inj[0]+co_pom_inj[1])/2)
    global volumebatch
    volumebatch = data_entr['id_volumebatch']
    # global max_dem_pr
    # max_dem_pr = []
    # print('___________________________________________________________'+str(crit_dar))
    global qnti_resp_def
    qnti_resp_def=fonction.lis(ndepo, nprod, 0)
    for i in r_ndepo:
        for j in r_nprod:
            qnti_resp_def[i][j]=[]
    # global lis_temps_sum
    # lis_temps_sum=[]
    # for i in r_temps_sum:
    #     lis_temps_sum.append(0)
    # print('population install ')
    st='population initiale '+str(crit_dar)
    update_res(st)
    update_stop_date(datetime.now())
    po = population(t_population)
    min_indu = po.individus[po.classement_po[0]]
    min_fo = min_indu.fo
    iii = 0
    ref=25
    while iii < crit_dar:
        # print('iteration ',iii,'  ',min_indu.fo)
        if iii%ref==0:
            st='iteration '+str(iii)+'  '+str(min_indu.fo)
            old=get_res()
            st=str(old)+"<br/>"+st
            update_res(st)


        # print('iteration ',iii,'  ',min_indu.fo)
        st='iteration '+str(iii)+'  '+str(min_indu.fo)
        po = po.new_population()  # tt etap d'AG
        po.classement_po = po.classement_ind()
        min_indu2 = po.individus[po.classement_po[0]]
        if min_fo > min_indu2.fo:
            min_indu = min_indu2
            min_fo = min_indu2.fo
        iii += 1

    # min_indu.solition =add_stok(min_indu.solition)
    return deepcopy(min_indu)
# if __name__ == "__main__":
#     print('                     ********                            ')

#     s_min = gin_AG()
#     print('                     ********                            ')