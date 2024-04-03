from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import *

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class EarlyRegister(View):

    def get(self, request):
        return JsonResponse({
            'status': 200,
            'message': 'Register for early interest in ScalerFest 2024'
        })

    def post(self, request):

        email = request.POST.get('email')
        print("Registering early interest for user => ", email)
        if email:
            earlyInterestUser = EarlyInterest.objects.get_or_create(email=email)
            return JsonResponse({
                'status': 200,
                'message': 'User registered successfully'
            })
        else:
            return render(request, 'failure.html')