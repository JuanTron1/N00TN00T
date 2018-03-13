from django.shortcuts import render
from .models import Applicant
from django import forms
# Create your views here.
class ApplicantForm(forms.ModelForm):
	class Meta:
		model = Applicant
		fields = '__all__'
def apply(request):
	form = ApplicantForm()
	return render(request, 'wcts_app/apply.html',{'form':form})
