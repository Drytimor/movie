from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm

# Create your views here.
def index(requests):
    if requests.method == 'POST':
        form = FeedbackForm(requests.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
    return render(requests, 'html/feedback.html', context={'form': form})



def done(requests):
    return render(requests, 'html/done.html')