from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .email_info import EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_HOST_NAME
import smtplib

class EmailSender:
    def __init__(self, to_member_email, message, member_name, subject):
        self.host = EMAIL_HOST
        self.port = EMAIL_PORT
        self.admin_email = EMAIL_HOST_USER
        self.admin = EMAIL_HOST_NAME
        self.password = EMAIL_HOST_PASSWORD
        self.from_email = self.admin_email
        
        # 단체
        # to_email_list = ["bingeoul@gmail.com", "hansoha7@gmail.com"]
        # 개인
        self.to_member_email = to_member_email
        self.message = message
        self.member_name = member_name
        self.subject = subject

# 회원개인 이메일 전송    
    def sending_one(self):
        try:
            email_conn = smtplib.SMTP(self.host, self.port)
            email_conn.ehlo()
            email_conn.starttls()
            email_conn.login(self.admin_email, self.password)
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = self.subject
            msg['From'] = self.from_email
            msg['To'] = self.to_member_email
            
            sender = "나란다불교학술원 운영진"
            receiver = self.member_name
            subject = self.subject
            text = self.message
            html = """
            <html>
              <head></head>
              <body>
                <h2>Hi!<br>How are you?</h2>
                 <p> 발신자 : %s </p>
                 <p> 수신자 : %s </p>
                 <p> 주제 : %s </p>
                 <p> 알림내용 </p>
                 <p> %s </p>
                 <p> 이 이메일은 나란다불교학술원 문의사항 이메일입니다.</p>
              </body>
            </html>
            """% (sender, receiver, subject, text)
            
            # part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')
            
            # msg.attach(part1)
            msg.attach(part2)
            
            email_conn.sendmail(self.from_email, self.to_member_email, msg.as_string())
            email_conn.quit()
        except smtplib.SMTPException:
            print("error sending email")

# 문의사항 이메일
    def contact_us(self):
        try:
            email_conn = smtplib.SMTP(self.host, self.port)
            email_conn.ehlo()
            email_conn.starttls()
            email_conn.login(self.admin_email, self.password)
            
            msg = MIMEMultipart('alternative')
            msg['Subject'] = self.subject
            msg['From'] = self.from_email
            msg['To'] = self.from_email
            
            sender = self.member_name
            sender_email = self.to_member_email
            subject = self.subject
            text = self.message
            html = """
            <html>
              <head></head>
              <body>
                <h2>Hi!<br>How are you?</h2>
                 <p> 발신자 : %s </p>
                 <p> 발신자 E-mail : %s </p>
                 <p> 주제 : %s </p>
                 <p> 문의내용 </p>
                 <p> %s </p>
                 <p> 이 이메일은 나란다불교학술원 문의사항 이메일입니다.</p>
              </body>
            </html>
            """% (sender, sender_email, subject, text)
            
            # part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')
            
            # msg.attach(part1)
            msg.attach(part2)
            
            email_conn.sendmail(self.from_email, self.from_email, msg.as_string())
            email_conn.quit()
        except smtplib.SMTPException:
            print("error sending email")
    