from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact

# Create your views here.
def contacts(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You inquiry has already been sent. A realtor will get back to you soon.')
                return redirect('/listings/'+listing_id)


        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        messages.success(request, 'Inquiry sent succesfully. A realtor will get back to you soon.')

        return redirect('/listings/'+listing_id)
    
    return redirect('/listings/'+listing_id)
