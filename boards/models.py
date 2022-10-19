from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True)
    age = models.IntegerField()
    salary = models.IntegerField()
    department = models.CharField(max_length=20, blank=True)
    passward = models.CharField(max_length=20, blank=True)


    class Meta:
    	db_table='user'
        
class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=30,blank=True)
    contact_name = models.CharField(max_length=30,blank=True)
    address = models.CharField(max_length=30,blank=True)
    city = models.CharField(max_length=30,blank=True)
    postal_code = models.CharField(max_length=30,blank=True)
    country = models.CharField(max_length=30,blank=True)

    class Meta:
    	db_table='customers'

class Empolyee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=30,blank=True)
    age = models.IntegerField(blank=True)
    contactno = models.IntegerField(blank=True)
    

    class Meta:
    	db_table='employee'
 
class Persons(models.Model):
    person_id = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=30,blank=True)
    person_age = models.IntegerField(blank=True)
    person_contactno = models.CharField(max_length=12,blank=True)
    person_status = models.BooleanField()
    joining_date = models.DateField()

    

    class Meta:
    	db_table='persons'
 