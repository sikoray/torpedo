from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField( max_length = 100, widget=forms.TextInput(attrs={'placeholder': "  Ім'я"}))
	phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '  Номер телефону'}))
	sender = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': '  Email'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'size','placeholder': '  Ваше повідомлення'}))
	
