from elasticsearch import Elasticsearch
import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText


def get_max_count():
    es = Elasticsearch([{'host': '10.10.10.10', 'port': 9200}])
    # print(es)
    # res = es.search(index='history', body={'query': {}})
    # print(res['hits']['hits'])
    while True:
        time.sleep(600)
        res = es.search(index='history', body={
          "aggs": {
            "by_time": {
              "terms": {
                "field": "Check_Time",
              },
              "aggs": {
                "theMax": {
                  "max": {
                    "field": "CMD_Count"
                  }
                }
              }
            }
          }
        }, size=0)

        # print(res)
        if res['aggregations']['by_time']['buckets'][0]['theMax']['value'] >= 1000000:
            send_email()


def send_email():
    sender = 'jszxtsj@163.com'
    receiver = 'jszxtsj@163.com'
    smtpServer = 'smtp.163.com'
    username = 'jszxtsj@163.com'
    password = ''

    mail_title = 'alarm email'
    mail_body = 'alarm email test'

    message = MIMEText(mail_body, 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpServer)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
        print("Email sent success.")
        smtp.quit()
    except smtplib.SMTPException:
        print("Email sent failed.")


if __name__ == "__main__":
    get_max_count()
