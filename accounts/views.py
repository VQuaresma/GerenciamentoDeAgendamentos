from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):  # <-- corrigi aqui
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # redireciona para a página de login
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})  # <-- corrigi aqui
