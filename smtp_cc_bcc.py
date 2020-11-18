import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send_email():
    """
    Send an email
    """
    subject = "Test email from Python"
    sender = 'jszxtsj@163.com'
    to_emails = ["group@aaa.com"]
    cc_emails = ["dhutsj@gmail.com", "jszxtsj@163.com"]
    bcc_emails = ["jszxtsj@163.com"]
    smtpServer = 'smtp.163.com'
    username = 'jszxtsj@163.com'
    password = ''

    mail_body = '''Alarm email for mars.
Mars Staging Report DB02 count more than 1M!
Please check Grafana to verify.
                    '''

    message = MIMEText(mail_body, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = ''.join(to_emails)
    message['CC'] = ';'.join(cc_emails)
    message['BCC'] = ''.join(bcc_emails)
    message['Subject'] = Header(subject, 'utf-8')
    print(message.as_string())

    emails = to_emails + cc_emails + bcc_emails
    print(emails)

    smtp = smtplib.SMTP()
    smtp.connect(smtpServer)
    smtp.login(username, password)
    smtp.sendmail(sender, emails, message.as_string())
    print("Email sent success.")
    smtp.quit()


if __name__ == "__main__":
    send_email()
