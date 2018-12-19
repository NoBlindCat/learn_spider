# coding=utf-8
import requests
from bs4 import BeautifulSoup
import json
import os

index_url = 'https://www.damai.cn/'
# base_path = '/home/noblindcat/PycharmProjects/learn_spider/images'


def parse_index():
    session = requests.Session()

    resp = session.post(url=index_url)
    print(resp.content)


if __name__ == '__main__':
    parse_index()
