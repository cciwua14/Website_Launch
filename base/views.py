from django.shortcuts import render, redirect
from .forms import MemeberRegistrationForm
from django.contrib import messages
from .models import Member

# Create your views here.


def index(request):
    members = Member.objects.all().count
    form = MemeberRegistrationForm()
    if request.method == 'POST':
        form = MemeberRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Joined Successfully!")
            form = MemeberRegistrationForm()
            return redirect('index')
        else:
            messages.error(request, "Invalid data")
    context = {'form':form, 'members':members, 'messgaes':messages}
    return render(request, 'base/index.html', context)