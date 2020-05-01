#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for hidd in dir(hidden_4):
        if (hidd != '_'):
            print("{}".format(hidd))
