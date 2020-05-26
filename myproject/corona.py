import  random
L = 15 # taille de la grille L*L
P = 800 # nombre d’habitants
n_malade_init = 3 # nombre initial de malades
njour = 200 # duree de la simulation
proba_deplacement = 0.9 # p_move
proba_contagion = 0.06 # p_cont
duree_maladie = 20 # Nmax

def creation(P,L,n_malade_init):
    habitants=[]
    for i in range(P):
        x = random.randint(0, L)
        y = random.randint(0, L)
        if i<n_malade_init:
            habitant=[x,y,0]
        else:
            habitant = [x, y, 1]
        habitants.append(habitant)
    return habitants

def deplacement (list_populations,proba_deplacement):
    len_p=len(list_populations)
    numb_dep=int(len_p * proba_deplacement)
    for i in range(numb_dep):
        index = random.randint(0, len_p)
        x = random.randint(0, L)
        y = random.randint(0, L)
        list_populations[index][0] = x
        list_populations[index][1] = y
    return list_populations

def evolution(list_populations,duree_maladie,liste_evolution):
    len_p = len(list_populations)
    for i in range(len_p):
        if list_populations[i][2]==0:
            liste_evolution[i]=liste_evolution[i]+1
        if liste_evolution[i]==duree_maladie:
            list_populations[i][2]=1
            liste_evolution[i]=0
    return liste_evolution

def contagion(list_populations,L,proba_contagion,duree_maladie):
    len_p = len(list_populations)
    lieu=[]
    for i in range(len_p):
        if list_populations[i][2]==0:
            x=list_populations[i][0]
            y=list_populations[i][1]
            lieu.append([x,y])


liste_evolution=[]
for i in range(P):
    liste_evolution.append(0)
list_populations =creation(P,L,n_malade_init)
liste_evolution= evolution(list_populations,duree_maladie,liste_evolution)
list_populations_2 =deplacement (list_populations,proba_deplacement)
liste_evolution= evolution(list_populations_2,duree_maladie,liste_evolution)