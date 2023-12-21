from django.db import models

# Create your models here.
# class model(models.Model):
#     charField = models.CharField(max_length=50)
#     testField = models.TextField(null=True, blank=True)
#     connection = models.ForeignKey(model1, on_delete=models.DO_NOTHING, null=True, blank=True)

class ContactFormModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    message = models.TextField(null=True, blank=True)