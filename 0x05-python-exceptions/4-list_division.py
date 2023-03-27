#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = list()
    for element in range(list_length):
            try:
                answer = my_list_1[element] / my_list_2[element]
            except (ValueError, TypeError):
                print("wrong type")
                answer = 0
            except ZeroDivisionError:
                print("division by 0")
                answer = 0
            except IndexError:
                print("out of range")
                answer = 0
            finally:
                new_list.append(answer)
    return (new_list)
