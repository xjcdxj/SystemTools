import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if __name__ == '__main__':
    account = smtplib.SMTP()
    account.connect('smtp.office365.com', 587)
    account.login('yuxjc@outlook.com', 'xjc19960323XJC')
    msg = MIMEText("Hello World", 'plain', 'utf-8')
    account.sendmail('yuxjc@outlook.com', '1749736146@qq.com', msg.as_string())
