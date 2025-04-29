import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# number of songs a traer
limit = str(3)


response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit="
    + limit
    + "&term="
    + sys.argv[1]
)
# print(json.dumps(response.json(), indent=2))


o = response.json()
print()
