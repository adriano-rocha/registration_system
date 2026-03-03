from django.shortcuts import render, redirect
from .models import User

def home(request):
    return render(request, 'users/home.html')

def users(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cpf = request.POST.get('cpf')
        birth_date = request.POST.get('birth_date')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        gender = request.POST.get('gender')
        status = request.POST.get('status', 'A')
        
        # Validação básica
        if name and email and cpf and birth_date:
            new_user = User()
            new_user.name = name
            new_user.email = email
            new_user.phone = phone
            new_user.cpf = cpf
            new_user.birth_date = birth_date
            new_user.street = street
            new_user.city = city
            new_user.state = state
            new_user.zipcode = zipcode
            new_user.gender = gender
            new_user.status = status
            
            # Foto de perfil (se enviada)
            if request.FILES.get('profile_photo'):
                new_user.profile_photo = request.FILES['profile_photo']
            
            new_user.save()
            return redirect('users_list')
    
    users = {'users': User.objects.all()}
    return render(request, 'users/users.html', users)

def delete_user(request, user_id):
    user = User.objects.get(user_id=user_id)
    user.delete()
    return redirect('users_list')