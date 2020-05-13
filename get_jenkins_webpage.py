import requests
from bs4 import BeautifulSoup

"""
if version of requests is <= 2.16.0:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
else:
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
"""

url = '/consoleFull'
log_file = './ccc.log'


def get_content(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    with open(log_file, 'wb') as f:
        for item in soup.select("#main-panel > pre"):
            f.write(item.get_text().encode("utf-8"))


if __name__ == '__main__':
    get_content(url)
