#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# description: ShowDoc
# author: xiaguliuxiang@foxmail.com
# date: 2019-10-29 20:00:00

import json

import requests


def write_to_file(file, content):
    with open(file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n\n\n')


def api_page_info(server, page_id):
    result = requests.post('{}/server/index.php?s=/api/page/info'.format(server), {'page_id': page_id})
    print('接口返回数据:{}'.format(result.text))
    page = json.loads(result.text)
    print('page_title:{},page_content:{}'.format(page['data']['page_title'], page['data']['page_content']))
    write_to_file('showdoc.txt', page['data'])


def main():
    server = 'http://129.28.201.138:24999'
    data = {
        'item_id': '1',
        'keyword': '',
        'default_page_id': '2'
    }
    result = requests.post('{}/server/index.php?s=/api/item/info'.format(server), data)
    item = json.loads(result.text)
    print('接口返回数据:{}'.format(item))

    menu = item['data']['menu']

    for page in menu['pages']:
        print('page_id:{},page_title:{}'.format(page['page_id'], page['page_title']))

    for catalogs in menu['catalogs']:
        print('cat_id:{},cat_name:{}'.format(catalogs['cat_id'], catalogs['cat_name']))
        for page in catalogs['pages']:
            print('page_id:{},page_title:{}'.format(page['page_id'], page['page_title']))
            api_page_info(server, page['page_id'])


if __name__ == '__main__':
    main()
