# feedback/views.py
from django.shortcuts import render,redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app1:thanks')
           
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

def thanks_view(request):
    return render(request, 'thanks.html')
