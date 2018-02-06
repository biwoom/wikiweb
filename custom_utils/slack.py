from slacker import Slacker
from custom_utils.basic_info import SLACK_TOKEN

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
        channel = '#contact_us'
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

class SlackBotDonate:
    def __init__(self, member_name, real_name, birth, mobile, to_member_email, addess, amount_of_donation, donation_message):
        self.token = SLACK_TOKEN
        
        self.member_name = member_name
        self.real_name = real_name
        self.birth = birth
        self.mobile = mobile
        self.to_member_email = to_member_email
        self.addess = addess
        self.amount_of_donation = amount_of_donation
        self.donation_message = donation_message
        
    def slack_one_time_donation_notify(self):
        token = self.token
        member_name = self.member_name
        real_name = self.real_name
        birth = self.birth
        mobile = self.mobile
        to_member_email = self.to_member_email
        addess = self.addess
        amount_of_donation = self.amount_of_donation
        donation_message = self.donation_message
    
        # 슬랙 알림
        text = 'INB 일시후원 신청'
        channel = '#donation'
        username = 'inb_bot'
        attachments = [{
            "color": "#36a64f",
            "title": "후원신청",
            "title_link": "https://wiki-blog-dict-biwoom.c9users.io/",
            "fallback": "후원신청 알림",
            "fields": [
                {
                    "title": '후원자아이디',
                    "value": member_name,
                    "short": True
                },
                {
                    "title": '성명',
                    "value": real_name,
                    "short": True
                },
                {
                    "title": '생년월일',
                    "value": birth,
                    "short": True
                },
                {
                    "title": '휴대전화',
                    "value": mobile,
                    "short": True
                },
                {
                    "title": '주소',
                    "value": addess,
                    "short": True
                },
                {
                    "title": '이메일',
                    "value": to_member_email,
                    "short": True
                },
                {
                    "title": '후원금액',
                    "value": amount_of_donation,
                    "short": True
                },
                {
                    "title": '내용',
                    "value": donation_message,
                    "short": False
                }
            ]
        }]
                
        slack = Slacker(token)
        slack.chat.post_message(text=text, channel=channel, username=username, attachments=attachments)