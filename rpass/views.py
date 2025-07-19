from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import random
# Create your views here.



def edit_pass(request):
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

            return redirect('tekshir')

        except User.DoesNotExist:
            return render(request, 'accounts/edit_pass.html', {'error': 'Email topilmadi.'})
    
    return render(request, 'accounts/edit_pass.html')




def tekshir(request):
    if request.method == 'POST':
        entered_code = request.POST.get('code')
        code = request.session.get('code')

        if entered_code == code:
            return redirect('yparol')
        else:
            return render(request, 'accounts/tekshir.html', {'error': '❌ Kod notogri'})

    return render(request, 'accounts/tekshir.html')







def yparol(request):
    if request.method == 'POST':
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'accounts/set_new_password.html', {'error': 'Parollar mos emas'})

        email = request.session.get('email')
        user = User.objects.filter(email=email).first()

        if not user:
            return render(request, 'accounts/yparol.html', {'error': 'Foydalanuvchi topilmadi'})

        user.password = make_password(password1)
        user.save()

        request.session.pop('email', None)
        request.session.pop('code', None)

        return redirect('get-login')

    return render(request, 'accounts/yparol.html')
