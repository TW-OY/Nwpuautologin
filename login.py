#!/usr/bin/env python3
# encoding: utf-8


import requests



def login():

    post_data = {'userName': '2012301972',
                 'userPwd': 'aGVoZWRh',
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
    cookie = {'i_p_pl': 'JTdCJTIyZXJyb3JOdW1iZXIlMjIlM0ElMjIxJTIyJTJDJTIybmV4dFVybCUyMiUzQSUyMmh0dHAlM0ElMkYlMkYyMDIuMTE3LjgwLjEzOCUzQTgwODAlMkZwb3J0YWwlMkZ0ZW1wbGF0ZVBhZ2UlMkYyMDE0MDIyNTIzMDYzNjMwNSUyRmxvZ2luX2N1c3RvbS5qc3AlMjIlMkMlMjJxdWlja0F1dGglMjIlM0FmYWxzZSUyQyUyMmNsaWVudExhbmd1YWdlJTIyJTNBJTIyQ2hpbmVzZSUyMiUyQyUyMmFzc2lnbklwVHlwZSUyMiUzQTAlMkMlMjJpTm9kZVB3ZE5lZWRFbmNyeXB0JTIyJTNBMSUyQyUyMm5hc0lwJTIyJTNBJTIyJTIyJTJDJTIydmFsQ29kZVR5cGUlMjIlM0ElMjIwJTIyJTJDJTIyYnlvZFNlcnZlcklwJTIyJTNBJTIyMjAyLjExNy44MC4xMzglMjIlMkMlMjJieW9kU2VydmVySHR0cFBvcnQlMjIlM0ElMjI4MDgwJTIyJTJDJTIyaWZUcnlVc2VQb3B1cFdpbmRvdyUyMiUzQWZhbHNlJTJDJTIydWFtSW5pdEN1c3RvbSUyMiUzQSUyMjElMjIlMkMlMjJjdXN0b21DZmclMjIlM0ElMjJNVEE0JTIyJTdE'}
    #  cookies = s.get(WiFiurl)
    #  print (cookies.cookies)
    response = s.post(url=WiFiurl, data=post_data, headers=custom_headers, cookies=cookie, allow_redirects=True)
    print (response.cookies)
    print (response.status_code)
    print (response.headers)
login()
