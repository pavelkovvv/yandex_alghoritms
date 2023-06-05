# ID успешной посылки: 87941661
def broken_search(arr: list, find_elem: int) -> int:
    start_index = 0
    end_index = len(arr) - 1
    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if arr[mid_index] == find_elem:
            return mid_index
        elif arr[start_index] <= arr[mid_index]:
            if arr[start_index] <= find_elem < arr[mid_index]:
                end_index = mid_index - 1
            else:
                start_index = mid_index + 1
        else:
            if arr[mid_index] < find_elem <= arr[end_index]:
                start_index = mid_index + 1
            else:
                end_index = mid_index - 1
    return -1


if __name__ == '__main__':
    quantity = int(input())
    target = int(input())
    arr = [int(num) for num in input().split()]
    print(broken_search(arr, target))

# Исправил свой альтернативный вариант, спасибо Вам:)


# def broken_search(x, find_elem) -> int:
#     try:
#         x = x[find_elem]                        # ЕСЛИ ЗАПРАШИВАЕМЫЙ ЭЛЕМЕНТ В СЛОВАРЕ НАЙДЕН, ТО
#         print(x)                                # ПЕЧАТАЕМ ЕГО ЗНАЧЕНИЕ (Т.Е. ИНДЕКС, КОТОРЫЙ МЫ ПРИСВОИЛИ)
#     except KeyError:
#         print(-1)                               # ЕСЛИ ЭЛЕМЕНТ НЕ НАЙДЕН, ТО ПЕЧАТАЕМ -1
#
#
# def test():
#     quantity = int(input())                     # СЧИТЫВАЕМ КОЛ-ВО ЭЛЕМЕНТОВ
#     find_elem = input()                         # СЧИТЫВАЕМ ЭЛЕМЕНТ КОТОРЫЙ НУЖНО НАЙТИ
#     x = {value: index for index, value in       # СЧИТЫВАЕМ МАССИВ ДАННЫХ И ИСПОЛЬЗУЯ DICT COMPREHENSION
#          enumerate(input().split())}
                                                  # ЗАПОЛНЯЕМ СЛОВАРЬ ГДЕ КЛЮЧАМИ БУДУТ ЯВЛЯТЬСЯ ВВЕДЁННЫЕ
                                                  # ДАННЫЕ, А ИХ ЗНАЧЕНИЯМИ БУДУТ НУЛИ
#     index = 0                                   # СЧЁТЧИК ДЛЯ ПРИСВОЕНИЯ ИНДЕКСА ЭЛЕМЕНТАМ СЛОВАРЯ
#     for key in x:                               # ДЛЯ ВСЕХ КЛЮЧЕЙ В СЛОВАРЕ
#         x[key] = index                          # ПРИСВАЕВАЕМ КЛЮЧУ (Т.Е. ЭЛЕМЕНТУ МАССИВА) ЕГО ИНДЕКС
#         index += 1                              # НА КАЖДОЙ ИТЕРАЦИИ УВЕЛИЧИВАЕМ ИНДЕКС НА 1
#     broken_search(x, find_elem)
#
#
# if __name__ == '__main__':
#     test()