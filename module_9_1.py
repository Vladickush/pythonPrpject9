# Задача "Вызов разом":

def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results


def max_(int_list):
    return max(int_list)


def min_(int_list):
    return min(int_list)


def len_(int_list):
    return len(int_list)


def sum_(int_list):
    return sum(int_list)


def sorted_(int_list):
    return sorted(int_list)


print(apply_all_func([6, 20, 15, 9], max, min), end='')
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
