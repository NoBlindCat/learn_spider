# coding=utf-8
import requests
from bs4 import BeautifulSoup
import json
import os

index_url = 'http://www.mzitu.com/150001'
base_path = '/home/noblindcat/PycharmProjects/learn_spider/images'


def parse_index():
    """
    解析mzitu首页
    :return:
    """
    session = requests.Session()

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'http://www.mzitu.com',
        'referer': 'http://www.mzitu.com/xinggan',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    resp = session.post(url=index_url, headers=headers)

    # print resp
    # print resp.content
    url = "http://i.meizitu.net/2018/09/07b02.jpg"
    parse_mmpage(session, url=url)


def parse_mmpage(session, url):
    if not os.path.exists(base_path):
        os.mkdir(base_path)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'zh-CN,zh;q=0.9',
        'referer': 'http://www.mzitu.com/150001/2',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    }
    resp = session.get(url=url, headers=headers)
    print resp
    content = resp.content
    with open(os.path.join(base_path, 'img1.jpg'), 'wb') as f:
        f.write(content)
    # content = resp.content
    # bsobj = BeautifulSoup(content, 'lxml')
    #
    # img_list = bsobj.find('div', {'class': 'main-image'})
    # print img_list
    # for img in img_list:
    #     src = img.get('src')
    #     print src


# def download_img(url, path, name):
#     """
#     download a img
#     :param url: 地址
#     :param path: 保存路径
#     :param name: 保存名称
#     :return:
#     """
#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'Host': 'img.alicdn.com',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
#     }
#


if __name__ == '__main__':
    parse_index()