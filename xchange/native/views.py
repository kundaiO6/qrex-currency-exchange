from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Listing
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json

@csrf_exempt
def index(request):
    listing = Listing.objects.all()
    if request.method == "POST":
        x=Listing.objects.create( phone_number = request.POST['phone_number'],
            country = request.POST['country'],
            currency = request.POST['currency'],
            action = request.POST['action'],
            at = request.POST['at'],
            pair = request.POST['pair'])

        x.save()
    
    
    return HttpResponse(json.dumps(list(listing.values())), content_type='application/json')
