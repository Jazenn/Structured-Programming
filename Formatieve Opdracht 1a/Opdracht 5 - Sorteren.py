import random

def lijst_zip(lijst_1, lijst_2):
    """
    :param lijst_1: De eerste lijst die meegegeven wordt om samengevoegd te worden.
    :param lijst_2: De tweede lijst die meegegeven wordt om samengevoegd te worden.
    :return: Een gesorteerde variant (lijst) van de twee meegegeven lijsten.
    """
    gesorteerde_lijst = []
    flag_1 = 0
    flag_2 = 0
    while True:
        if flag_1 >= len(lijst_1) and flag_2 >= len(lijst_2):
            break

        if flag_1 >= len(lijst_1):
            gesorteerde_lijst.append(lijst_2[flag_2])
            flag_2 += 1
        elif flag_2 >= len(lijst_2):
            gesorteerde_lijst.append(lijst_1[flag_1])
            flag_1 += 1

        elif flag_2 >= len(lijst_2) or lijst_1[flag_1] <= lijst_2[flag_2]:
            gesorteerde_lijst.append(lijst_1[flag_1])
            flag_1 += 1
        elif flag_1 >= len(lijst_1) or lijst_2[flag_2] < lijst_1[flag_1]:
            gesorteerde_lijst.append(lijst_2[flag_2])
            flag_2 += 1

    return gesorteerde_lijst


def merge_sort(lst):
    """
    :param lst: Een ongesorteerde lijst.
    :return: De gesorteerde variant van die lijst, uitgevoerd met een complexiteit van O(n log n).
    """
    copy_list = lst.copy()

    if not copy_list:
        return copy_list
    elif len(copy_list) == 1:
        return copy_list
    else:
        pointer_midden = len(copy_list) // 2
        lijst_1 = copy_list[:pointer_midden]
        lijst_2 = copy_list[pointer_midden:]

        lijst_1 = merge_sort(lijst_1)
        lijst_2 = merge_sort(lijst_2)

    return lijst_zip(lijst_1, lijst_2)


print(merge_sort([random.randrange(0, 100) for x in range(50)]))