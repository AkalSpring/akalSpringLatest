from django.contrib.postgres.fields import ArrayField
from django.db import models
from companies.models import Company
from products.models import Product
from django.db import models
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
    descriptionOfGoods = models.TextField(default="LAMINATED LEAF SPRINGS & NUT WITH BOLTS")

    def __str__(self):
        return str(self.invoice)

