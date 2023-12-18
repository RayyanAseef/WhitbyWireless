from django.db import models

model1 = 1

# Create your models here.
# class model(models.Model):
#     charField = models.CharField(max_length=50)
#     testField = models.TextField(null=True, blank=True)
#     connection = models.ForeignKey(model1, on_delete=models.DO_NOTHING, null=True, blank=True)

class quote(models.Model):
    pass