# coding=utf-8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import requests
# from bs4 import BeautifulSoup
#
# header = {'Username': 'xunda', 'Password': 'user@xunda'}
# resp = requests.get('http://xunda.lds.txnetworks.net/', auth=('xunda', 'user@xunda'))
# print resp
# print resp.content
#
#
# bsobj = BeautifulSoup(resp.content, 'lxml')
# a_list = bsobj.find_all('a')
# for a in a_list:
#     print a.get('href')
# import datetime
#
# begin = datetime.date(2018, 9, 18)
# end = datetime.date(2018, 10, 15)
# d = begin
# delta = datetime.timedelta(days=1)
# while d <= end:
#     remote_name = d.strftime("%Y-%m-%d") + ".log.gz"
#     print remote_name
#     d += delta
print type(bytearray("asdf")) == type(b'234')
