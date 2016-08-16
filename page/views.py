from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.utils import timezone
from .models import Article, Trademark, Slide



def contact(request):
	article = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	trademark = Trademark.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	slide = Slide.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	if request.method == 'POST':
		form = ContactForm(request.POST)
		
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			plus = message + ' ' + sender
			recipients = ['sikora.y@pozitiff.ua']
						
			try:
				send_mail(subject, plus, 'sikora.@nton.info', recipients)
			except BadHeaderError: 
				return HttpResponse('Invalid header found')
			
			return render(request, 'page/thanks.html')
	else:
		
		form = ContactForm()
	
	return render(request, 'page/contact.html', {'form': form, 'article':article, 'trademark':trademark, 'slide':slide})
def thanks(reguest):
	thanks = 'thanks'
	return render(reguest, 'page/thanks.html', {'thanks': thanks})