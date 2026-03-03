from django.db import models

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    
    STATUS_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    ]
    
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True, null=True)  # ← Opcional
    phone = models.CharField(max_length=20, blank=True, null=True)  # ← Opcional
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)  # ← Opcional
    birth_date = models.DateField(blank=True, null=True)  # ← Opcional
    
    # Endereço
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.CharField(max_length=9, blank=True, null=True)
    
    # Outros
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    
    def __str__(self):
        return self.name