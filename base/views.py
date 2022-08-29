from django.shortcuts import render, redirect
from .forms import MemeberRegistrationForm

# Create your views here.


def index(request):
    form = MemeberRegistrationForm()
    if request.method == 'POST':
        form = MemeberRegistrationForm(data=request.POST)
        if form.is_valid:
            form.save()
            form = MemeberRegistrationForm()
            return redirect('index')
    context = {'form':form}
    return render(request, 'base/index.html', context)