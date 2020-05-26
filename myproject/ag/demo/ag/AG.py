###!/usr/bin/env python
# *-* coding: utf8 *-*
import traceback, os
xrange =range
if True:
    import random, sys, time
    from copy import deepcopy
    from ag import entr, fonction
    n_c_a=50
    p_c_c=0.2

    # def xrange(n):
    #     return list(range(0,n))

    nprod = entr.nprod
    r_nprod = range(nprod)

    ndepo = entr.ndepo
    r_ndepo = range(ndepo)
    nb = entr.nb - 1
    print (nb)
    t_population = entr.t_population
    crit_dar = entr.crit_dar
    delai_fin = entr.delai_fin
    temps_sum = entr.temps_sum  # par jour  hmax
    Demdepo = entr.Demdepo
    bathint = entr.bathint
    bathint.append([])
    for i in range(len(bathint[0])):
        bathint[2].append(0)

    cont_dem = entr.cont_dem
    cont_entr = entr.cont_entr
    Localdep = entr.Localdep
    co_pom_inj = entr.co_pom_inj
    volumebatch = entr.volumebatch
    max_dem_pr = []
    for i in range(0, entr.nprod):
        s = 0
        for j in range(0, entr.ndepo):
            s = s + Demdepo[j][i]
        max_dem_pr.append(s * temps_sum)
    for i in range(0, len(bathint[1])):
        max_dem_pr[bathint[1][i]] -= bathint[0][i]


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

    def calu_qnti_ac(self, bath_en, Localdep_inv, qnti_ac, rang2, rang):
        s = 0

        for z in rang:
            qnti = bath_en[0][0]
            s = 0
            for j in rang2:
                s = s + bath_en[0][j]
                if s > Localdep_inv[0][z]:
                    delta = s - Localdep_inv[0][z]
                    ll = [delta, bath_en[0][j], qnti]
                    var = min(ll)
                    qnti_ac[z][bath_en[1][j]] += var
                    qnti -= var

        return deepcopy(qnti_ac)

    def act_bath_en(self, qnti, bath_en, rang2, qnti_ac, Localdep_inv, Demdepo2, a):
        qnti_resp = fonction.lis(ndepo, nprod)
        qnti_resp2 = fonction.lis(ndepo, nprod)
        cum_bath_en = []
        s = 0
        for i in rang2:
            s += bath_en[0][i]
            cum_bath_en.insert(0, s)
        random.shuffle(a)
        for j in a:
            jj = j[1]
            ii = j[0]
            qnti_resp2[ii][jj] = []
            if qnti != 0:
                if qnti_ac[ii][jj] != 0:
                    for zz in rang2:
                        if (bath_en[1][zz] == jj and qnti_ac[ii][jj] != 0):
                            if cum_bath_en[zz] > Localdep_inv[0][ii]:
                                delta = cum_bath_en[zz] - Localdep_inv[0][ii]
                                l = [bath_en[0][zz], qnti_ac[ii][jj], delta, qnti, Demdepo2[ii][jj]]
                                va = min(l)
                                qnti_resp[ii][jj] += va
                                if va != 0:
                                    qnti_resp2[ii][jj].append([va, bath_en[2][zz]])
                                qnti_ac[ii][jj] -= va
                                Demdepo2[ii][jj] -= va
                                bath_en[0][zz] -= va
                                qnti -= va

        return deepcopy(bath_en), deepcopy(qnti_resp2)

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

        Localdep_inv = deepcopy(Localdep)
        Demdepo1 = deepcopy(Demdepo)
        for j in range(0, nprod):
            for i in range(0, ndepo):
                Demdepo1[i][j] = Demdepo[i][j] * temps_sum
        bath_en = deepcopy(bathint)

        for i in range(0, len(Localdep[0])):
            Localdep_inv[0][i] = volumebatch - Localdep[0][i]
            Localdep_inv[1][i] = volumebatch - Localdep[1][i]
        rang = list(range(0, ndepo))[::-1]
        rang1 = list(range(0, nprod))[::-1]
        n = []
        m = rang * nprod
        for ra in rang1:
            n1 = []
            n1.append(ra)
            n += n1 * ndepo
        a = list(zip(m, n))
        Demdepo2 = Demdepo1
        le = len(Batch[0])
        for i in range(0, le):

            qnti_ac = fonction.lis(ndepo, nprod)  # qentiti  poue depot pent reception

            qnti = Batch[0][i]
            typ = Batch[1][i]
            bath_en[0].insert(0, qnti)
            bath_en[1].insert(0, typ)
            bath_en[2].insert(0, i + 1)

            rang2 = list(range(0, len(bath_en[0])))[::-1]
            qnti_ac = self.calu_qnti_ac(bath_en, Localdep_inv, qnti_ac, rang2, rang)
            bath_en, qnti_resp = self.act_bath_en(qnti, bath_en, rang2, qnti_ac, Localdep_inv, Demdepo2, a)
            # print('_________f__zff______')
            # # print(qnti_resp)
            # print(qnti_resp2)





            bath_en = self.sup_double_2(bath_en)

            Batch[2].append(deepcopy(qnti_resp))
            Batch[3].append(deepcopy(bath_en))

            if i == le - 1:
                if Demdepo2 != fonction.lis(ndepo, nprod, 0):
                    Batch = None
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
                    # # print(exc_type, fname, exc_tb.tb_lineno,er)
                    # print(traceback.format_exc())
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
                # print(traceback.format_exc())
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
    for n in xrange(len(l)):
        for i in r_ndepo:
            for j in r_nprod:
                s = 0
                for k in l[n][i][j]:
                    s += k[0]
                stok[i][j] += deepcopy(s)
        l_stok.append(deepcopy(stok))
    sol.append(l_stok)
    return deepcopy(sol)

def gin_AG():
    # print'population install '
    po = population(max_dem_pr, t_population)
    # classemen des cromo pub initial
    # print  ('_______   ',po.classement_po)
    min_indu = po.individus[po.classement_po[0]]
    min_fo = min_indu.fo

    iii = 0
    while iii < crit_dar:
        # print'iteration ',iii,'  ',min_indu.fo
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


