# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def file_path(full_path):
    parts = full_path.split('\\')
    return ('/'.join(parts[:-1]), *parts[-1].split('.'),)
    # как соеденить через \ при при '\\' возвращается двойной ?
print(file_path(r'c:\Users\user\Documents\GeekBrains\python\Lesson5\task1.py'))