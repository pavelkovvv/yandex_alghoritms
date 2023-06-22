"""
Лишняя буква

Васе очень нравятся задачи про строки, поэтому он придумал свою.
Есть 2 строки s и t, состоящие только из строчных букв. Строка t
получена перемешиванием букв строки s и добавлением 1 буквы в случайную
позицию. Нужно найти добавленную букву.

Формат ввода
На вход подаются строки s и t, разделённые переносом строки.
Длины строк не превосходят 1000 символов. Строки не бывают пустыми.

Формат вывода
Выведите лишнюю букву.

Пример 1
Ввод	            Вывод
abcd                e
abcde
"""


str1 = input()
str2 = input()

str1_list = [i for i in str1]
str2_list = [i for i in str2]
res = list()
str1_list.sort()
str2_list.sort()
str1_len = len(str1_list)
str2_len = len(str2_list)


def main():
    if str1_len > str2_len:
        for i in range(str1_len-1):
            if str1_list[i] == str2_list[i]:
                continue
            elif str1_list[i] != str2_list[i]:
                res.append(str1_list[i])
                return True
            else:
                res.append(str1_list[-1])
                return True
    elif str2_len > str1_len:
        for i in range(str2_len-1):
            if str2_list[i] == str1_list[i]:
                continue
            if str2_list[i] != str1_list[i]:
                res.append(str2_list[i])
                return True
            else:
                res.append(str2_list[-1])
                return True


main()

if len(res) > 0:
    for i in res:
        print(i)
elif len(res) == 0 and str1_len > str2_len:
    print(str1_list[-1])
elif len(res) == 0 and str2_len > str1_len:
    print(str2_list[-1])
