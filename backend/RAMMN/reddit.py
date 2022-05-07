from flask import (
    Blueprint, request, session, abort
)

import requests
import json
import time

bp = Blueprint('reddit', __name__, url_prefix='/reddit')

@bp.route('/profile')
def profile():
  profile = {}
  token = '1778087909870-Zbo6lvGydgQqoYUCXu6h4aspbKfEGA'
  headers = { 'User-agent': 'RAMMN', 'Authorization': 'Bearer ' + token }
  res = requests.get("https://oauth.reddit.com/api/v1/me.json", headers = headers).json()
  profile["display_name"] = res["subreddit"]["title"]
  profile["username"] = res["name"]
  profile["karma"] = res["total_karma"]
  age = time.time() - res["created"]
  hours = int(age / 60 / 60)
  days = int(hours / 24)
  years = int(days / 365.25)
  hours = int(hours - days * 24)
  days = int(days - years * 365.25)
  profile["account_age"] = str(years) + "y " + str(days) + "d " + str(hours) + "h"
  profile["bio"] = res["subreddit"]["public_description"]
  profile["link"] = "https://reddit.com" + res["subreddit"]["url"]
  profile["pic"] = res["snoovatar_img"]
  profile["id"] = res["id"]
  return profile

@bp.route('/<int:num>')
def reddit(num):
    results = [ {}, {}, {}, {}, {}, {} ]
    headers = { 'User-agent': 'RAMMN' }
    res = requests.get("https://api.reddit.com/subreddits/popular.json?limit=6", headers = headers).json()
    for i in range(6):
      results[i]["subreddit"] = res["data"]["children"][i]["data"]["display_name"]
      results[i]["image"] = res["data"]["children"][i]["data"]["header_img"]
      post = requests.get("https://api.reddit.com/r/" + results[i]["subreddit"] + "/hot.json?limit=" + str(num), headers = headers).json()
      results[i]["title"] = post["data"]["children"][num - 1]["data"]["title"]
      results[i]["description"] = post["data"]["children"][num - 1]["data"]["selftext"]
      results[i]["link"] = post["data"]["children"][num - 1]["data"]["url"]
    return json.dumps(results)

@bp.route('/interests')
def interests():
  interests = []
  token = 'asdf'
  headers = { 'User-agent': 'RAMMN', 'Authorization': 'Bearer ' + token }
  res = requests.get("https://www.reddit.com/subreddits/mine/subscriber.json", headers = headers).json()
  for i in range(len(res["data"]["children"])):
    interests.append({})
    interests[i]["subreddit"] = res["data"]["children"][i]["data"]["display_name_prefixed"]
    interests[i]["description"] = res["data"]["children"][i]["data"]["public_description"]
  return json.dumps(interests)
