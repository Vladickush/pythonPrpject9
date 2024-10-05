# Задание по теме "Генераторы"

def all_variants(text):
    end = len(text)
    m = 0
    while m < end:
        i = 0
        while i < end - m:
            yield text[i: i + m + 1]
            i += 1
        m += 1


a = all_variants("abc")
for i in a:
    print(i)
