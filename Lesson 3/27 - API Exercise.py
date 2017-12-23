import json
import requests
from pprint import pprint

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    # 
    # Once you've done this, return the name of the number 1 top artist in
    # Spain. 
    r = requests.get('https://api.github.com/events').text
    json_object = json.loads(r)
    # pprint(json_object)
    return json_object['topartists']['artist'][0]['name']
