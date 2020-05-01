#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if (len(sys.argv) - 1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        nun = int(sys.argv[1])
        nun2 = int(sys.argv[3])
        if (sys.argv[2] == '+'):
            if (len(sys.argv) - 1 >= 3):
                print("{} + {} = {}".format(nun, nun2, (add(nun, nun2))))
                exit(0)
        if (sys.argv[2] == '-'):
            if (len(sys.argv) - 1 >= 3):
                print("{} - {} = {}".format(nun, nun2, (sub(nun, nun2))))
                exit(0)
        if (sys.argv[2] == '*'):
            if (len(sys.argv) - 1 >= 3):
                print("{} * {} = {}".format(nun, nun2, (mul(nun, nun2))))
                exit(0)
        if (sys.argv[2] == '/'):
            if (len(sys.argv) - 1 >= 3):
                print("{} / {} = {}".format(nun, nun2, (div(nun, nun2))))
                exit(0)
        if (sys.argv[2] != '+', '-', '*', '/'):
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
