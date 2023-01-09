from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User, Campaign
import json

from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.utils.functional import SimpleLazyObject

from marshmallow import Schema, fields, ValidationError
from pprint import pprint
import datetime

def say_hello(request):
  return HttpResponse("Hello, world. You're at the polls index.")

def get_user(request, id):
  user = User.objects.get(id=id)
  return HttpResponse(f"user email is {user.email}")

class CampaignSchema(Schema):
  name = fields.String()
  start_time = fields.DateTime()
  end_time = fields.DateTime()
  budget = fields.Integer()
  bid_amount = fields.Integer()
  title = fields.String()
  description =fields.String()
  banner = fields.String()
  final_url = fields.String()
  used_amount = fields.Integer()
  usage_rate = fields.Integer()
  user_id = fields.String()

@csrf_exempt
def add_campaign(request):
  if request.method == "POST":
    #covert input to json format
    data = json.loads(request.body)

    fields = [ "name", "start_time", "end_time", "budget", "bid_amount", "title", "description", "banner", "final_url", "used_amount", "usage_rate", "user_id" ]
    fields.sort()
    list_keys = list(data.keys())
    list_keys.sort()

    if fields != list_keys:
      return JsonResponse({"status": "error", "message": "missing fields"}, status=400)

    user = User.objects.get(id=data["user_id"])

    camp = Campaign(name = data["name"], start_time = data["start_time"], end_time = data["end_time"], budget = data["budget"], bid_amount = data["bid_amount"], title = data["title"], description = data["description"], banner= data["banner"], final_url= data["final_url"], used_amount = data["used_amount"], usage_rate = data["usage_rate"], user_id = user)
    camp.save()
    
    try:
      CampaignSchema().load(data)
    except ValidationError as err:
      pprint(err.messages)
      return JsonResponse({"status": "error validation", "message": err.messages}, status=400)


    return JsonResponse({"create status" : "success"})
