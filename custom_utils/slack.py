from slacker import Slacker
from custom_utils.basic_info import SLACK_TOKEN


# def slack_notify(text, channel, username, attachments):
#     token = 'xoxb-288855504401-1rBL1UsVE5FUsvDIqdDMuypt' #토근값은 공개저장소에 공개되지 않도록 주의
#     slack = Slacker(token)
#     slack.chat.post_message(text=text, channel=channel, username=username, attachments=attachments)

class SlackBot:
    def __init__(self, to_member_email, message, member_name, subject):
        self.token = SLACK_TOKEN
        
        self.to_member_email = to_member_email
        self.message = message
        self.member_name = member_name
        self.subject = subject
        
    def slack_contact_us_notify(self):
        token = self.token
        member_email = self.to_member_email
        message = self.message
        member_name = self.member_name
        subject = self.subject
    
        # 슬랙 알림
        text = 'INB 문의'
        channel = '#general'
        username = 'inb_bot'
        attachments = [{
            "color": "#36a64f",
            "title": "문의이메일",
            "title_link": "https://wiki-blog-dict-biwoom.c9users.io/",
            "fallback": "문의이메일 알림",
            "fields": [
                {
                    "title": '발송자',
                    "value": member_name,
                    "short": True
                },
                {
                    "title": '발송자이메일',
                    "value": member_email,
                    "short": True
                },
                {
                    "title": '주제',
                    "value": subject,
                    "short": True
                },
                {
                    "title": '내용',
                    "value": message,
                    "short": False
                }
            ]
        }]
                
        slack = Slacker(token)
        slack.chat.post_message(text=text, channel=channel, username=username, attachments=attachments)