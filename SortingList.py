def sort_acending_order(list):
    sorted_list = []

    while (len(list) > 0):
        a = list[0]

        for i in range(len(list)):
            if list[i] < a:
                a = list[i]

        sorted_list.append(a)
        list.remove(a)

    return sorted_list


def sort_decending_order(list):
    sorted_list = []

    while (len(list) > 0):
        a = list[0]

        for i in range(len(list)):
            if list[i] > a:
                a = list[i]

        sorted_list.append(a)
        list.remove(a)

    return sorted_list






