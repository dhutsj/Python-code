# -*- coding: utf-8 -*-


import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 发件人和收件人
sender = 'jszxtsj@163.com'
receiver = 'jszxtsj@163.com'

# 所使用的用来发送邮件的SMTP服务器
smtpserver = 'smtp.163.com'

# 发送邮箱的用户名和授权码（不是登录邮箱的密码）
username = 'jszxtsj@163.com'
password = ''

# 邮件主题
mail_title = '主题：html邮件'

# 读取html文件内容
f = open('gg.html', 'rb')  # HTML文件默认和当前文件在同一路径下，若不在同一路径下，需要指定要发送的HTML文件的路径
mail_body = f.read()
f.close()

# 邮件内容, 格式, 编码
message = MIMEText(mail_body, 'html', 'utf-8')
message['From'] = sender
message['To'] = receiver
message['Subject'] = Header(mail_title, 'utf-8')

try:
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, message.as_string())
    print("发送邮件成功！！！")
    smtp.quit()
except smtplib.SMTPException:
    print("发送邮件失败！！！")
