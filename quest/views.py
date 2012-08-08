#encoding: utf-8

from django.shortcuts import render
import csv
from time import gmtime, strftime


def quest(request):
    data = {}
    return render(request, 'quest.html', data)


def quest_nutri(request):
    data = {}
    return render(request, 'quest-nutri.html', data)


def quest_pg(request):
    data = {}
    return render(request, 'quest-pg.html', data)


def quest_tech(request):
    data = {}
    return render(request, 'quest-tech.html', data)


def quest_colab(request):
    data = {}
    return render(request, 'quest-colab.html', data)


def resp(request):
    data = {}
    perguntas = 16
    csv_out = []
    usuario = request.POST["usuario"]
    data_atual = strftime("%Y-%m-%d %H:%M:%S", gmtime())

    for p in range(0, perguntas + 1):
        respostas = []
        respostas.append(data_atual)
        respostas.append(usuario)

        for e in range(1, 5):
            key = "p%se%s" % (str(p), str(e))
            respostas.append(request.POST[key])

        csv_out.append(respostas)

    arquivo_csv = open('output.csv', "a")
    writer = csv.writer(arquivo_csv, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    for r in csv_out:
        writer.writerow(r)
    data['success'] = True
    return render(request, 'resp.html', data)
