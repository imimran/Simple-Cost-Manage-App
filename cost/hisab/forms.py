from django import forms
from .models import Hisab

class HisabForm(forms.ModelForm):
	class Meta:
		model = Hisab
		fields = '__all__'