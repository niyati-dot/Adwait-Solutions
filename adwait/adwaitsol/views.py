from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from .forms import NewsletterForm, ContactInquiryForm
from .models import AdwaitappContact,AdwaitappMainServices, AdwaitappSubServices ,AdwaitappBlogs, AdwaitappTechnologies, AdwaitappTechnologiesService, AdwaitappInquiries
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db import IntegrityError
from django.utils import timezone

def render_items(request, item_name):
    cd = AdwaitappContact.objects.get(id=1)
    item = get_object_or_404(AdwaitappMainServices, url=item_name)
    menu = AdwaitappMainServices.objects.all()
    submenu = AdwaitappSubServices.objects.filter(main_service_id_id = item.id)
    main_service_ids = [item.id] 
    tech_main_services = AdwaitappTechnologiesService.objects.filter(main_services_id__in=main_service_ids)
    technologies_ids = tech_main_services.values_list('technologies_id', flat=True)
    technologies = AdwaitappTechnologies.objects.filter(id__in=technologies_ids)
    blogs = AdwaitappBlogs.objects.filter(status=1, main_service_id_id = item.id)
    return render(request, 'adwaitsol/service.html', {'item': item, 'menu': menu, 'submenu': submenu, 'cd': cd, 'blogs': blogs , 'technologies': technologies})

def render_submenu(request, item_name):
    cd = AdwaitappContact.objects.get(id=1)
    item = get_object_or_404(AdwaitappSubServices, url=item_name)
    menu = AdwaitappMainServices.objects.all()
    submenu = AdwaitappSubServices.objects.all()
    return render(request, 'adwaitsol/sub-service.html', {'item': item, 'menu': menu, 'submenu': submenu, 'cd': cd })

def render_blogs(request, item_name):
    cd = AdwaitappContact.objects.get(id=1)
    item = get_object_or_404(AdwaitappBlogs, url=item_name)
    menu = AdwaitappMainServices.objects.all()
    submenu = AdwaitappSubServices.objects.all()
    blogs = AdwaitappBlogs.objects.filter(status=1)
    return render(request, 'adwaitsol/blog.html', {'item': item, 'menu': menu, 'submenu': submenu, 'cd': cd, 'blogs': blogs })

def home(request):
    cd = AdwaitappContact.objects.get(id=1)
    menu = AdwaitappMainServices.objects.all()
    submenu = AdwaitappSubServices.objects.all()
    blogs = AdwaitappBlogs.objects.filter(status=1).order_by('-id')[:10:1]
    context = {
        'cd': cd,
        'menu': menu,
        'submenu': submenu,
        'blogs': blogs
    }
    return render(request, 'adwaitsol/index.html', context=context)

def contact(request):
    cd = AdwaitappContact.objects.get(id=1)
    menu = AdwaitappMainServices.objects.all()
    submenu = AdwaitappSubServices.objects.all()
    context = {
        'cd': cd,
        'menu': menu,
        'submenu': submenu
    }
    return render(request, 'adwaitsol/contact.html', context=context)

def blogs(request):
    cd = AdwaitappContact.objects.get(id=1)
    menu = AdwaitappMainServices.objects.all()
    submenu = AdwaitappSubServices.objects.all()
    blogs = AdwaitappBlogs.objects.filter(status=1)
    context = {
        'cd': cd,
        'menu': menu,
        'submenu': submenu,
        'blogs': blogs
    }
    return render(request, 'adwaitsol/blogs.html', context=context)


def about(request):
    cd = AdwaitappContact.objects.get(id=1)
    menu = AdwaitappMainServices.objects.all()
    submenu = AdwaitappSubServices.objects.all()
    context = {
        'cd': cd,
        'menu': menu,
        'submenu': submenu
    }
    return render(request, 'adwaitsol/about.html', context=context)

def services(request):
    cd = AdwaitappContact.objects.get(id=1)
    menu = AdwaitappMainServices.objects.all()
    submenu = AdwaitappSubServices.objects.all()
    context = {
        'menu': menu,
        'submenu': submenu,
        'cd': cd
    }
    return render(request, 'adwaitsol/services.html', context=context)

def portfolio(request):
    cd = AdwaitappContact.objects.get(id=1)
    menu = AdwaitappMainServices.objects.all()
    submenu = AdwaitappSubServices.objects.all()
    context = {
        'menu': menu,
        'submenu': submenu,
        'cd': cd
    }
    return render(request, 'adwaitsol/portfolio.html', context=context)

def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'].strip()  # Strip whitespace
            try:
               
                form.save()
                
                send_mail(
                    'Welcome to Our Newsletter',
                    'Dear Subscriber,\n\nThank you for subscribing to our newsletter. We are excited to have you on board!\n\nYou can look forward to receiving the latest updates, news, and exclusive offers from us.\n\nIf you have any questions or need assistance, please feel free to reach out.\n\nBest regards,\nThe Adwait Solutions Team',
                    'adwaitsolutions9@gmail.com',
                    [email],
                    fail_silently=False,
                )

                # Return success message
                return JsonResponse({'success': True, 'message': "Thank you for subscribing!"})

            except IntegrityError:
                # Handle duplicate email error
                return JsonResponse({'success': False, 'message': "You are already subscribed."})

        # If form is invalid, return errors
        return JsonResponse({'success': False, 'errors': form.errors})

    # If the request method is not POST, return an error message
    return JsonResponse({'success': False, 'message': 'Invalid request.'})

#Contact Form
def inquiry(request):
    if request.method == 'POST':
        form = ContactInquiryForm(request.POST)
        if form.is_valid():
    
            entry = AdwaitappInquiries(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
                status = 1,
                creation_date = timezone.localtime(timezone.now())
            )
            entry.save()
            from_email = 'vyasniyati.1828@gmail.com'
            email = EmailMessage(
                subject='New Inquiry Form Adwait Website',
                body=f"Name: {entry.name}\nEmail: {entry.email}\nSubject: {entry.subject}\nMessage: {entry.message}",
                from_email=from_email,
                to=['adwaitsolutions9@gmail.com'],  # List of recipient emails
            )
            email.reply_to = [entry.email]

            email.send(fail_silently=False)

            return JsonResponse({
                'success': True, 
                'message': "Thank you for Inquiry! We will get back to you shortly"
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'There was an issue with your form submission.',
                'errors': form.errors
            })
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method.'
    })