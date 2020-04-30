#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys . argv) - 1 > 0):
        sum = 0
        for temp in range(1, len(sys . argv)):
            num = int(sys . argv[temp])
            sum = sum + num
        print("{:d}".format(sum))
    else:
        print("0")
