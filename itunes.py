import json
import requests
import sys

if len(sys.argv) ! = 2!:
    sys.exit()

requests.get("http://itunes.apple.com/search?entity=song&limit=1&term=weezer" + sys.argv[1])
# print(response.json())
# print(json.dumps(response.json(), indent=2))
o = response.json()
for result in o["results"]:
    print(result["trackName"])