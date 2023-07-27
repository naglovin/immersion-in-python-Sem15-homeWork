from collections import namedtuple
import os
import logging


FORMAT = ("{asctime} - {levelname}: {msg}")

logging.basicConfig(filename='file', filemode='w', format=FORMAT, style='{', level=logging.INFO)
log = logging.getLogger()

Clas_Dir = namedtuple('Clas_Dir', 'name ext is_dir parent', defaults=['', '', False, ''])   # (имя файла, расширение, директория или нет, родительская директория) - кортеж
def path_dir(path_string):
    cl_objects = []
    if not path_string:
        path_string = os.getcwd()
        log.warning(f'Путь установлен по умолчанию {path_string}')
    path_string = os.path.abspath(path_string)
    parent = path_string.rstrip('/').rsplit('/', 1)[1]          # получаем абсолютный путь
    try:
        for item in os.listdir(path_string):
            obj_name, obj_ext = None, None
            item: str = item.rsplit('/', 1)[1]
            if item.rfind('.') != -1 and not item.startswith('.'):
                obj_name, obj_ext = item.rsplit('.', 1)
            else:
                obj_name = item
            cl_objects.append(cl_objects(name=obj_name, ext=obj_ext, parent=parent, is_dir=False))
        log.info(msg=str(cl_objects[-1]))
    except Exception as ex:
        print(f' {ex.__class__.name__}')
        log.error(msg=f'{ex.__class__.name__}: {ex}')
    return cl_objects                                   # список наименованных кортежей

if __name__ == '__main__':
    print()