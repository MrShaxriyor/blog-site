from django.shortcuts import render, redirect
from django.core.mail import send_mail
import random
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def edit_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.filter(email=email).first()

            if user is None:
                raise User.DoesNotExist

            code = str(random.randint(100000, 999999))
            request.session['code'] = code  
            request.session['email'] = email

            send_mail(
                'Tastiqlash kod:',
                f'Sizning tasdiqlash kodingiz: {code}',
                'coder.eror@gmail.com',   
                [email],                  
                fail_silently=False,
            )

            return redirect('check_code')

        except User.DoesNotExist:
            return render(request, 'accounts/reset_password.html', {'error': 'Email topilmadi.'})
    
    return render(request, 'accounts/reset_password.html')





def verify_code(request):
    if request.method == 'POST':
        entered_code = request.POST.get('code')
        reset_code = request.session.get('code')


        if str(entered_code) == str(reset_code):
            return redirect('set_new_password')
        else:
            return render(request, 'accounts/verify_code.html', {'error': '❌ Notog‘ri kod'})
    
    return render(request, 'accounts/verify_code.html')




from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()

def set_new_password(request):
    if request.method == 'POST':
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'accounts/set_new_password.html', {'error': 'Parollar mos emas'})

        email = request.session.get('email') 
        if not email:
            return render(request, 'accounts/set_new_password.html', {'error': 'Muddat tugagan. Qayta urinib ko‘ring.'})

        user = User.objects.filter(email=email).first()
        if not user:
            return render(request, 'accounts/set_new_password.html', {'error': 'Foydalanuvchi topilmadi.'})

        
        user.password = make_password(password1)
        user.save()

        
        request.session.pop('email', None)
        request.session.pop('code', None)

        return redirect('get-profile')

    return render(request, 'accounts/set_new_password.html')
