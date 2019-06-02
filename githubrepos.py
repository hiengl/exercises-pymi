#!/usr/bin/env python3

__doc__ = '''
Viết 1 script để liệt kê tất cả các GitHub repository của 1 user:
    Ví dụ với user pymivn, sử dụng dữ liệu ở JSON format tại
        https://api.github.com/users/pymivn/repos

    Câu lệnh của chương trình có dạng:
        python3 githubrepos.py username

    Gợi ý:
    Sử dụng các thư viện:

        requests
        sys or argparse
'''

import sys
import requests

import log
logger = log.get_logger(__name__)


def get_repos(user):
    '''Trả về tất cả các GitHub repository của 1 user
    :param user: username của github repository
    '''

    path = 'https://api.github.com/users/{}/repos'.format(user)
    sec = requests.Session()
    res = sec.get(path)
    git_repos = res.json()

    return git_repos


def main():
    user = sys.argv[1]
    # Viết code xử lí truyền argument `user` bên dưới
    # user: username của github repository
    git_repos = get_repos(user)
    for repo in git_repos:
        repo = repo['name'].strip("'")
        print(repo)


if __name__ == "__main__":
    main()
