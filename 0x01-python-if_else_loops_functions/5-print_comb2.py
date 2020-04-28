#!/usr/bin/python3
for ch in range(100):
    if (ch != 99):
        print("{:02d}".format(ch), end=", ")
    else:
        print(ch)
