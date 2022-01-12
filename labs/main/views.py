from typing import List
from django.shortcuts import render
from .models import TprLab1Strategy, TprLab1Dohod, TprLab1StrategyExample, TprLab1DohodsExample, TprLab6StockData
from .forms import TprLab1StrategyForm, TprLab1DohodForm
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.core import serializers
import json

def index(request):
    return render(request,'main/index.html')


def about(request):
    data = {
        'title': 'About us',
        'values' : ['Someone', 'Hello', 'Ana'], # список
        'obj':{ # словарь
            'car' : 'AUDI',
            'age' : '21',
            'hobby' : 'cars'
        }
    }
    return render(request,'main/about.html', data)


# def tpr1(request):
#     return render(request, 'main/tpr/tpr1.html')


# def tpr2(request):
#     return render(request, 'main/tpr/tpr2.html')


def tpr3(request):
    return render(request, 'main/tpr/tpr3.html')


def tpr4(request):
    return render(request, 'main/tpr/tpr4.html')


def tpr5(request):
    return render(request, 'main/tpr/tpr5.html')


def tpr1_upload(request):
    strategys = TprLab1Strategy.objects.all()
    dohods = TprLab1Dohod.objects.all()
    if request.method == 'POST':
        # tpr1TestData = TprLab1StrategyForm()
        datasetStr = Dataset()
        datasetDohod = Dataset()

        new_file_strat= request.FILES['myfileStrategy']
        new_file_dohod= request.FILES['myfileDohods']


        if not (new_file_strat.name.endswith('xlsx') and new_file_dohod.name.endswith('xlsx')):
            messages.info(request,'неверный формат файла')
            return render(request, 'main/tpr/tpr1.html')

        imported_data_strat = datasetStr.load(new_file_strat.read(), format='xlsx')
        imported_data_dohod = datasetDohod.load(new_file_dohod.read(), format='xlsx')

        for data in imported_data_strat:
            valueStrategy = TprLab1Strategy (
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5]
            )
            valueStrategy.save()
        for data in imported_data_dohod:
            valDohod = TprLab1Dohod (
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5]
            )
            valDohod.save()
    
    return render(request, 'main/tpr/tpr1.html', {'strats' : strategys, 'dohods': dohods},)


def tpr1_upload_Example(request):
    strategysExample = TprLab1StrategyExample.objects.all()
    dohodsExample = TprLab1DohodsExample.objects.all()
    if request.method == 'POST':
        # tpr1TestData = TprLab1StrategyForm()
        datasetStr = Dataset()
        datasetDohod = Dataset()

        new_file_strat= request.FILES['myfileStrategyExample']
        new_file_dohod= request.FILES['myfileDohodsExample']


        if not (new_file_strat.name.endswith('xlsx') and new_file_dohod.name.endswith('xlsx')):
            messages.info(request,'неверный формат файла')
            return render(request, 'main/tpr/tpr2.html')

        imported_data_strat = datasetStr.load(new_file_strat.read(), format='xlsx')
        imported_data_dohod = datasetDohod.load(new_file_dohod.read(), format='xlsx')

        for data in imported_data_strat:
            valueStrategy = TprLab1StrategyExample (
                data[0], data[1], data[2], data[3], data[4],
                data[5], data[6], data[7], data[8], data[9], 
                data[10]
            )
            valueStrategy.save()
        for data in imported_data_dohod:
            valDohod = TprLab1DohodsExample (
                data[0], data[1], data[2], data[3], data[4],
                data[5], data[6], data[7], data[8], data[9], 
                data[10]
            )
            valDohod.save()
    
    return render(request, 'main/tpr/tpr2.html', {'stratsExample' : strategysExample, 'dohodsExample': dohodsExample},)


def tpr6_upload(request):
    # json_serializer = serializers.get_serializer("json")
    # stockData = json_serializer.serialize(TprLab6StockData.objects.all().order_by('id')[:3], ensure_ascii=False)
    stockData = TprLab6StockData.objects.all().values('ticker','stockDate', 'stockOpen', 'stockHigh', 'stockLow', 'stockClose', 'stockVol')
    data = list(stockData)
    # stockDataJSON = json.dumps(stockData)
    if request.method == 'POST':
        # tpr1TestData = TprLab1StrategyForm()
        datasetStock = Dataset()

        new_file_stock= request.FILES['fileLab6']

        if not (new_file_stock.name.endswith('xlsx')):
            messages.info(request,'неверный формат файла')
            return render(request, 'main/tpr/tpr5.html')

        imported_data_stock = datasetStock.load(new_file_stock.read(), format='xlsx')

        for data in imported_data_stock:
            valuesStock = TprLab6StockData (
                data[0], data[1], data[2], data[3], 
                data[4], data[5], data[6], data[7]
            )
            valuesStock.save()
    return render(request, 'main/tpr/tpr5.html', {'stockData' : data},)