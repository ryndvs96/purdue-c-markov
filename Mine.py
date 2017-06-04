import json
import re
import requests
import sys

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
    AUTH = data['auth']
    PAGE_ID = data['page_id']

# URL TYPE
INITIAL_URL = 'https://graph.facebook.com/v2.9/{page_id}/posts?limit=100&access_token={auth}'
PAGING_URL = 'https://graph.facebook.com/v2.9/{page_id}/posts?limit=100&after={after}&access_token={auth}'

def main(argv):
    url = INITIAL_URL.format(page_id=PAGE_ID, auth=AUTH)
    r = requests.get(url)
    j = r.json()
    f = open('db/corpus.txt', 'w+')
    pattern = re.compile('#\d{1,5}')

    while len(j['data']) > 0:
        for post in j['data']:
            if 'message' not in post:
                continue
            message = post['message']
            first = message.split(' ')[0]
            if pattern.match(first): 
                rem = len(first) + 1
                msg = message[rem:]
                print(first)
                #print(msg)
                f.write(msg + '\n')

        aft = j['paging']['cursors']['after']
        url = PAGING_URL.format(page_id=PAGE_ID, auth=AUTH, after=aft)
        r = requests.get(url)
        print(url)
        j = r.json()

if __name__ == "__main__":
    main(sys.argv[1:])
