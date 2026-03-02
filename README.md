# Sistema de Registro - Django

Sistema de registro de usuários desenvolvido com Django.

## 🚀 Tecnologias

- Python 3.x
- Django
- SQLite

## 📋 Requisitos

- Python 3.x
- pip

## 🔧 Instalação

1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/registration_system.git
cd registration_system
```

2. Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Execute as migrações
```bash
python manage.py migrate
```

5. Crie um superusuário
```bash
python manage.py createsuperuser
```

6. Rode o servidor
```bash
python manage.py runserver
```

7. Acesse: http://127.0.0.1:8000

## 📁 Estrutura
```
registration_system/
├── manage.py
├── registration_system/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app_users_reg/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── requirements.txt
└── README.md
```

## 👤 Autor

Adriano Rocha