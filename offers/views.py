from django.shortcuts import render , redirect
from offers.models import Offer
from .models import Offer

#def create_Offer(request):

    #if request.method=='POST'
       #form =OfferForm(request.POST)
       #if form.is_valid():
        #    f=form.save(commit=False)
         #   f.user = request.user 
         #   f.save()
          #  return 
    #else:    







def offer(request):

   # offers = data ['offers']
    offers = Offer.objects.all()
    context = {  'offers'  : offers   }
    return render(request, 'offers/offer.html',  context)
	
