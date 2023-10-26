import requests
from bs4 import BeautifulSoup
import time
from slack_sdk import WebClient

BASE_URLS = [
    'https://home.sch.ac.kr/sch/06/010100.jsp',
    'https://home.sch.ac.kr/sch/06/010200.jsp',
    'https://home.sch.ac.kr/sch/06/010300.jsp',
    'https://home.sch.ac.kr/sch/06/020000.jsp',
]

def fetch_current_notices(fetch_url):
    try:
        response = requests.get(fetch_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        notice_list = soup.find('tbody').find_all('tr')
        
        current_notice_list = [
            {
                'title': notice.find('a').get_text(strip=True),
                'author': notice.find('td', {'class': 'writer'}).contents[2].strip(),
                'date': notice.find('td', {'class': 'date'}).contents[2].strip(),
                'href': fetch_url + notice.find('a')['href'],
            }
            for notice in notice_list if not notice.find('span', {'class': 'notice'})
        ]

        today = time.strftime('%Y-%m-%d')
        return [notice for notice in current_notice_list if notice['date'] == today]

    except Exception as e:
        raise Exception({"done": False, "error_message": str(e)})

def post_to_slack(notices, slack_token, slack_channel_id):
    client = WebClient(token=slack_token)
    for notice in notices:
        block = [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "순천향대학교 공지사항 알리미",
                    "emoji": True
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*제목:*\n{notice['title']}\n*작성자:*\n{notice['author']}\n*게시일:*\n{notice['date']}"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://avatars.slack-edge.com/2023-10-25/6079284493415_d57be27f27f6305cd06f_96.png",
                    "alt_text": "SCH thumbnail"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "emoji": True,
                            "text": "바로가기"
                        },
                        "style": "primary",
                        "url": notice['href'],
                    }
                ]
            },
            {
                "type": "divider"
            }
        ]
        try:
            client.chat_postMessage(
                channel=slack_channel_id,
                blocks=block,
                text=f"{notice['title']}"
            )
        except Exception as e:
            raise Exception({"done": False, "error_message": str(e)})

def main(args):
    for index, fetch_url in enumerate(BASE_URLS):
        slack_channel_key = f'slack_channel_id_{index + 1}'
        notices = fetch_current_notices(fetch_url=fetch_url)
        post_to_slack(notices, args['slack_token'], args[slack_channel_key])
    return {"done": True}
