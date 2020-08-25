#!/usr/bin/python3
""" this is a comment """
import requests
from sys import argv

if __name__ == '__main__':
    """ script that takes your Github
        credentials (username and password)
        and uses the Github API
        to display your id """
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(username, password))
    print(req.json().get("id"))
