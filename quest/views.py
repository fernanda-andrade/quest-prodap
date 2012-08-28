#encoding: utf-8

from django.conf import settings
from django.shortcuts import render
import csv
from time import gmtime, strftime


def quest(request):
    data = {}
    data["BASE_URL"] = settings.BASE_URL
    data["STATIC_URL"] = settings.STATIC_URL
    return render(request, 'quest.html', data)


def quest_nutri(request):
    data = {}
    #data["empresa"] = nutri
    data["BASE_URL"] = settings.BASE_URL
    data["STATIC_URL"] = settings.STATIC_URL
    return render(request, 'quest-nutri.html', data)


def quest_pg(request):
    data = {}
    #data["empresa"] = pg
    data["BASE_URL"] = settings.BASE_URL
    data["STATIC_URL"] = settings.STATIC_URL
    return render(request, 'quest-pg.html', data)


def quest_tech(request):
    data = {}
    #data["empresa"] = tech
    data["BASE_URL"] = settings.BASE_URL
    data["STATIC_URL"] = settings.STATIC_URL
    return render(request, 'quest-tech.html', data)


def quest_colab(request):
    data = {}
    data["BASE_URL"] = settings.BASE_URL
    data["STATIC_URL"] = settings.STATIC_URL
    return render(request, 'quest-colab.html', data)


def resp(request):
    data = {}
    data["BASE_URL"] = settings.BASE_URL
    data["STATIC_URL"] = settings.STATIC_URL
    perguntas = 10
    csv_out = []
    usuario = request.POST["usuario"]
    negocio = request.POST["negocio"]
    if negocio == '':
        negocio = "na"

    ip = request.META['REMOTE_ADDR']
    
    data_atual = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    for p in range(0, perguntas + 1):
        respostas = []
        respostas.append(ip)
        respostas.append(negocio)
        respostas.append(data_atual)
        respostas.append(usuario)
        respostas.append(str(p))

        for e in range(1, 5):
            key = "p%se%s" % (str(p), str(e))
            respostas.append(request.POST[key])

        csv_out.append(respostas)

    arquivo_csv = open('/home/ubuntu/dados/oficial.csv', "a")
    writer = csv.writer(arquivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    for r in csv_out:
        writer.writerow([s.encode("latin-1") for s in r])
    data['success'] = True
    return render(request, 'resp.html', data)
