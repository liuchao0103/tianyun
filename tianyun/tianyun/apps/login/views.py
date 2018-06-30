from django.shortcuts import render

def show_login_view(request):
    return render(request, "login/index.html", locals())

def post_login(request):
    return render(request, "login/index.html", locals()) 
