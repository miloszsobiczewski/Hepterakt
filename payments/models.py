import os

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Payment(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    value = models.DecimalField(decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    invoice = models.FileField(null=True, blank=True, upload_to='invoices/%Y/%m')
    invoice_location = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField()

    def __str__(self):
        return self.name

    def filename(self):
        return os.path.basename(self.invoice.name)

    class Meta:
        ordering = ('date',)


class Task(models.Model):
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    deadline = models.DateField()

    def __str__(self):
        return self.name


class Month(models.Model):
    date = models.DateField(auto_now_add=True)
    work_hours = models.IntegerField()
    vacation_hours = models.IntegerField(default=0)

    def __str__(self):
        return str(self.date.year) + "." + str(self.date.month) + "-" + str(self.work_hours)