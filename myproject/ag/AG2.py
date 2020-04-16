###!/usr/bin/env python
# *-* coding: utf8 *-*
import traceback, os
from app.models import log_res
import time
import random, sys, time
from ag import fonction
from copy import deepcopy
from app.models import data as m_data
def prin(va,st):
    print(st," : ",va)
def red_f(m_data):
    Demdepo = m_data.objects.all()
    d_data={}
    for x in Demdepo:
        d_data[x.name] = eval(x.value)
    return d_data
def tempe_depas(str=''):
        if delai_fin <= time.clock():
            sys.exit('le temp depase delai_fin' + str)


class individu:
    def __init__(self, max_dem_pr, Batch_n=None, flag_g=0):
        tempe_depas('  1')
        a = self.genirisolition(Batch_n, flag_g)

        if a != None:
            self.fo = self.evalutation(a)
            self.solition = self.add_temps(a)
        else:
            self.fo = None
            self.solition = None

    # list des Batch
    #
    # verifi les séquences interdites C
    def seq_inter(self, Batch):
        m = list(range(0, len(Batch[1]) - 1))
        v = True
        for j in m:
            if cont_entr[Batch[1][j]][Batch[1][j + 1]] == 'n':
                v = False
                break
        return deepcopy(v)

    # corection  les séquences interdites
    def corec_seq_inter(self, Batch):
        m = list(range(0, len(Batch[1]) - 1))
        for i in m:
            for j in m:
                if i != j and cont_entr[Batch[1][j]][Batch[1][j + 1]] == 'n':
                    b1 = Batch[0][j]
                    b2 = Batch[1][j]
                    Batch[0][j] = Batch[0][j + 1]
                    Batch[1][j] = Batch[1][j + 1]
                    Batch[0][j + 1] = b1
                    Batch[1][j + 1] = b2
        return deepcopy(Batch)

    # convert l to Batch alatoir and save as "Batch"
    def rand_seq_bat(self, Batch):
        # rasembler dans un seul chromo
        rang_in = list(range(0, len(Batch[0])))

        l = [[], []]
        random.shuffle(rang_in)
        for i in rang_in:
            l[0].append(Batch[0][i])
            l[1].append(Batch[1][i])
        Batch = l
        return deepcopy(Batch)

    # A
    def geniri_Batch(self):

        p = list(range(0, nprod))
        Batch = [[], []]

        nbpp = fonction.generater_random_list2(nb, nprod)
        while 0 in nbpp:
            nbpp = fonction.generater_random_list2(nb, nprod)
        for i in p:
            # v=fonction.generater_random_list(max_dem_pr[i], co_inj[0], co_inj[1])
            v = fonction.generater_random_list2(max_dem_pr[i], nbpp[i])
            vi = [i] * len(v)

            Batch[0] = Batch[0] + list(v)
            Batch[1] = Batch[1] + vi

        return deepcopy(Batch)

    # convert Batch to Batch {Batch[0] qentiti/ l[1] type de produit } sans doublen
    def sup_double(self, Batch):
        rang = list(range(0, len(Batch[1])))
        order = [[], []]
        for i in rang:
            if Batch[0][i] != 0:
                order[0].append(Batch[0][i])
                order[1].append(Batch[1][i])
        Batch = order

        order = [[], []]

        s = Batch[0][0]
        rang = list(range(0, len(Batch[1]) - 1))
        if len(rang) > 0:
            for i in rang:
                if Batch[1][i] == Batch[1][i + 1]:
                    s = s + Batch[0][i + 1]
                else:
                    order[0].append(s)
                    order[1].append(Batch[1][i])
                    s = Batch[0][i + 1]
                if i == len(Batch[1]) - 2:
                    order[0].append(s)
                    order[1].append(Batch[1][i + 1])
            Batch = order
        return deepcopy(Batch)

    def sup_double_2(self, Batch):
        rang = list(range(0, len(Batch[1])))
        order = [[], [], []]
        for i in rang:
            if Batch[0][i] != 0:
                order[0].append(Batch[0][i])
                order[1].append(Batch[1][i])
                order[2].append(Batch[2][i])
        # Batch=order

        # order = [[], [],[]]

        # s = Batch[0][0]
        # rang=range(0, len(Batch[1])-1)
        # if len(rang)>0:
        #     for i in rang:
        #         if Batch[1][i] == Batch[1][i + 1]:
        #             s = s + Batch[0][i + 1]
        #         else:
        #             order[0].append(s)
        #             order[1].append(Batch[1][i])
        #             order[2].append(Batch[2][i])
        #             s = Batch[0][i + 1]
        #         if i == len(Batch[1]) - 2:
        #             order[0].append(s)
        #             order[1].append(Batch[1][i + 1])
        #             order[2].append(Batch[2][i + 1])
        Batch = order
        return deepcopy(Batch)
    # add  temps to Batch {Batch[3] temps}
    def add_temps(self, Batch):
        # tempe d'injection

        tem_inj = []
        for i in Batch[0]:
            # tempe_inj = inj / pom_inj
            temp = random.randint(int(i * 100 / co_pom_inj[1]),int(i * 100 / co_pom_inj[1]))
            tem_inj.append(round(float(temp) / 100, 2))
        Batch.append(tem_inj)
        return deepcopy(Batch)
    def evalutation(self, Batch):
        s = 0
        for i in range(0, len(Batch[1]) - 2):
            s = s + cont_entr[Batch[1][i]][Batch[1][i + 1]]
        return deepcopy(s)

    def act_bath_en(self, qnti, bath_en,  qnti_resp, Localdep, Demdepo2, ndepo):
        # len_b lengeur de batch
        qnti_local =deepcopy(qnti)     
        len_b = len(bath_en[0]) 
        while qnti_local != 0 :
            # qnti_ran random qantit
            qnti_ran = random.randint(1,qnti_local)
            # dep_ran random depo
            dep_ran = random.randint(0,ndepo-1)
            while qnti_ran != 0 :
                s=0
                i=0
                while i < len_b :
                    s+=bath_en[0][i]
                    if Localdep[dep_ran]<=s:
                        ty_p_r=bath_en[1][i]
                        nb_p_r=bath_en[2][i]
                        if i!=0:
                            # qr_ar qantiti acsepti areseptioni de type 
                            qr_ar=Localdep[dep_ran]-(s-bath_en[0][i])
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
                        bath_en[0][0]+= qr_ar
                        qnti_resp[dep_ran][ty_p_r].append([qr_ar,nb_p_r])
                        qnti_resp[dep_ran][ty_p_r].append([qr_ar,nb_p_r])
                        qnti_ran -= qr_ar
                        qnti_local -= qr_ar
                        break
                    i+=1
        return deepcopy(bath_en), deepcopy(qnti_resp)
    def genirisolition(self, Batch_n, flag_g):
        fin = False
        j = 0
        # afficahe chromosome A
        if j >= flag_g:
            Batch = self.geniri_Batch()
        else:
            Batch = deepcopy(Batch_n)
        while fin == False:
            if j != 0:
                Batch = self.geniri_Batch()
            # for i in Batch :
            i = 0
            j += 1
            while (fin == False and i < n_c_a):
                i += 1
                Batch = self.rand_seq_bat(Batch)  # b chromo alea  prd essayer
                fin = self.seq_inter(Batch) and fonction.double(Batch[1])  # ver seq interdit
                if (not fin and j > n_c_a * p_c_c):  # sol corrigie apres 80 % %
                    Batch = self.corec_seq_inter(Batch)
                    fin = self.seq_inter(Batch) and fonction.double(Batch[1])
        Batch = self.sup_double(Batch)  # chromo final
        self.solition = Batch
        Batch[0].append(volumebatch)
        Batch[1].append(0)
        Batch.append([])
        Batch.append([])
        Demdepo1 = deepcopy(Demdepo)
        for j in range(0, nprod):
            for i in range(0, ndepo):
                Demdepo1[i][j] = Demdepo[i][j] * temps_sum
        bath_en = deepcopy(bathint)
        rang = list(range(0, ndepo))[::-1]
        rang1 = list(range(0, nprod))[::-1]
        Demdepo2 = Demdepo1
        le = len(Batch[0])
        for i in range(0, le):
            qnti = Batch[0][i]
            typ = Batch[1][i]
            bath_en[0].insert(0, 0)
            bath_en[1].insert(0, typ)
            bath_en[2].insert(0, i + 1)
            
            qnti_resp=deepcopy(qnti_resp_def) 
            bath_en, qnti_resp = self.act_bath_en(qnti, bath_en, qnti_resp, Localdep, Demdepo2, ndepo)
            bath_en = self.sup_double_2(bath_en)
            Batch[2].append(deepcopy(qnti_resp))
            Batch[3].append(deepcopy(bath_en))
        return deepcopy(Batch)

class population:
    def __init__(self, max_dem_pr, nombre_initial_population=50, Batch_ns=None, flag_gs=0, dely=33):
        self.nombre_initial_population = nombre_initial_population

        self.individus = self.genu_individus(Batch_ns, flag_gs, dely)
        self.classement_po = self.classement_ind()
        self.p = self.calcu_prob()

    # daily  due data & qté
    def contrent_dem(self, Batch, Demdepo, dely=24):
        Demdepo0 = fonction.lis(ndepo, nprod, 0)
        fin = True
        t_s = 0
        for i in range(len(Batch[0])):
            tem = Batch[4][i]
            t_s += tem
            j = 1
            while (t_s >= dely or j == 1) and fin == True:
                j = 0
                if t_s < dely:
                    for d in range(ndepo):
                        for p in range(nprod):
                            Demdepo0[d][p] += Batch[2][i][d][p]
                elif t_s == dely:
                    for d in range(ndepo):
                        for p in range(nprod):
                            nfin = Demdepo0[d][p] >= Demdepo[d][p]
                            fin = fin and nfin
                            Demdepo0[d][p] -= Demdepo[d][p]
                    t_s = 0

                else:

                    t_t_s = (tem - (t_s - dely)) / tem
                    in_t_t_s = 1 - t_t_s
                    t_s = tem * in_t_t_s
                    for d in range(ndepo):
                        for p in range(nprod):
                            Demdepo0[d][p] += t_t_s * Batch[2][i][d][p]
                            nfin = Demdepo0[d][p] >= Demdepo[d][p]
                            fin = \
                                nfin
                            Demdepo0[d][p] -= Demdepo[d][p]
                            Demdepo0[d][p] += in_t_t_s * Batch[2][i][d][p]

            if fin == False:
                break
        return fin

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

    def genu_individus(self, Batch_ns, flag_gs, dely):
        individus = []
        for v in range(self.nombre_initial_population):
            fin = True
            i = 0

            while fin:

                try:
                    if i == 0:
                        if Batch_ns == None:
                            sol = individu(max_dem_pr)
                        else:
                            sol = individu(max_dem_pr, Batch_ns[v], flag_gs)
                        i += 1
                    if sol.solition != None:
                        if cont_dem:
                            if self.contrent_dem(sol.solition, Demdepo, dely):
                                individus.append(sol)
                                fin = False
                                i = 0
                            else:
                                ll = [deepcopy(sol.solition[0]), deepcopy(sol.solition[1])]
                                # sol = individu(max_dem_pr, sol.solition, 1)
                                sol = individu(max_dem_pr, ll, 1)
                        else:
                            individus.append(sol)
                            fin = False
                            i = 0
                    else:
                        sol = individu(max_dem_pr)
                        i += 1

                except Exception as er:
                    # exc_type, exc_obj, exc_tb = sys.exc_info()
                    # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    # print(exc_type, fname, exc_tb.tb_lineno,er)
                    print(traceback.format_exc())
                    # sys.exit('listofitems not long enough')
                    pass
                tempe_depas(' 2')

        return individus

    def new_population(self):
        new_individus = []
        ta = int(round(t_population * 0.01))
        ta2 = t_population - ta
        t = 0
        while t < ta:
            ii = int(random.uniform(0, t_population - 1))
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

        return deepcopy(new_individus)

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
            aa = random.uniform(0, 1)
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
        for i in range(len(l2)):
            try:
                if l2[i] in l1[1]:
                    j = l1[1][:-1].index(l2[i])
                    l3[0].append(l1[0][j])
                    l3[1].append(l1[1][j])
                    l1[0].pop(j)
                    l1[1].pop(j)

            except Exception as er:
                # exc_type, exc_obj, exc_tb = sys.exc_info()
                # fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                # # print(exc_type, fname, exc_tb.tb_lineno,er)
                print(traceback.format_exc())
                # sys.exit('listofitems not long enough')
                pass
        l1[0] = l3[0] + l1[0]
        l1[1] = l3[1] + l1[1]
        return deepcopy(l1)

    def mutation(self, i1):
        ta = int(round(nb * 0.1))
        f = 0
        while f < ta:
            i = int(random.uniform(0, nb))
            j = int(random.uniform(0, nb))
            n = i1[1][i]
            m = i1[0][i]
            i1[1][i] = i1[1][j]
            i1[0][i] = i1[0][j]
            i1[1][j] = n
            i1[0][j] = m
            f += 1
        return deepcopy(i1)
def add_stok(sol):
    stok = fonction.lis(ndepo, nprod, 0)
    l = sol[2]
    l_stok = []
    for n in range(0,len(l)):
        for i in r_ndepo:
            for j in r_nprod:
                s = 0
                for k in l[n][i][j]:
                    s += k[0]
                stok[i][j] += deepcopy(s)
        l_stok.append(deepcopy(stok))
    sol.append(l_stok)
    return deepcopy(sol)
def update_res(st):
    b=log_res.objects.filter(id_page=1)
    b.update(res=st)
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
    global ndepo
    ndepo = data_entr['id_ndepo']
    global r_ndepo
    r_ndepo = range(ndepo)
    global nb
    nb = data_entr['id_nb'] - 1
    global t_population
    t_population = data_entr['id_t_population']
    global crit_dar
    crit_dar = data_entr['id_crit_dar']
    global delai_fin
    delai_fin = data_entr['id_delai_fin']
    global temps_sum
    temps_sum = data_entr['id_temps_sum']  # par jour  hmax
    global Demdepo
    Demdepo = data_entr['id_Demdepo']
    global bathint
    bathint = data_entr['id_bathint']
    bathint.append([])
    for i in range(len(bathint[0])):
        bathint[2].append(0)

    global cont_dem
    cont_dem = data_entr['id_cont_dem']
    global cont_entr
    cont_entr = data_entr['id_cont_entr']
    global Localdep
    Localdep = data_entr['id_Localdep'][0]
    global co_pom_inj
    co_pom_inj = data_entr['id_co_pom_inj']
    global volumebatch
    volumebatch = data_entr['id_volumebatch']
    global max_dem_pr
    max_dem_pr = []
    print('___________________________________________________________'+str(crit_dar))
    global qnti_resp_def
    qnti_resp_def=fonction.lis(ndepo, nprod, 0)
    for i in range(0, nprod):
        s = 0
        for j in range(0, ndepo):
            s = s + Demdepo[j][i]
            qnti_resp_def[j][i]=[]
        max_dem_pr.append(s * temps_sum)
    for i in range(0, len(bathint[1])):
        max_dem_pr[bathint[1][i]] -= bathint[0][i]





    print('population install ')
    update_res('population install ')
    po = population(max_dem_pr, t_population)
    # classemen des cromo pub initial
    print  ('_______   ',po.classement_po)
    min_indu = po.individus[po.classement_po[0]]
    min_fo = min_indu.fo

    iii = 0
    while iii < crit_dar:
        print('iteration ',iii,'  ',min_indu.fo)
        st='iteration '+str(iii)+'  '+str(min_indu.fo)
        old=get_res()
        st=str(old)+"<br/>"+st
        update_res(st)
        time.sleep(3)
        po = po.new_population()  # tt etap d'AG

        npo = population(max_dem_pr, t_population, po, 1)
        min_indu2 = npo.individus[npo.classement_po[0]]
        if min_fo > min_indu2.fo:
            min_indu = min_indu2
            min_fo = min_indu2.fo
        po = deepcopy(npo)
        iii += 1
    min_indu.solition =add_stok(min_indu.solition)
    return deepcopy(min_indu)
if __name__ == "__main__":
    print('                     ********                            ')

    s_min = gin_AG()
    print('                     ********                            ')