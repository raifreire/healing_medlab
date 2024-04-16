from django.shortcuts import render,redirect
from django.contrib.auth.models import User



def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get('confirmar_senha')
        users = User.objects.filter(username=username) 
    if users.exists():
        print('Erro 1')
        return redirect('/usuarios/cadastro')
    if senha != confirmar_senha:
        print('Erro ')
        return redirect('/usuarios/cadastro')
    if len(senha) < 6:
        #messages.add_message(request, constants.ERROR, 'A senha deve possuir pelo menos 6 caracteres')
        print('Erro 3')
        return redirect('/usuarios/cadastro')

    try:
        User.objects.create_user(
            username=username,
            email=email,
            password=senha
        )
        return redirect('/usuarios/login')
    except:
        print('Erro 4')
        return redirect('/usuarios/cadastro')
