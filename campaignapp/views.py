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

def say_hello(request):
  return JsonResponse({"result" : "Hello, world. You're at the polls index."})

def get_user(request, id):
  try:
      user = User.objects.get(id=id)
  except User.DoesNotExist:
      return JsonResponse({"result": "user does not exist"},status=404)
  user = User.objects.get(id=id)
  return HttpResponse(f"user email is {user.email}")

def get_all_campaign(request):
  try:
      campaign_list = []
      campaigns = Campaign.objects.all()
      for campaign in campaigns:
        new_item = {
          "name": campaign.name,
          "start_time": str(campaign.start_time),
          "end_time": str(campaign.end_time),
          "budget": campaign.budget,
          "bid_amount": campaign.bid_amount,
          "title": campaign.title,
          "description": campaign.description,
          "banner": campaign.banner,
          "final_url": campaign.final_url,
          "used_amount": str(campaign.used_amount),
          "usage_rate": str(campaign.usage_rate),
          "user_id": campaign.user_id_id
        }
        # campaign_list[campaign_index] = new_item
        campaign_list.append(new_item)
      return JsonResponse({"result": campaign_list},status=200)
      
  except Campaign.DoesNotExist:
      return JsonResponse({"result": "campaign does not exist"},status=404)

def get_campaign_by_user_id(request, user_id):
  try:
      campaign_list = []
      campaigns = Campaign.objects.filter(user_id_id = user_id)
      for campaign in campaigns:
        new_item = {
          "name": campaign.name,
          "start_time": str(campaign.start_time),
          "end_time": str(campaign.end_time),
          "budget": campaign.budget,
          "bid_amount": campaign.bid_amount,
          "title": campaign.title,
          "description": campaign.description,
          "banner": campaign.banner,
          "final_url": campaign.final_url,
          "used_amount": str(campaign.used_amount),
          "usage_rate": str(campaign.usage_rate),
          "user_id": campaign.user_id_id
        }
        # campaign_list[campaign_index] = new_item
        campaign_list.append(new_item)
      return JsonResponse({"result": campaign_list},status=200)
      
  except Campaign.DoesNotExist:
      return JsonResponse({"result": "campaign does not exist"},status=404)
@csrf_exempt
def add_campaign(request):
  if request.method == "POST":
    data = json.loads(request.body)

    try:
      CampaignSchema().load(data)
    except ValidationError as err:
      pprint(err.messages)
      return JsonResponse({"status": "error validation", "message": err.messages}, status=400)

    try:
      user = User.objects.get(id=data["user_id"])
      camp = Campaign(name = data["name"], start_time = data["start_time"], end_time = data["end_time"], budget = data["budget"], bid_amount = data["bid_amount"], title = data["title"], description = data["description"], banner= data["banner"], final_url= data["final_url"], used_amount = data["used_amount"], usage_rate = data["usage_rate"], user_id = user)
      camp.save()
    except User.DoesNotExist:
      return JsonResponse({"status": "error", "message": "user does not exist"}, status= 400)

    return JsonResponse({"create status" : "success"})

@csrf_exempt
def edit_campaign(request, campaign_id):
  if request.method == "POST":
    #covert input to json format
    data = json.loads(request.body)

    try:
      CampaignSchema().load(data)
    except ValidationError as err:
      pprint(err.messages)
      return JsonResponse({"status": "error validation", "message": err.messages}, status=400)
    test = "name"
    try:
      camp = Campaign.objects.get(id=campaign_id)
      camp.name = data["name"]
      camp.start_time = data["start_time"]
      camp.end_time = data["end_time"]
      camp.budget = data["budget"]
      camp.bid_amount = data["bid_amount"]
      camp.title = data["title"]
      camp.description = data["description"]
      camp.banner = data["banner"]
      camp.final_url = data["final_url"]
      camp.used_amount = data["used_amount"]
      camp.usage_rate = data["usage_rate"]
      camp.save()
    except Campaign.DoesNotExist:
      return JsonResponse({"status": "error", "message": "Campaign does not exist"}, status= 400)

    return JsonResponse({"Edit status" : "success"})

@csrf_exempt
def delete_campaign(request, campaign_id):
  if request.method == "POST":
    try:
      camp = Campaign.objects.get(id=campaign_id)
      camp.delete()
    except Campaign.DoesNotExist:
      return JsonResponse({"status": "error", "message": "Campaign does not exist"}, status= 400)

    return JsonResponse({"Delete status" : "success"})
