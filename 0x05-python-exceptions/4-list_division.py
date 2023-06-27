#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                item_1 = my_list_1[i]
                item_2 = my_list_2[i]

                if isinstance(item_1, (int, float)) and
                isinstance(item_2, (int, float)):
                    try:
                        result = item_1 / item_2
                    except ZeroDivisionError:
                        result = 0
                        print("division by 0")
                else:
                    result = 0
                    print("wrong type")
            except IndexError:
                result = 0
                print("out of range")

            new_list.append(result)
    finally:
        return new_list
