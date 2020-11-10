from elasticsearch import Elasticsearch
import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from datetime import datetime
import pytz


def get_max_count():
    es = Elasticsearch([{'host': '10.10.10.10', 'port': 9200}])
    # print(es)
    # res = es.search(index='mars-staging-report-db2-history', body={
    #     "query": {"match_all": {}},
    #     "sort": [
    #                {"Check_Time": "desc"}
    #             ],
    #     "_source": ["Check_Time", "Pending_CMD_Count"]
    #         }, size=100
    #                 )
    # pdb.set_trace()
    # print(res['hits']['hits'])
    # res = es.search(index='mars-staging-report-db2-history', body={
    #     "aggs": {
    #         "by_time": {
    #             "terms": {
    #                 "field": "Check_Time",
    #             },
    #             "aggs": {
    #                 "theMax": {
    #                     "max": {
    #                         "field": "Pending_CMD_Count"
    #                     }
    #                 }
    #             }
    #         }
    #     },
    #     "sort": [
    #         {"Check_Time": "desc"}
    #     ],
    # }, size=10)
    # print(res['aggregations']['by_time']['buckets'][0]['theMax']['value'])

    time_count_dict = {}
    while True:
        time.sleep(30)
        bj_tz = pytz.timezone('Asia/Shanghai')
        my_date = datetime.now(bj_tz)
        res = es.search(index='mars-staging-report-db2-history', body={
            "query": {"match_all": {}},
            "sort": [
                       {"Check_Time": "desc"}
                    ],
            "_source": ["Check_Time", "Pending_CMD_Count"]
                }, size=100
                        )
        for r in res['hits']['hits']:
            with open("aaa.log", "a+") as f:
                f.write("datetime is {}, count value is {}\n".format(r['_source']['Check_Time'], r['_source']['Pending_CMD_Count']))
            print("datetime is {}, count value is {}".format(r['_source']['Check_Time'], r['_source']['Pending_CMD_Count']))
            if r['_source']['Pending_CMD_Count'] >= 1000000:
                if time_count_dict.get(r['_source']['Check_Time'], False):
                    pass
                else:
                    time_count_dict[r['_source']['Check_Time']] = r['_source']['Pending_CMD_Count']
                    print('alarm triggered')
                    send_email()


def send_email():
    sender = 'jszxtsj@163.com'
    receiver = 'shuangjie.tian@aaa.com,shuangjie.tian@bbb.com'
    smtpServer = 'smtp.163.com'
    username = 'jszxtsj@163.com'
    password = ''

    mail_title = 'alarm email for mars'
    mail_body = '''Alarm email for mars.
Mars Staging Report DB02 count more than 1M!
Please check Grafana to verify.
                '''

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
    print("start script.")
    get_max_count()
    # send_email()
