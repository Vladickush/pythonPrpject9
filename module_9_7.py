# Задание: Декораторы в Python

def is_prime(add_indicator):
    def wropper(*args):
        a = sum(args)
        indicator = 'Простое'
        for i in range(2, a // 2 + 1):  # перебираем делители
            if a % i == 0:
                indicator = 'Составное'
                break
        print(indicator)
        return a
    return wropper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
