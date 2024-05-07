def print_list(arg):
    if isinstance(arg, list):
        return print(arg)
    else:
        return print("not list")


print_list([1, 2, 3, 4, 5])
print_list('something')


def max_number(a, b, c):
    print(max(a, b, c))
    return max(a, b, c)


max_number(4, 12, 7)


def return_min_print_max(*args):
    print(max(*args))
    return min(*args)


return_min_print_max(4, 12, 7, 10, 19)


def min_list(list_number):
    return min(list_number)


def max_list(list_number):
    return max(list_number)


def sum_list(list_number):
    return sum(list_number)


def av_list(list_number):
    return sum(list_number)/len(list_number)


print(min_list([5, 13, 7, 10, 19]))
print(max_list([5, 13, 7, 10, 19]))
print(sum_list([5, 13, 7, 10, 19]))
print(av_list([5, 13, 7, 10, 19]))
