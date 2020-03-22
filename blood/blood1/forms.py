from django import forms
from .models import *

class signup_form(forms.ModelForm):
	name=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
	emailid=forms.EmailField()
	state=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)
	city=forms.CharField(widget=forms.TextInput(),required=True,max_length=100)


	class Meta():
		model= Register12
		fields = ['name','emailid','gender','blood_group','state','city']

class share_feedback(forms.ModelForm):
	name=forms.CharField(widget=forms.TextInput(),required=True,max_length=30)
	emailid=forms.EmailField(required=True)
	inbox=forms.CharField(widget=forms.TextInput(),required=True,max_length=500)

	class Meta():
		model=donar_feedback
		fields=['name','emailid','inbox']
class find_donor(forms.ModelForm):
	

	class Meta():
		model=Register12
		fields=['state','city','gender','blood_group']

class contact_form(forms.ModelForm):



	class Meta():
		model=contactus
		fields=['name','emailid','subject','message']

class volunterr_form(forms.ModelForm):
	



	class Meta():
		model=volunteer_apply
		fields=['first_name','last_name','emailid','address','city','state','Pin_code','profile_image']