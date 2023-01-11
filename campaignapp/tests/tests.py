import pytest
import json
import requests

# Create your tests here.
@pytest.mark.django_db
def test_get_all_campaign():
  response = requests.get("http://127.0.0.1:8000/campaignapp/allcampaign")
  # print(response.json())
  assert response.json() == {'result': {'0': {'name': 'campaign 1', 'start_time': '2023-01-05 00:00:00+00:00', 'end_time': '2023-01-07 00:00:00+00:00', 'budget': 10000, 'bid_amount': 10, 'title': 'campaign title', 'description': 'desc', 'banner': 'banner', 'final_url': 'url', 'used_amount': '0.00', 'usage_rate': '0.00', 'user_id': 1}, '1': {'name': 'campaign 2', 'start_time': '2023-01-05 00:00:00+00:00', 'end_time': '2023-01-07 00:00:00+00:00', 'budget': 10000, 'bid_amount': 10, 'title': 'campaign title', 'description': 'desc', 'banner': 'banner', 'final_url': 'url', 'used_amount': '0.00', 'usage_rate': '0.00', 'user_id': 1}, '2': {'name': 'campaign 3', 'start_time': '2017-09-29 00:00:00+00:00', 'end_time': '2017-10-30 00:00:00+00:00', 'budget': 10000, 'bid_amount': 10, 'title': 'campaign title', 'description': 'campaign description', 'banner': 'banner', 'final_url': 'https://www.youtube.com', 'used_amount': '0.00', 'usage_rate': '0.00', 'user_id': 2}, '3': {'name': 'campaign 4', 'start_time': '2017-09-29 00:00:00+00:00', 'end_time': '2017-10-30 00:00:00+00:00', 'budget': 10000, 'bid_amount': 10, 'title': 'campaign title', 'description': 'campaign description', 'banner': 'banner', 'final_url': 'https://www.youtube.com', 'used_amount': '0.00', 'usage_rate': '0.00', 'user_id': 1}, '4': {'name': 'campaign 5', 'start_time': '2017-09-29 00:00:00+00:00', 'end_time': '2017-10-30 00:00:00+00:00', 'budget': 10000, 'bid_amount': 10, 'title': 'campaign title', 'description': 'campaign description', 'banner': 'banner', 'final_url': 'https://www.youtube.com', 'used_amount': '0.00', 'usage_rate': '0.00', 'user_id': 1}, '5': {'name': 'campaign 6', 'start_time': '2017-09-29 00:00:00+00:00', 'end_time': '2017-10-30 00:00:00+00:00', 'budget': 10000, 'bid_amount': 10, 'title': 'campaign title', 'description': 'campaign 6 description', 'banner': 'banner', 'final_url': 'https://www.youtube.com', 'used_amount': '0.00', 'usage_rate': '0.00', 'user_id': 2}, '6': {'name': 'campaign 7', 'start_time': '2017-09-29 00:00:00+00:00', 'end_time': '2017-10-30 00:00:00+00:00', 'budget': 10000, 'bid_amount': 10, 'title': 'campaign title', 'description': 'campaign description', 'banner': 'banner', 'final_url': 'https://www.youtube.com', 'used_amount': '0.00', 'usage_rate': '0.00', 'user_id': 2}, '7': {'name': 'campaign 8', 'start_time': '2017-09-29 00:00:00+00:00', 'end_time': '2017-10-30 00:00:00+00:00', 'budget': 10000, 'bid_amount': 10, 'title': 'campaign title', 'description': 'campaign description', 'banner': 'banner', 'final_url': 'https://www.youtube.com', 'used_amount': '0.00', 'usage_rate': '0.00', 'user_id': 2}, '8': {'name': 'campaign 9', 'start_time': '2017-09-29 00:00:00+00:00', 'end_time': '2017-10-30 00:00:00+00:00', 'budget': 10000, 'bid_amount': 10, 'title': 'campaign title', 'description': 'campaign description', 'banner': 'banner', 'final_url': 'https://www.youtube.com', 'used_amount': '0.00', 'usage_rate': '0.00', 'user_id': 2}}}

def test_get_campaign_by_user():
  response = requests.get("http://127.0.0.1:8000/campaignapp/campaignbyuserid/2")
  print(response.json())
  # assert response.json() == {'result': "Hello, world. You're at the polls index."}
  assert response.json() == {
    "result": {
        "0": {
            "name": "campaign 3",
            "start_time": "2017-09-29T00:00:00Z",
            "end_time": "2017-10-30T00:00:00Z",
            "budget": 10000,
            "bid_amount": 10,
            "title": "campaign title",
            "description": "campaign description",
            "banner": "banner",
            "final_url": "https://www.youtube.com",
            "used_amount": "0.00",
            "usage_rate": "0.00",
            "user_id": 2
        },
        "1": {
            "name": "campaign 6",
            "start_time": "2017-09-29T00:00:00Z",
            "end_time": "2017-10-30T00:00:00Z",
            "budget": 10000,
            "bid_amount": 10,
            "title": "campaign title",
            "description": "campaign description",
            "banner": "banner",
            "final_url": "https://www.youtube.com",
            "used_amount": "0.00",
            "usage_rate": "0.00",
            "user_id": 2
        },
        "2": {
            "name": "campaign 7",
            "start_time": "2017-09-29T00:00:00Z",
            "end_time": "2017-10-30T00:00:00Z",
            "budget": 10000,
            "bid_amount": 10,
            "title": "campaign title",
            "description": "campaign description",
            "banner": "banner",
            "final_url": "https://www.youtube.com",
            "used_amount": "0.00",
            "usage_rate": "0.00",
            "user_id": 2
        },
        "3": {
            "name": "campaign 8",
            "start_time": "2017-09-29T00:00:00Z",
            "end_time": "2017-10-30T00:00:00Z",
            "budget": 10000,
            "bid_amount": 10,
            "title": "campaign title",
            "description": "campaign description",
            "banner": "banner",
            "final_url": "https://www.youtube.com",
            "used_amount": "0.00",
            "usage_rate": "0.00",
            "user_id": 2
        }
    }
}

