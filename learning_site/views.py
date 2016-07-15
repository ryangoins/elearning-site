from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms

def hello_world(request):
    return render(request, 'home.html')

def suggestion_view(request):
    form = forms.SuggestionForm()
    if request.method == 'POST':
        #takes all of the form data that comes in via POST and
        #puts it into the form. request.POST is kinda like a dictionary
        #it matches the values to their form fields
        form = forms.SuggestionForm(request.POST)
        #validates the data
        if form.is_valid():
            send_mail(
                'Suggestion from {}'.format(form.cleaned_data['name']),
                form.cleaned_data['suggestion'],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['ryan.c.goins@gmail.com']
            )
            messages.add_message(request, messages.SUCCESS,
                                'Thanks for your suggestion!')
            return HttpResponseRedirect(reverse('suggestion'))
        else:
            messages.add_message(request, messages.ERROR,
                                'Sorry, try again!')
    #the context dictionary passes the value to the variable in the template
    return render(request, 'suggestion_form.html', {'form': form})
