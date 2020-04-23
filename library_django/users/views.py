from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('library-login')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }

    return render(response, 'users/register.html', context)

