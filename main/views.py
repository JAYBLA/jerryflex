from django.shortcuts import render, get_object_or_404, redirect, reverse
from.models import Contact
from .forms import ContactForm
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import JsonResponse

def home(request):
    template_name = 'main/home.html'
    context = {
        'title':"Home"    
        
    }    
    return render(request, template_name, context)