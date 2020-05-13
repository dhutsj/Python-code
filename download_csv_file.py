import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download_csv_file():
    url = ""
    username = ""
    password = ""
    headers = {"User-Agent": "my-agent"}
    session = requests.session()
    chunk_size = 1024

    with session:
        res = session.get(url, auth=(username, password), headers=headers, verify=False, stream=True)
        with open("target.csv", 'wb') as fd:
            for chunk in res.iter_content(chunk_size):
                fd.write(chunk)


if __name__ == '__main__':
    download_csv_file()
