from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import ContactFormModel
from .forms import ContactForm

# Create your views here.
def homePage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message') 

        form_data = {'name': name, 'email': email, 'phone': phone, 'message': message}
        form = ContactForm(form_data)

        if form.is_valid():
            html = render_to_string('main\contactform.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message
            })
            send_mail('Customer Contact Form', 'Message', email, ['rayyanusername5@gmail.com'], html_message=html, fail_silently=False)
            return redirect('home')
    else:
        form = ContactForm()

    context = { 'form': form }
    return render(request, 'main/home.html', context)