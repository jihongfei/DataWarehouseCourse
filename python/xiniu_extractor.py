# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests
import os
import urllib2

html_space = '/Users/admin/JavaProjects/DataWarehouseCourse/python/htm/'
output_space = '/Users/admin/JavaProjects/DataWarehouseCourse/python/output'

#session = requests.Session()
#payload = {'mobile': '13146810601', 'password': '810601', 'rd': '0.9470549339899308'}
#session.post("http://www.xiniuedu.com/weishuedu/api/user/login", data=payload)
#r = session.get("http://www.xiniuedu.com/lab.html?task_id=1004&lab_id=107")
#print(r.text)

#data = open('/Users/admin/Downloads/xiniu_ex1.htm').read()
#print(data)
#html = requests.get().content



def extract_ipynb_url(link):
    s = link.find('www.xiniuedu.com/nas')
    e = link.rfind('?')
    if e == -1:
        e = len(link)
    link = link[s: e]
    link = url_unquote(link)
    print(link)
    return 'http://'+link[s: e]

def get_default_name(url):
    ext = '.ipynb'
    s = link.rfind('/')
    if s == -1:
        s = 0
    e = link.rfind(ext)
    if e == -1:
        e = len(url)
#    print('url:%s, s=%d ,e=%d' % (url, s, e))
    name = url[s:e]
#    print('before:'+name)
#    print('after:'+name)
    return name + ext

def url_unquote(encode_str):
    return urllib2.unquote(encode_str)

def download(url):
    r = requests.get(url)
    dname = get_default_name(url)
    with open(dname, "wb") as f:
        f.write(r.content)

for f in os.listdir(html_space):
    htm = html_space + f
    soup = BeautifulSoup(open(htm), 'html.parser', from_encoding='utf-8')
    for a in soup.find_all("a", class_="am-text-truncate textunder"):
        link = a.get('href')
        url = extract_ipynb_url(link)
#        download(url)
        get_default_name(url)