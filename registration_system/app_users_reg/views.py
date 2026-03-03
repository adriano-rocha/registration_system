from django.shortcuts import redirect, render
from .models import User

def home(request):
    return render(request, 'users/home.html')

def users(request):
    # Salvar os dados da tela para o banco de dados.
     if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')        
    # Verifica se campos não estão vazios    
        if name and age:
            new_user = User()
            new_user.name = name
            new_user.age = age
            new_user.save()
    # Exibir todos os usuários já cadastrados em uma nova página
     users = {
        'users': User.objects.all()
    }
    # Retornar os dados para a página de listagem de usuários
     return render(request,'users/users.html',users)

def delete_user(request, user_id):
        user = User.objects.get(user_id=user_id)
        user.delete()
        return redirect('users_list')
    
   
