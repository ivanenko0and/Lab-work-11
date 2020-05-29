
"""
Дан текстовий файл f. Видалити з нього останній рядок, результат записати у файл g.

Виконав Іваненко Андрій Вадимович
"""

import random


answer = '1'
while answer == '1':

    f = open('f.txt', 'w')  # Заповнення файлу f.txt
    # lines - список з випадкової кількості рядків, що складаються з випадкової кількості випадкових латинських літер
    lines = ["".join([chr(random.randint(97, 122)) for i in range(random.randint(5, 20))])
             for j in range(random.randint(3, 10))]
    length = len(lines)
    for i in range(length):
        f.write(lines[i])
        if i != length - 1:
            f.write("\n")
    f.close()

    f = open('f.txt', 'r+')
    text = f.read()
    print(f"Файл f.txt містить такі дані: \n{text}")  # Виведення даних файлу f.txt
    last_enter_index = text.rfind("\n")  # last_enter_index - індекс входження останнього Enter-а файлу f.txt
    last_line = text[last_enter_index + 1:]  # last_line - останній рядок файлу f.txt
    f.truncate(last_enter_index + length - 2)  # Видалення останнього рядку з файлу f.txt
    """ Оскільки '\n' для об'єкту типу str рахується як один символ, а для текстового файлу - як два, 
    то до позиції останнього рядка також додається кількість рядків, тобто кількість символів '\n' 
    (також віднімається 2, щоб не зараховувався останній символ '\n'). """
    f.close()

    g = open('g.txt', 'w')  # Перенесення останнього рядку файлу f.txt у файл g.txt
    g.write(last_line)
    g.close()

    print(f"Останній рядок файлу f.txt, який переходить до файлу g.txt, дорівнює: {last_line}")

    answer = input("Введіть '1' для повторення:")

