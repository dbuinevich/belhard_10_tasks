"""
Написать функцию revert_rows, которая принимает путь к файлу и делает новый
файл. Создать новый файл, каждая строка которого получается из соответствующей
строки исходного файла перестановкой слов в обратном порядке.
"""


def revert_rows():
    text = open('text.txt', 'r+')
    reverted_text = open('reverted_text.txt', 'a')
    lines_to_revert = text.readlines()
    for line in lines_to_revert:
        change_line = line.split(' ')
        change_line[-1] = change_line[-1].removesuffix('.\n')
        change_line.reverse()
        new_line = ' '.join(change_line)
        reverted_text.write(new_line + '\n')


if __name__ == '__main__':
    revert_rows()
