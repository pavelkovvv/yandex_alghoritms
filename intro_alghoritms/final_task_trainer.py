# ID успешной посылки: 86277353
from collections import Counter


def main():
    k = int(input()) * 2
    str1 = input()
    str2 = input()
    str3 = input()
    str4 = input()
    res_counter = 0
    # Объединяем всё в одну строку и убираем точки
    str_union = str1 + str2 + str3 + str4
    str_union = str_union.replace(".", "")
    count = Counter(str_union)
    for key, value in count.items():
        if value <= k:
            res_counter += 1
    print(res_counter)


if __name__ == '__main__':
    main()
