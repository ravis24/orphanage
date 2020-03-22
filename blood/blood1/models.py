from django.db import models

# Create your models here.

#donar registration form
class Register12(models.Model):
	blood_choice=(
		('a','a+'),
		('b','a-'),
		('c','o+'),
		('d','o-'),
		('e','b+')
		)
	gen=(
		('male','M'),
		('Female','F'),
		('Others','O')
		)
	name = models.CharField(max_length=50)
	emailid = models.EmailField()
	gender=models.CharField(choices=gen,max_length=30)
	blood_group = models.CharField(choices=blood_choice, max_length=128)
	state=models.CharField(max_length=30)
	city=models.CharField(max_length=30)
	def __str__(self):
		return self.name
# donar feedback form
class donar_feedback(models.Model):
	name = models.CharField(max_length=30)
	emailid = models.EmailField()
	inbox=models.CharField(max_length=500)
	def __str__(self):
		return self.name
# if  any one contact with us or if anyone have a query		
class contactus(models.Model):
	name = models.CharField(max_length=30)
	emailid = models.EmailField()
	subject=models.CharField(max_length=100)
	message=models.CharField(max_length=300)
	def __str__(self):
		return self.name
# Volunteer aplication form
class volunteer_apply(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    emailid=models.EmailField()
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    Pin_code=models.IntegerField()
    profile_image = models.ImageField(upload_to='images/',blank=True) 
    
    def __str__(self):
    	return self.emailid


