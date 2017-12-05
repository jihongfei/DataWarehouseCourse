# -*- coding: utf-8 -*-
"""
Spyder Editor

For crawling python notebook from xiniu.
Only support read from static htm page so far.

"""

from bs4 import BeautifulSoup
import requests
import os
import urllib2

html_space = '/Users/admin/JavaProjects/DataWarehouseCourse/python/htm/'
output_space = '/Users/admin/JavaProjects/DataWarehouseCourse/python/output/'

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
    link = url_unquote(str(link))
    link = link.decode('utf-8')
    return 'http://%s' % link

def get_default_name(url):
    ext = '.ipynb'
    s = url.rfind('/')
    if s == -1:
        s = 0
    e = url.rfind(ext)
    if e == -1:
        e = len(url)
    name = url[(s + 1) : e]
    return name + ext

def url_unquote(encode_str):
    return urllib2.unquote(encode_str)

def download(dir_name, url):
    r = requests.get(url)
    create_dir(os.path.join(output_space, dir_name))
    default_name = get_default_name(url)
    path = os.path.join(output_space, dir_name, default_name)
    print('DOWNLOADING:\n%s\nTO PATH:\n%s\n' % (url, path))
    with open(path, "wb") as f:
        f.write(r.content)

def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
for f in os.listdir(html_space):
    htm = html_space + f
    soup = BeautifulSoup(open(htm), 'html.parser', from_encoding='utf-8')
    for a in soup.find_all("a", class_="am-text-truncate textunder"):
        link = a.get('href')
        url = extract_ipynb_url(link)
        dir_name = f
        if dir_name.find('.htm') != -1:
            dir_name = dir_name[0: dir_name.find('.htm')]
        download(dir_name, url)
