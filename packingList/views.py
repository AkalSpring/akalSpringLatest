import json
from math import ceil

from django.shortcuts import render
from master.models import Bill


def index(request):
    return render(request, "packingList/home.html")


def showBills(request):
    context = dict()

    datFrom = request.POST.get("billDateFrom")
    datTo = request.POST.get("billDateTo")
    instance = Bill.objects.filter(billDate__range=[datFrom, datTo])

    for i in instance:
        i.products = json.loads(i.products)

    context["bills"] = instance

    return render(request, "packingList/home.html", context)


def showPdf(request):
    context = dict()
    id = request.GET.get("id")
    instance = Bill.objects.get(id=id)
    instance.products = json.loads(instance.products)

    netWt = 0
    netGrossWt = 0
    lst = list()

    for product in instance.products:
        netWt += float(product["weight"])*float(product["qty"])
        netGrossWt += float(product["weight"])*float(product["qty"]) + float(product["boxWt"])
        lst.append(product)

    prodList = []
    while len(lst):
        prods = []
        while len(lst) > 0 and len(prods) < 12:
            prods.append(lst.pop(0))
        prodList.append(prods)

    lastList = prodList[-1]
    prodList = prodList[:-1]

    context = {
                "iProds": prodList, "eProds": lastList, "netWt": netWt, "netGrossWt": netGrossWt,
                "totalBoxes": instance.totalBoxes, "invoice": instance.invoice, "billDate": instance.billDate,
                "otherReferences": instance.otherReferences, 'grNo': instance.grNo, "customerId": instance.customerId,
                "termOfPayment": instance.termsOfPayment, "preCarriage": instance.preCarriage,
                "billOfLadingNo":instance.billOfLadingNo, "ladingDate": instance.ladingDate,
                "vesselFlightNo": instance.vesselFlightNo, "portOfLoading": instance.portOfLoading,
                "portOfDischarge": instance.portOfDischarge, "finalDestination": instance.finalDestination,
                "natureOfContract": instance.natureOfContract, "billId": id,
               }
    return render(request, 'packingList/pdf_template.html', context)
