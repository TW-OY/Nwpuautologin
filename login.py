#!/usr/bin/env python
# encoding: utf-8


import base64
import requests
import socket
import platform
import fcntl
import struct
import time


IP_pre = '10.25'
Time_format = "%Y-%m-%d %H:%M:%S"


def ping():

    ping_response = requests.get('http://www.baidu.com', timeout=2)
    if ping_response.headers['connection'] == 'close':
        return False
    else:
        return True


def print_time():

    print (time.strftime(Time_format,time.localtime()) + '  ', end='')


#  def get_ip_address_win():
    #  #  win平台下的ip地址获取方法

    #  local_ip_list = socket.gethostbyname_ex(socket.gethostname())
    #  for local_ip in local_ip_list:
        #  if local_ip in local_ip:
            #  print(u"欢迎使用NWPU-WLAN-AUTOLOGIN")
            #  return True
        #  else:
            #  print(u"您似乎没有连接到NWPU-WLAN哦")
            #  return False


def get_ip_address_linux(ifname):
    #    linux平台下的ip地址获取方法

    socket_temp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_ip= socket.inet_ntoa(fcntl.ioctl(socket_temp.fileno(), 0x8915, struct.pack('256s', ifname[:15].encode('utf-8')))[20:24])
    if IP_pre in local_ip:
        print_time()
        print(u"欢迎使用NWPU-WLAN-AUTOLOGIN")
        return True
    else:
        print_time()
        print(u"您似乎没有连接到NWPU-WLAN哦")
        return False


def login(username,passwd):

    encode_passwd = base64.b64encode(passwd.encode())
    post_data = {'userName': username,
                 'userPwd': encode_passwd.decode(),
                 'serviceTypeHIDE': '',
                 'serviceType': '',
                 'userurl': '',
                 'userip': '',
                 'basip': '',
                 'language': 'Chinese',
                 'usermac': 'null',
                 'entrance': 'null',
                 'custompath': "templatePage/20140225230636305",
                 'portalProxyIP': '202.117.80.138',
                 'portalProxyPort': '50200',
                 'dcPwdNeedEncrypt': '1',
                 'assignIpType': '0',
                 'appRootUrl': 'http://202.117.80.138:8080/portal/',
                 'manualUrl': '',
                 'manualUrlEncryptKey': ''}
    custom_headers = {"Host": '202.117.80.138:8080',
                      "Origin": 'http://202.117.80.138:8080',
                      'Pragma': 'no-cache',
                      'Referer': 'http://202.117.80.138:8080/portal/templatePage/20140225230636305/login_custom.jsp',
                      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
                      'X-Requested-With': 'XMLHttpRequest',
                      'Accept': "text/plain, */*; q=0.01",
                      'Accept-Encoding': 'gzip, deflate',
                      'Accept-Language': 'zh-CN,zh;q=0.8',
                      'Cache-Control': 'no-cache',
                      'Connection': 'keep-alive',
                      'Content-Length': '353',
                      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    WiFiurl = 'http://202.117.80.138:8080/portal/pws?t=li'
    s = requests.Session()
    cookies = {'i_p_pl': 'JTdCJTIyZXJyb3JOdW1iZXIlMjIlM0ElMjIxJTIyJTJDJTIybmV4dFVybCUyMiUzQSUyMmh0dHAlM0ElMkYlMkYyMDIuMTE3LjgwLjEzOCUzQTgwODAlMkZwb3J0YWwlMkZ0ZW1wbGF0ZVBhZ2UlMkYyMDE0MDIyNTIzMDYzNjMwNSUyRmxvZ2luX2N1c3RvbS5qc3AlMjIlMkMlMjJxdWlja0F1dGglMjIlM0FmYWxzZSUyQyUyMmNsaWVudExhbmd1YWdlJTIyJTNBJTIyQ2hpbmVzZSUyMiUyQyUyMmFzc2lnbklwVHlwZSUyMiUzQTAlMkMlMjJpTm9kZVB3ZE5lZWRFbmNyeXB0JTIyJTNBMSUyQyUyMm5hc0lwJTIyJTNBJTIyJTIyJTJDJTIydmFsQ29kZVR5cGUlMjIlM0ElMjIwJTIyJTJDJTIyYnlvZFNlcnZlcklwJTIyJTNBJTIyMjAyLjExNy44MC4xMzglMjIlMkMlMjJieW9kU2VydmVySHR0cFBvcnQlMjIlM0ElMjI4MDgwJTIyJTJDJTIyaWZUcnlVc2VQb3B1cFdpbmRvdyUyMiUzQWZhbHNlJTJDJTIydWFtSW5pdEN1c3RvbSUyMiUzQSUyMjElMjIlMkMlMjJjdXN0b21DZmclMjIlM0ElMjJNVEE0JTIyJTdE'}
    #  cookies = s.get(WiFiurl)
    #  print (cookies.cookies)
    cookies_no ={'i_p_pl': 'i_p_pl=JTdCJTIycG9ydFNlcnZJbmNsdWRlRmFpbGVkUmVhc29uJTIyJTNBJTIyJUU2JTk3JUEwJUU1JThGJUFGJUU3JTk0JUE4JUU1JTg5JUE5JUU0JUJEJTk5JUU2JUI1JTgxJUU5JTg3JThGJTIxJTIyJTJDJTIyZV9jJTIyJTNBJTIycG9ydFNlcnZJbmNsdWRlRmFpbGVkQ29kZSUyMiUyQyUyMmVfZCUyMiUzQSUyMnBvcnRTZXJ2SW5jbHVkZUZhaWxlZFJlYXNvbiUyMiUyQyUyMmVycm9yTnVtYmVyJTIyJTNBJTIyNyUyMiU3RA'}
    response = s.post(url=WiFiurl, data=post_data, headers=custom_headers, cookies=cookies, allow_redirects=True)
    if response.cookies == cookies_no:
        print (u"密码似乎输错了或者您流量已经耗尽请重试")
        return False
    else:
        print (u"登录成功")
        return True


def main():

    #  if platform.system() == 'Linux':
    result = get_ip_address_linux("wlan0")
    #  if platform.system() == 'Windows':
        #  result = get_ip_address_win()
    if result == False:
        while True:
            time.sleep(10)
            if get_ip_address_linux('wlan0'):
                break
    print_time()
    main_username = input('请输入您的学号\n')
    print_time()
    main_passwd = input('请输入您的密码\n')
    login_result = login(main_username, main_passwd)
    while login_result == False:
        login_result = login(main_username, main_passwd)
    while True:
        if ping():
            pass
        else:
            print_time()
            print(u"您已掉线正在重连...")
            login(main_username, main_passwd)


if __name__ == '__main__':
    main()
