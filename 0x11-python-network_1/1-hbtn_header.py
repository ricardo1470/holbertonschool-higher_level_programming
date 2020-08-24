#!/usr/bin/python3
from urllib import request
from sys import argv
""" script that takes in a URL,
    sends a request to the URL and displays
    the value of the X-Request-Id variable found
    in the header of the response.
    -You must use the packages urllib and sys """


if __name__ == '__main__':
    with request.urlopen(argv[1]) as page:
        req_pag = page.headers.get("X-Request-Id")
    print(req_pag)
