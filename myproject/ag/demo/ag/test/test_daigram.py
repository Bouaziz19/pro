def load_src(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))


load_src("fonction", "../fonction.py")
import webbrowser,os,fonction
import xml.etree.ElementTree as ET
import fonction
a = fonction.gen()


# pour  modifi
volumebatch=40# cap max pipeline
type0 = [0, 1,2]
Volume0=[14,6,20] #old batch  autre sense
bathint =[Volume0,type0]
produits =["p1","p2","p3"]
s_min=[
    #qentiti injection
    [1, 1, 2, 6, 18, 13, 5, 34, 40],
    # type produit  injection
       [0, 2, 0, 2, 0, 2, 0, 1, 0],
        # resption pour  chaque batche
       [[[0, 1, 0], [0, 0, 0]],
        [[0, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 2]],
        [[0, 0, 0], [0, 0, 6]],
        [[11, 0, 5], [2, 0, 0]],
        [[0, 0, 2], [0, 0, 11]],
        [[4, 0, 0], [0, 0, 1]],
        [[0, 3, 13], [18, 0, 0]],
        [[5, 15, 0], [0, 20, 0]]],

       # les batch
        [[[15, 5, 20], [0, 1, 2]],
        [[1, 15, 4, 20], [2, 0, 1, 2]],
        [[2, 1, 15, 4, 18], [0, 2, 0, 1, 2]],
        [[6, 2, 1, 15, 4, 12], [2, 0, 2, 0, 1, 2]],
        [[18, 2, 4, 4, 12], [0, 2, 0, 1, 2]],
        [[13, 22, 4, 1], [2, 0, 1, 2]],
        [[5, 13, 18, 4], [0, 2, 0, 1]],
        [[31, 5, 4], [1, 0, 1]],
        [[40], [0]]],
 #temp
    [0.08, 0.09, 0.15, 0.53, 1.42, 0.88, 0.47, 2.38, 3.36]]
#  fin modification
print (s_min)
temp=[]
qr=[]
ip=[]
inj=[]
i_inj=[]
res=[]
t_s=0
for i in xrange(len(s_min[1])):
    qr1=[]
    ip1=[]
    for j in s_min[3][i][0]:
        qr1.append([100*(float(j) / volumebatch),j])
    qr.append(qr1)
    for j in s_min[3][i][1]:
        ip1.append(j)
    ip.append(ip1)
    inj.append(s_min[0][i])
    i_inj.append(s_min[1][i])
    res.append(s_min[2][i])
    t_s +=s_min[4][i]
    temp.append(t_s)
n_bathint=[[],[]]
for j in bathint[0]:
    n_bathint[0].append([100*(float(j) / volumebatch),j])
n_bathint[1]=bathint[1]

b = a.progresss(1100,qr,ip,produits,inj,i_inj,res,4,n_bathint,temp)

fonction.indent(b)
c = ET.tostring(b)

#print c


script_dir = os.path.dirname(__file__)

rel_path = "..\output\index.html"
abs_file_path = os.path.join(script_dir, rel_path)
f = open(abs_file_path, 'w')

f.write(c)
webbrowser.open(abs_file_path);