import oss2
import datetime

endpoint = 'http://oss-cn-shanghai-internal.aliyuncs.com'

auth = oss2.Auth('access_key', 'key_secret')
bucket = oss2.Bucket(auth, endpoint, 'noversioning')

for i in range(1,21):
    a = datetime.datetime.now()
    suffix = a.strftime("%Y%m%d%H%M%S")
    key = 'test' + suffix
    bucket.put_object_from_file(key, '/root/test')
