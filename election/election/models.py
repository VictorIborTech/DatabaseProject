from django.db import connections
from django.db import models

class Agent(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    pollingunit_id=models.CharField(max_length=20)

    class Meta:
        db_table= "agentname"





class Lgaresult(models.Model):
    lga_name=models.CharField(max_length=100)
    party_abbreviation=models.CharField(max_length=100)
    party_score=models.CharField(max_length=100)
    entered_by_user=models.CharField(max_length=100)
    date_entered=models.CharField(max_length=20)
    user_ip_address=models.CharField(max_length=20)

    class Meta:
        db_table= "announced_lga_results"




class Unitresult(models.Model):
    polling_unit_id=models.CharField(max_length=100)
    party_abbreviation=models.CharField(max_length=100)
    party_score=models.CharField(max_length=100)
    entered_by_user=models.CharField(max_length=100)
    date_entered=models.CharField(max_length=20)
    user_ip_address=models.CharField(max_length=20)

    class Meta:
        db_table= "announced_pu_results"



class Lga(models.Model):
    lga_id=models.CharField(max_length=100)
    lga_name=models.CharField(max_length=100)
    lga_numb=models.CharField(max_length=100)
    lga_description=models.TextField(max_length=100)
    entered_by_user=models.CharField(max_length=100)
    date_entered=models.CharField(max_length=20)
    user_ip_address=models.CharField(max_length=20)

    class Meta:
        db_table= "lga"


class Polling_Unit(models.Model):
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField()
    polling_unit_number = models.CharField(max_length=100)
    polling_unit_name = models.CharField(max_length=100)
    polling_unit_description = models.TextField(max_length=200)
    lat= models.CharField(max_length=100)
    long= models.IntegerField()


    class Meta:
        db_table = 'polling_unit'



class State(models.Model):
    state_name= models.CharField(max_length=50)

    class Meta:
        db_table = 'states'

class Ward(models.Model):
    ward_id= models.IntegerField()
    ward_name= models.CharField(max_length=200)
    lga_id = models.IntegerField()
    ward_description= models.TextField(max_length=100)
    entered_by_user = models.CharField(max_length=100)
    date_entered = models.CharField(max_length=20)
    user_ip_address = models.CharField(max_length=20)

    class Meta:
        db_table= 'ward'



class New_Unit(models.Model):
     id = models.IntegerField(primary_key=True)
     polling_unit_id = models.IntegerField()
     lga_id = models.IntegerField()
     polling_unit_number =models.IntegerField()
     polling_unit_name = models.CharField(max_length=100)
     polling_unit_description = models.TextField(max_length=200)
     party_abbreviation = models.CharField(max_length=100)
     party_scores = models.IntegerField()
     date = models.DateField()

     class Meta:
         db_table='new_polling_unit'