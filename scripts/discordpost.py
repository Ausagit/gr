import sys
import requests

if len(sys.argv) > 3:
    url = sys.argv[1]
    post_name = sys.argv[2]
    post_content = sys.argv[3]

    # for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        "content": post_content,
        "username": post_name
    }

    result = requests.post(url, json=data)
