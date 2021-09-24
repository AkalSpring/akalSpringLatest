from typing import Tuple
from django.contrib.postgres.fields import ArrayField
from django.db import models
from companies.models import Company
from products.models import Product
from django.db import models
import json
# Create your models here.


class Bill(models.Model):
    invoice = models.TextField()
    billDate = models.DateField()
    otherReferences = models.TextField(blank=True, null=True)
    grNo = models.TextField(blank=True, null=True)
    customerId = models.ForeignKey(Company, on_delete=models.CASCADE)
    termsOfPayment = models.TextField(blank=True, null=True)
    natureOfContract = models.TextField(blank=True, null=True)
    preCarriage = models.TextField(blank=True, null=True)
    vesselFlightNo = models.TextField(blank=True, null=True)
    portOfLoading = models.TextField(blank=True, null=True)
    portOfDischarge = models.TextField(blank=True, null=True)
    finalDestination = models.TextField(blank=True, null=True)
    products = models.TextField()
    freightCharges = models.FloatField()
    totalSales = models.FloatField()
    currency = models.TextField()
    ladingDate = models.DateField(blank=True, null=True)
    billOfLadingNo = models.TextField(blank=True, null=True)
    totalBoxes = models.IntegerField()
    # for letters
    lcNo = models.TextField(blank=True, null=True)
    lcDate = models.DateField(blank=True, null=True)
    contractNo = models.TextField(blank=True, null=True)
    contractDate = models.DateField(blank=True, null=True)
    shippingBillNo = models.TextField(blank=True, null=True)
    shippingBillDate = models.DateField(blank=True, null=True)
    exchangeNo = models.TextField(blank=True, null=True)
    exchangeDate = models.DateField(blank=True, null=True)
    consigneeBank = models.TextField(blank=True, null=True)
    consigneeAccount = models.TextField(blank=True, null=True)
    descriptionOfGoods = models.TextField(
        default="LAMINATED LEAF SPRINGS & NUT WITH BOLTS")
    shipMark = models.TextField(blank=True, null=True)
    checkerForCForFOB = models.TextField(default="C&F")
    amtDesc = models.TextField(blank=True, null=True)
    pdfConsignee = models.TextField(blank=True, null=True)

    def shipingMark(self):
        if self.shipMark:
            return self.shipMark
        else:
            self.shipMark = (
                "1 - {} {}".format(self.totalBoxes, self.finalDestination))
            self.save()
            return self.shipMark

    def amtDescription(self):
        if self.amtDesc:
            return self.amtDesc
        else:
            self.amtDesc = ("Total {} FOB".format(
                self.currency.split(" - ")[1]))
            self.save()
            return self.amtDesc

    def getConsignee(self):
        if self.pdfConsignee:
            return json.loads(self.pdfConsignee)
        else:
            self.pdfConsignee = json.dumps({
                    'name': self.customerId.company_name,
                    'address': self.customerId.company_address,
                    'country': self.customerId.company_country,
                })
            
            self.save()
            return json.loads(self.pdfConsignee)

    def __str__(self):
        return str(self.invoice)
