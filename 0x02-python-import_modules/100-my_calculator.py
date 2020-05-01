#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if (len(sys.argv) - 1 < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        if (sys.argv[2] == '+'):
            if (len(sys.argv) - 1 > 1):
                print("{} + {} = {}".format(sys.argv[1], sys.argv[3],\
                    (add(int(sys.argv[1]), int(sys.argv[3])))))
        if (sys.argv[2] == '-'):
            if (len(sys.argv) - 1 > 1):
                print("{} + {} = {}".format(sys.argv[1], sys.argv[3],\
                    (sub(int(sys.argv[1]), int(sys.argv[3])))))
        if (sys.argv[2] == '*'):
            if (len(sys.argv) - 1 > 1):
                print("{} + {} = {}".format(sys.argv[1], sys.argv[3],\
                    (mul(int(sys.argv[1]), int(sys.argv[3])))))
        if (sys.argv[2] == '/'):
            if (len(sys.argv) - 1 > 1):
                print("{} + {} = {}".format(sys.argv[1], sys.argv[3],\
                    (div(int(sys.argv[1]), int(sys.argv[3])))))
