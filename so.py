#!/usr/bin/env python3

__doc__ = '''
    Yêu cầu: Viết script lấy top N câu hỏi được vote cao nhất của tag LABEL
    trên stackoverflow.com.
    In ra màn hình: Title câu hỏi, link đến câu trả lời được vote cao nhất

    Link API: https://api.stackexchange.com/docs

    Dạng của câu lệnh:
        python3 so.py N LABEL
'''

import sys
import requests

import log
logger = log.get_logger(__name__)


def get_questions(N, tag):
    '''Trả về list N câu hỏi được vote cao nhất của tag được truyền vào

    :param N: số câu hỏi cần lấy
    :param tag: tên tag cần truyền vào
    '''

    path = 'https://api.stackexchange.com/2.2/questions?order=desc&sort=votes&tagged={}&site=stackoverflow'.format(tag)
    sec = requests.Session()
    res = sec.get(path)
    list_ques = res.json()
    questions = list_ques['items'][:int(N)]

    return questions


def main():
    N, tag = sys.argv[1:]
    # Viết code xử lí truyền 2 argument `N` và `tag` bên dưới
    # N: số câu hỏi cần lấy
    # tag: tên tag cần truyền vào
    questions = get_questions(N, tag)
    for question in questions:
        print(question['title'])
        print(question['link'] + '?answertab=votes#tab-top')


if __name__ == "__main__":
    main()
