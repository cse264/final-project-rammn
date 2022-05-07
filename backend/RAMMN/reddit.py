from flask import (
    Blueprint, request, session, abort
)

import requests
import json

bp = Blueprint('reddit', __name__, url_prefix='/reddit')

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