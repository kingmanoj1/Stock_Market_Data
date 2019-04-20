from django.shortcuts import render
from django.http import HttpResponse
import bs4 as bs
import requests
import json
import urllib.request
from matplotlib import pyplot as plt

# Create your views here.



def home(request):
    return render(request,'stockdata/home.html')


def index(request):

    if request.method=="POST":

        p1 = []
        data = urllib.request.urlopen("https://finance.yahoo.com/quote/AAPL/history?p=AAPL")
        sp = bs.BeautifulSoup(data, 'lxml')
        out = sp.find("table")

        for x in out:
            row = out.find_all('tr')
            for y in row:
                tt = y.find_all('td')
                for d in tt:
                    p1.append(d.text.strip())

        frm=request.POST.get('start','')
        too=request.POST.get('end','')
        print(frm,too)
        st=frm*7
        end=too*7

        return render(request,'stockdata/index.html',{'st':st,'end':end,'alldata':p1})


    else:
        p1=[]
        data=urllib.request.urlopen("https://finance.yahoo.com/quote/AAPL/history?p=AAPL")
        sp=bs.BeautifulSoup(data,'lxml')
        out=sp.find("table")

        for x in out:
            row=out.find_all('tr')
            for y in row:
                tt=y.find_all('td')
                for d in tt:
                    p1.append(d.text.strip())


        a=requests.get("https://www.quandl.com/api/v3/datasets/EOD/AAPL.json?api_key=xMK26SS7BgSLAGzJDXGT")
        b=json.loads(a.text)
        mdata=b['dataset']['data']
        udata=[i[1] for i in mdata]
        xdata=[i for i in range(len(udata))]


        return render(request,'stockdata/index.html',{'alldata':p1,'y':udata,'x':xdata })



def sony(request):
    ddd = urllib.request.urlopen("https://finance.yahoo.com/quote/SNE/history?p=SNE")  # https://finance.yahoo.com/quote/IBM/history?p=IBM
    dd = bs.BeautifulSoup(ddd, 'lxml')
    tbl = dd.find('table')
    l=[]
    for i in tbl:
        ttr=tbl.find_all('tr')
        for j in ttr:
            ttd=j.find_all('td')
            for k in ttd:
                l.append(k.text.strip())


    return render(request,'stockdata/sony.html',{'alldata':l})


def ibm(request):

    data=urllib.request.urlopen("https://finance.yahoo.com/quote/IBM/history?p=IBM")
    sp1=bs.BeautifulSoup(data,'lxml')
    dd=sp1.find('table')
    l=[]
    for i in dd:
        ttr=dd.find_all('tr')
        for j in ttr:
            ttd=j.find_all("td")
            for k in ttd:
                l.append(k.text.strip())
    return  render(request,'stockdata/ibm.html',{'alldata':l})



def fb(request):
    data=urllib.request.urlopen("https://finance.yahoo.com/quote/FB/history?p=FB")
    sp=bs.BeautifulSoup(data,"lxml")
    tbl=sp.find("table")
    l=[]
    for i in tbl:
        rrt=tbl.find_all("tr")
        for j in rrt:
            rrd=j.find_all("td")
            for k in rrd:
                l.append(k.text.strip())
    return render(request,'stockdata/fb.html',{'alldata':l})


def google(request):

    data=urllib.request.urlopen("https://finance.yahoo.com/quote/GOOG/history?p=GOOG")
    sp=bs.BeautifulSoup(data,"lxml")
    tbl=sp.find("table")
    l=[]
    for i in tbl:
        ttr=tbl.find_all("tr")
        for j in ttr:
            ttd=j.find_all("td")
            for k in ttd:
                l.append(k.text.strip())

    return  render(request,'stockdata/google.html',{'alldata':l})