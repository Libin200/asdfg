from django.db import models

# Create your models here.
class itdesk(models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    salary=models.IntegerField()
    contact_no=models.BigIntegerField()
    class Meta:
        db_table="ITDESK"

class up_load(models.Model):
    id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=50)
    file=models.FileField()
    class Meta:
        db_table="up_load"
