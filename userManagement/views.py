from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import *

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class RegisterUser(View):

    def get(self, request):
        return JsonResponse({
            "status": "ok"
        })

    def post(self, request):
        userEmail = request.POST.get("name", None)
        user = User.objects.get(username=userEmail)
        if userName is not None:
            return JsonResponse({
                "status": 500,
                "message": "ERROR: User with this email already registered"
            })
        user = User.objects.create_user(username=userEmail)
        user.save()

        customUser = CustomUser.objects.create(
            user=user,
            phoneNumber=request.POST.get("phone", "-1"),
            email=userEmail,
            facialEmbedding=""
        )
        customUser.save()
        return JsonResponse({
            "status": 200,
            "message": "User registered successfully"
        })