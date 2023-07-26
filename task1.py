# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.


import argparse
from path_to_the_directory import path_dir

def parse_ars():
    parser = argparse.ArgumentParser(description="text.txt")
    parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='введите путь к директории')
    args = parser.parse_args()
    return args.p

def main():
    for place in parse_ars():
        for item in (path_dir(place)):
            print(repr(item))

if __name__ == '__main__':
    main()
