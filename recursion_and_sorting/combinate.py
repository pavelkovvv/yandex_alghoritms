button_characters = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def generate_combinations(buttons, current_word, results):
    if not buttons:  # Если больше нет кнопок для обработки, текущее слово считается полным
        results.append(current_word)
        return

    current_button = buttons[0]  # Берем первую кнопку из оставшихся
    for char in button_characters[current_button]:
        # Рекурсивно вызываем функцию с оставшимися кнопками и обновленным текущим словом
        generate_combinations(buttons[1:], current_word + char, results)


# Пример использования
sequence = input()
results = []  # Здесь будут храниться все комбинации слов
generate_combinations(sequence, "", results)
print(*results)
