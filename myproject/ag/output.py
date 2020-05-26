import xml.etree.ElementTree as ET
import os, random,time
from ag import AG,fonction
from app.models import log_res
def get_res():
    a = fonction.gen()
    #creation
    s_min=AG.gin_AG()
    # print('ggggggggggggggg')
    
    # for i in range(0,len(s_min.solition[0])):
    #     print (s_min.solition[0][i], '//', s_min.solition[1][i], '//', s_min.solition[2][i], '//', s_min.solition[3][i], '//', s_min.solition[4][i], '//')
    print ('////////////////////////////')
    print ('s_min.solition[0]',s_min.solition[0])
    print ('s_min.solition[1]',s_min.solition[1])
    print ('s_min.solition[2]',s_min.solition[2])
    print ('s_min.solition[3]',s_min.solition[3])
    print ('s_min.solition[4]',s_min.solition[4])
    print ('s_min.solition[5]',s_min.solition[5])
    # def xrange(n):
    #     return list(range(0, n))
    temp=[]
    qr=[]
    ip=[]
    inj=[]
    i_inj=[]
    res=[]
    res2 = []
    t_s=0
    for i in range(0,len(s_min.solition[1])):
        qr1=[]
        ip1=[]
        v_i=0
        for j in s_min.solition[3][i][0]:
            qr1.append([100*(float(j) / AG.volumebatch),j,s_min.solition[3][i][2][v_i]])
            v_i+=1
        qr.append(qr1)
        for j in s_min.solition[3][i][1]:
            ip1.append(j)
        ip.append(ip1)
        inj.append(s_min.solition[0][i])
        i_inj.append(s_min.solition[1][i])
        # print '__________'
        # print s_min.solition[2][i]      
        res.append(s_min.solition[2][i])
        lll2=[]
        for l4 in s_min.solition[5][i]:
            lll1 = []
            l6 = 0
            for l5 in l4:
                if l5 != 0:
                    lll1.append([[l5, l6]])
                else:
                    lll1.append([])
                l6 += 1
            lll2.append(lll1)
        res2.append(lll2)
        # print ('gggggggggggg',res)
        # print (res2)
        t_s+=s_min.solition[4][i]
        temp.append(round(t_s, 1))
    n_bathint=[[],[]]
    for j in AG.bathint[0]:
        n_bathint[0].append([100*(float(j) / AG.volumebatch),j,0])
    n_bathint[1]=AG.bathint[1]
    fo=s_min.fo
    b = a.progresss(1100,qr,ip,AG.produits,inj,i_inj,res,4,n_bathint,temp,fo,res2)
    fonction.indent(b)
    c = ET.tostring(b)
    c = c.decode("utf-8")
    AG.update_res(c)
    # script_dir = os.path.dirname(__file__)
    # rel_path = "output\index.html"
    # abs_file_path = os.path.join(script_dir, rel_path)
    # f = open(abs_file_path, 'w')
    # f.write(c)
    # webbrowser.open(abs_file_path);
    return c
# print (get_res())