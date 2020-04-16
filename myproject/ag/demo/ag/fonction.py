#!/usr/bin/env python
# *-* coding: utf8 *-*

import random
import numpy as np
import sys
import xml.etree.ElementTree as ET
from copy import deepcopy


def xrange(n):
    return list(range(0, n))
color = ['Blue', 'Orange', 'Red', 'Green', 'Bisque', 'Yellow','Black', 'BlanchedAlmond', 'BlueViolet',
                 'Brown', 'BurlyWood', 'Chartreuse', 'Chocolate', 'Coral', 'CornflowerBlue', 'Cornsilk', 'Crimson',]

def double(l):
    for i in range(0,len(l)-1):
        if (l[i] == l[i + 1]):
            return False
    return True
def lis(x=0,y=0,z=0):
    a=[]
    for i in range(0,x):
        b=[]
        if y>0:
            b=[z]*y
        else :
            b=[]
        a.append(b)
    return a
def generater_random_list(num, v_min=0, v_max=1,step=0):
    # print num,v_min,v_max
    rand_list = []
    fin=True
    s=0
    while fin:
        if step:
            rand_num = random.randrange(v_min, v_max,step) 
        else:
            rand_num = random.randint(v_min, v_max)
            
        s+=rand_num
        if s<num:
            rand_list.append(rand_num)
        else:
            fin=False
    l=[index for index, value in enumerate(rand_list) if value < v_max]
    il=list(xrange(len(l)))
    d=num- sum(rand_list)
    if len(il)==0 and num<v_max:
        rand_list.append(num)
        return rand_list
    while d:
        ii=random.choice(il)
        il.remove(ii)
        dd=v_max-rand_list[l[ii]]
        if dd>=d:
            rand_list[l[ii]]+=d
            d=0
        else:
            rand_list[l[ii]]=v_max
            d-=dd
    return deepcopy(rand_list)
def generater_random_list2(num,nb):
    x = np.random.multinomial(num, np.ones(nb)/nb, size=1)[0]
    return x




class gen():
    def __init__(self):
        pass

    def svg2(self, color="red"):
        svg = ET.Element('svg')
        svg.attrib["height"] = '38pt'
        svg.attrib["width"] = '32pt'
        svg.attrib["viewBox"] = '0 0 38 38'
        path = ET.Element('path')
        path.attrib["d"] = "M 19 36.417969 C 11.152344 36.417969 6.332031 34.113281 6.332031 32.457031 C 6.332031 32.171875 6.472656 31.871094 6.746094 31.5625 C 7.035156 31.234375 7.007812 30.734375 6.679688 30.445312 C 6.578125 30.355469 6.457031 30.304688 6.332031 30.277344 L 6.332031 8.171875 C 8.859375 10.074219 14.035156 11.082031 19 11.082031 C 23.964844 11.082031 29.140625 10.074219 31.667969 8.171875 L 31.667969 30.277344 C 31.542969 30.304688 31.421875 30.355469 31.320312 30.445312 C 30.992188 30.734375 30.964844 31.234375 31.253906 31.5625 C 31.527344 31.871094 31.667969 32.171875 31.667969 32.457031 C 31.667969 34.113281 26.847656 36.417969 19 36.417969 Z M 19 36.417969 "
        path.attrib["fill"] = "black"
        svg.append(path)
        path = ET.Element('path')
        path.attrib["d"] = "M 21.5 36.332031 C 21.519531 36.328125 21.539062 36.328125 21.558594 36.328125 C 27.101562 35.9375 31.554688 34.316406 31.667969 32.402344 C 31.667969 32.183594 31.480469 31.816406 31.253906 31.5625 C 31.058594 31.34375 31.019531 31.042969 31.109375 30.785156 C 29.519531 29.003906 24.699219 27.707031 19 27.707031 C 13.300781 27.707031 8.480469 29.003906 6.890625 30.785156 C 6.980469 31.042969 6.941406 31.34375 6.746094 31.5625 C 6.519531 31.816406 6.375 32.183594 6.332031 32.53125 C 6.589844 34.253906 10.898438 35.9375 16.441406 36.328125 C 16.460938 36.328125 16.480469 36.328125 16.5 36.332031 C 16.882812 36.359375 17.273438 36.378906 17.667969 36.394531 C 18.105469 36.40625 18.546875 36.417969 19 36.417969 C 19.453125 36.417969 19.894531 36.40625 20.332031 36.394531 C 20.726562 36.378906 21.117188 36.359375 21.5 36.332031 Z M 21.5 36.332031 "
        path.attrib["fill"] = color
        svg.append(path)
        path = ET.Element('path')
        path.attrib["d"] = "M 19 0 C 12.09375 0 4.75 1.941406 4.75 5.542969 L 4.75 32.457031 C 4.75 36.058594 12.09375 38 19 38 C 25.90625 38 33.25 36.058594 33.25 32.457031 L 33.25 5.542969 C 33.25 1.941406 25.90625 0 19 0 Z M 19 0 "
        path.attrib["fill"] = "black"
        svg.append(path)
        path = ET.Element('path')
        path.attrib["d"] = "M 19 1.582031 C 26.847656 1.582031 31.667969 3.886719 31.667969 5.542969 C 31.667969 7.195312 26.847656 9.5 19 9.5 C 11.152344 9.5 6.332031 7.195312 6.332031 5.542969 C 6.332031 3.886719 11.152344 1.582031 19 1.582031 Z M 19 1.582031 "
        path.attrib["fill"] = color
        svg.append(path)
        path = ET.Element('path')
        path.attrib["d"] = "M 19 36.417969 C 11.152344 36.417969 6.332031 34.113281 6.332031 32.457031 C 6.332031 32.171875 6.472656 31.871094 6.746094 31.5625 C 7.035156 31.234375 7.007812 30.734375 6.679688 30.445312 C 6.578125 30.355469 6.457031 30.304688 6.332031 30.277344 L 6.332031 8.171875 C 8.859375 10.074219 14.035156 11.082031 19 11.082031 C 23.964844 11.082031 29.140625 10.074219 31.667969 8.171875 L 31.667969 30.277344 C 31.542969 30.304688 31.421875 30.355469 31.320312 30.445312 C 30.992188 30.734375 30.964844 31.234375 31.253906 31.5625 C 31.527344 31.871094 31.667969 32.171875 31.667969 32.457031 C 31.667969 34.113281 26.847656 36.417969 19 36.417969 Z M 19 36.417969 "
        path.attrib["fill"] = color
        svg.append(path)
        path = ET.Element('path')
        path.attrib["d"] = "M 12.886719 27.421875 C 11.796875 27.613281 10.777344 27.855469 9.859375 28.140625 C 9.441406 28.273438 9.210938 28.714844 9.339844 29.132812 C 9.445312 29.46875 9.757812 29.6875 10.097656 29.6875 C 10.175781 29.6875 10.253906 29.675781 10.332031 29.652344 C 11.1875 29.386719 12.136719 29.160156 13.160156 28.980469 C 13.589844 28.90625 13.878906 28.496094 13.800781 28.066406 C 13.726562 27.632812 13.316406 27.34375 12.886719 27.421875 Z M 12.886719 27.421875 "
        path.attrib["fill"] = "black"
        svg.append(path)
        path = ET.Element('path')
        path.attrib["d"] = "M 28.164062 28.148438 C 27.25 27.863281 26.234375 27.621094 25.140625 27.425781 C 24.699219 27.34375 24.296875 27.636719 24.222656 28.066406 C 24.144531 28.496094 24.433594 28.90625 24.863281 28.984375 C 25.890625 29.167969 26.839844 29.394531 27.6875 29.660156 C 27.769531 29.683594 27.847656 29.695312 27.925781 29.695312 C 28.261719 29.695312 28.574219 29.480469 28.683594 29.140625 C 28.8125 28.722656 28.578125 28.277344 28.164062 28.148438 Z M 28.164062 28.148438 "
        path.attrib["fill"] = "black"
        svg.append(path)
        path = ET.Element('path')
        path.attrib["d"] = "M 20.546875 26.945312 C 19.539062 26.90625 18.484375 26.90625 17.476562 26.945312 C 17.042969 26.960938 16.699219 27.328125 16.71875 27.765625 C 16.734375 28.203125 17.09375 28.574219 17.539062 28.527344 C 18.507812 28.492188 19.519531 28.492188 20.484375 28.527344 C 20.496094 28.53125 20.507812 28.53125 20.519531 28.53125 C 20.941406 28.53125 21.292969 28.195312 21.308594 27.769531 C 21.324219 27.332031 20.984375 26.964844 20.546875 26.945312 Z M 20.546875 26.945312 "
        path.attrib["fill"] = "black"
        svg.append(path)

        
        return deepcopy(svg)

    def svg(self,color="red",rot=0):
        svg = ET.Element('svg')
        svg.attrib["height"] = '28pt'
        svg.attrib["width"] = '28pt'
        svg.attrib["transform"] = 'rotate('+str(rot)+' 0 0)'
        svg.attrib["viewBox"] = '0 0 28 28'
        path1 = ET.Element('path')
        path1.attrib["d"] = "M 8.6875 20.535156 L 18.164062 20.535156 L 18.164062 " \
                            "11.058594 L 24.484375 11.058594 L 13.425781 0 L 2.371094" \
                            " 11.058594 L 8.6875 11.058594 Z M 8.6875 20.535156 "
        path1.attrib["fill"] = color
        path2 = ET.Element('path')
        path2.attrib["d"] = "M 2.371094 23.695312 L 24.484375 23.695312 L 24.484375 26.855469" \
                            " L 2.371094 26.855469 Z M 2.371094 23.695312 "
        path2.attrib["fill"] = color

        svg.append(path1)
        svg.append(path2)
        return deepcopy(svg)

    def table(self,inj=40, i_inj=0, res=[[0, 0, 0], [0, 0, 2]], spa=2,wi_t=7):
        
        trh = ET.Element('tr')
        trb = ET.Element('tr')
        # hader
        th = ET.Element('th')
        th.attrib["data-toggle"]="tooltip"
        th.attrib["data-placement"]="top"
        stt=str(inj)+'/'+str(i_inj)
        th.attrib["title"]=stt
        th.attrib["style"] = 'width: ' + str(wi_t) + '%;'
        span = ET.Element('span')
        span.text = stt
        th.append(span)
        trh.append(th)
        # body
        td = ET.Element('td')
        td.attrib["data-toggle"]="tooltip"
        td.attrib["data-placement"]="top"
        td.attrib["title"]=stt
        td.attrib["style"] = 'width: ' + str(wi_t) + '%;'
        td.append(self.svg(color[i_inj], rot=180))
        trb.append(td)

        t = 0
        for i in res:
            
            for j in xrange(spa+t):
                # hader
                th = ET.Element('th')
                th.attrib["style"] = 'width: ' + str(wi_t) + '%;'
                trh.append(th)
                # body
                td = ET.Element('td')
                td.attrib["style"] = 'width: ' + str(wi_t) + '%;'
                trb.append(td)
            t = 0
            n = 0
            for j in i:
                if j != []:
                    # hader
                    for kk in j :
                        th = ET.Element('th')
                        th.attrib["style"] = 'width: ' + str(wi_t) + '%;'
                        
                        th.attrib["data-toggle"]="tooltip"
                        th.attrib["data-placement"]="top"
                        stt=str(kk[0])+'/'+str(kk[1])
                        th.attrib["title"]=stt
                        span = ET.Element('span')
                        span.text = str(kk[0])
                        th.append(span)
                        trh.append(th)
                        # body
                        td = ET.Element('td')
                        td.attrib["style"] = 'width: ' + str(wi_t) + '%;'
                        td.attrib["data-toggle"]="tooltip"
                        td.attrib["data-placement"]="top"
                        td.attrib["title"]=stt
                        td.append(self.svg(color[n], rot=0))
                        trb.append(td)
                else:
                    t+=1
                n += 1


        thead = ET.Element('thead')
        thead.append(trh)
        tbody = ET.Element('tbody')
        tbody.append(trb)
        table = ET.Element('table')
        table.append(thead)
        table.append(tbody)
        return deepcopy(table)

    def table2(self, inj=40, i_inj=0, res=[[0, 0, 0], [0, 0, 2]], spa=2, wi_t=7):

        trh = ET.Element('tr')
        trb = ET.Element('tr')
        # hader
        th = ET.Element('th')
        th.attrib["data-toggle"] = "tooltip"
        th.attrib["data-placement"] = "top"
        stt = str(inj) + '/' + str(i_inj)
        th.attrib["title"] = stt
        th.attrib["style"] = 'width: ' + str(wi_t) + '%;'
        span = ET.Element('span')
        span.text = stt
        th.append(span)
        trh.append(th)
        # body
        td = ET.Element('td')
        td.attrib["data-toggle"] = "tooltip"
        td.attrib["data-placement"] = "top"
        td.attrib["title"] = stt
        td.attrib["style"] = 'width: ' + str(wi_t) + '%;'
        # td.append(self.svg2(color[i_inj]))
        trb.append(td)

        t = 0
        for i in res:

            for j in xrange(spa + t):
                # hader
                th = ET.Element('th')
                th.attrib["style"] = 'width: ' + str(wi_t) + '%;'
                trh.append(th)
                # body
                td = ET.Element('td')
                td.attrib["style"] = 'width: ' + str(wi_t) + '%;'
                trb.append(td)
            t = 0
            n = 0
            for j in i:
                if j != []:
                    # hader
                    for kk in j:
                        th = ET.Element('th')
                        th.attrib["style"] = 'width: ' + str(wi_t) + '%;'

                        th.attrib["data-toggle"] = "tooltip"
                        th.attrib["data-placement"] = "top"
                        stt = str(kk[0]) + '/' + str(kk[1])
                        th.attrib["title"] = stt
                        span = ET.Element('span')
                        span.text = str(kk[0])
                        th.append(span)
                        trh.append(th)
                        # body
                        td = ET.Element('td')
                        td.attrib["style"] = 'width: ' + str(wi_t) + '%;'
                        td.attrib["data-toggle"] = "tooltip"
                        td.attrib["data-placement"] = "top"
                        td.attrib["title"] = stt
                        td.append(self.svg2(color[n]))
                        trb.append(td)
                else:
                    t += 1
                n += 1

        thead = ET.Element('thead')
        thead.append(trh)
        tbody = ET.Element('tbody')
        tbody.append(trb)
        table = ET.Element('table')
        table.append(thead)
        table.append(tbody)
        return deepcopy(table)

    def progress(self, width=1150):
        progress = ET.Element('div')
        progress.attrib["class"] = 'progress'
        progress.attrib["style"] = 'width: ' + str(width) + 'px;'
        return progress

    def progress_bar(self, width=[40,00],back_color='red',text=''):
        progress_bar = ET.Element('div')
        progress_bar.attrib["class"] = 'progress-bar'
        progress_bar.attrib["role"] = 'progressbar'
        progress_bar.attrib["style"] = 'width:' + str(width[0]) + '%;background-color:'+back_color+';'
        stt=text+'('+str(width[1])+')'+'/'+str(width[2])
        progress_bar.text = stt
        progress_bar.attrib["data-toggle"]="tooltip"
        progress_bar.attrib["data-placement"]="top"
        progress_bar.attrib["title"]=stt
        return progress_bar

    def progress_bars(self, volumebatch=40, l=[],ip=[],p=[]):
        a = self.progress(volumebatch)
        j = 0

        for i in l:
            if p == []:
                b = self.progress_bar(i)
            else:
                b = self.progress_bar(i,color[ip[j]], p[ip[j]])
            a.append(b)
            j = j + 1
        return a

    def progresss(self, volumebatch=40, ll=[],ip=[] ,p=[],inj=0,i_inj=0,res=[[0, 0, 0], [0, 0, 2]],spa=2,bathint=[],temp=[],fo=0,res2=[[0, 0, 0], [0, 0, 2]]):
        html = ET.Element('html')
        html.attrib["lang"] = 'en'
        head = ET.Element('head')
        title = ET.Element('title')
        title.text = "Plannig  optimal "
        link = ET.Element('link')
        link.attrib["rel"] = 'stylesheet'
        link.attrib["href"] = 'dist/css/bootstrap.min.css'
        script = ET.Element('script')
        script.attrib["src"] = 'dist/js/bootstrap.min.js'
        script.text = " "
        script2 = ET.Element('script')
        script2.text = """$(document).ready(function(){
                         $('[data-toggle="tooltip"]').tooltip();   
                            })"""
        head.append(title)

        head.append(link)
        head.append(script)
        head.append(script2)
        html.append(head)
        body = ET.Element('body')
        div = ET.Element('div')
        ol = ET.Element('ol')
        ol.attrib["style"] = 'margin: 0% -40%;line-height:685%;'
        li = ET.Element('ui')
        li.text='00- 00 '
        br = ET.Element('br')
        ol.append(li)
        ol.append(br)
        ne=0
        for i in temp:
            li = ET.Element('ui')
            li.text = str(ne)+' - '+str(i)
            ol.append(li)
            ol.append(br)
            ne=i

        div = ET.Element('div')
        div.attrib["style"] = 'float: left;margin: 1.7% 0%;width: 6%;'
        div.append(ol)
        body.append(div)
        container = ET.Element('div')
        container.attrib["class"] = 'container'
        container.attrib["style"] = "margin:0% 10%"

        h2 = ET.Element('h2')
        # <a href="#" data-toggle="tooltip" data-placement="top" title="Hooray!">Hover</a>
        # <a href="#" data-toggle="tooltip" data-placement="bottom" title="Hooray!">Hover</a>
        # <a href="#" data-toggle="tooltip" data-placement="left" title="Hooray!">Hover</a>
        # <a href="#" data-toggle="tooltip" data-placement="right" title="Hooray!">Hover</a>
        h2.attrib["data-toggle"]="tooltip"
        h2.attrib["data-placement"]="top"
        h2.attrib["title"]="Plannig  optimal "
        h2.text = 'Plannig  optimal '
        container.append(h2)
        b = self.progress_bars(volumebatch, bathint[0],bathint[1],p)
        container.append(b)
        j=0
        for i in ll:
            table = self.table(inj[j], i_inj[j], res[j], spa)
            table.attrib["style"] = 'width: ' + str(volumebatch) + 'px;'
            print (res[j])
            print (res2[j])
            table2 = self.table2(inj[j], i_inj[j], res2[j], spa)
            table2.attrib["style"] = 'width: ' + str(volumebatch) + 'px;'
            container.append(table)
            container.append(table2)
            b = self.progress_bars(volumebatch, i,ip[j],p)
            j=j+1
            container.append(b)
        div_f = ET.Element('div')
        div_f.attrib["class"] = 'panel-group text-center'
        div_f.attrib["style"] = 'width: 50%'
        h1 = ET.Element('h1')
        h1.text='***  f.o  *** '
        div_f.append(h1)
        pre = ET.Element('pre')
        h1_f = ET.Element('h1')
        h1_f.text = str(fo)
        pre.append(h1_f)
        div_f.append(pre)
        container.append(div_f)
        body.append(container)
        html.append(body)
        return html


def indent(elem, level=0):
    i = "\n" + level * "  "
    j = "\n" + (level - 1) * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem


