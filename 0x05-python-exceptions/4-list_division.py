#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    _list = []
    for i in range(list_length):
        try:
            j = my_list_1[i]/my_list_2[i]
        except IndexError:
            print("out of range")
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            _list.append(i)
    return _list
