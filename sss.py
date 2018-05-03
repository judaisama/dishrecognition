# coding=utf-8
import json
import requests
load = {'loginname': 'umooc', 'password': 'BjTu@0!An'}
urllogin ='http://gsdb.bjtu.edu.cn/api/token/'
#urllogin ='http://127.0.0.1:8000/api/token/'
rlogin = requests.get(urllogin, params=load, verify=True)
print (rlogin.text)
data1 = json.loads(rlogin.text)
print (data1)
url ='http://gsdb.bjtu.edu.cn/api/v1/studentinfo/?token='+data1['token']
#url ='http://127.0.0.1:8000/api/v1/studentinfo/?token='+data1['token']
print url
rlogin = requests.get(url, verify=True)
print (rlogin)
data2 = json.loads(rlogin.text)
#print data2["objects"][2]['bmmc']