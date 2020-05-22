import pytz
import datetime
import time

def parse_time_string(start_time_string, end_time_string):
    est = pytz.timezone("America/New_York")
    start_time = datetime.datetime.strptime(start_time_string, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strptime(end_time_string, "%Y-%m-%d %H:%M:%S")
    t1 = est.localize(start_time)
    t2 = est.localize(end_time)
    utc_start_time = t1.astimezone(pytz.utc)
    utc_end_time = t2.astimezone(pytz.utc)

    utc_start_time_string = utc_start_time.strftime("%Y-%m-%d %H:%M:%S")
    utc_end_time_string = utc_end_time.strftime("%Y-%m-%d %H:%M:%S")

    print utc_start_time_string, utc_end_time_string

    start_timestamp = time.mktime(datetime.datetime.strptime(utc_start_time_string, "%Y-%m-%d %H:%M:%S").timetuple())
    end_timestamp = time.mktime(datetime.datetime.strptime(utc_end_time_string, "%Y-%m-%d %H:%M:%S").timetuple())

    return start_timestamp * 1000000, end_timestamp * 1000000

start_time_timestamp, end_time_timestamp = parse_time_string("2020-02-22 17:52:52", "2020-02-23 13:48:32")
print start_time_timestamp, end_time_timestamp