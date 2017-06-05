import json
import re
import requests
import sys

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
    AUTH = data['auth']
    PAGE_ID = data['page_id']

# URL TYPE
INITIAL_URL = 'https://graph.facebook.com/v2.3/{page_id}/feed?limit=100&access_token={auth}'

def main(argv):
    url = INITIAL_URL.format(page_id=PAGE_ID, auth=AUTH)
    r = requests.get(url)
    j = r.json()
    f = open('db/corpus.txt', 'w+')

    while len(j['data']) > 0:
        for post in j['data']:
            if 'message' not in post:
                continue
            message = post['message']
            f.write(message + '\n')

        url = j['paging']['next']
        r = requests.get(url)
        print(url)
        j = r.json()

if __name__ == "__main__":
    main(sys.argv[1:])
