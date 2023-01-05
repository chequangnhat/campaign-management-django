from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

def say_hello(request):
  return HttpResponse("Hello, world. You're at the polls index.")

def get_user(request, id):
  user = User.objects.get(id=id)
  # if user.id == "user1":
  #     user.email = "changed@gmail.com"
  return HttpResponse(f"user email is {user.email}")

@csrf_exempt
def add_campaign(request):
  if request.method == "POST":
    name = request.POST.get("name")
    print("request", request)
    data = json.loads(request.body)
    print("name: ", data["name"])
    

    # email = request.POST.get("email")
    # message = request.POST.get("message")
    # campaign = Campaign(name=name, email=email, message=message)
    return JsonResponse({"name recieved" : data["name"]})