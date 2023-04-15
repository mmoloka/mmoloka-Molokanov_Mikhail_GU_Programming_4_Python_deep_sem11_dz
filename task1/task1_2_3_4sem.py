from time import time

# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

class MyStr(str):
    """
    MyStr класс. Доступны все возможности класса str,
    дополнительно хранятся имя автора строки и время создания.
    """

    def __new__(cls, autor, value):
        """Метод управляет способом создания объекта класса и инициализирует его атрибуты. """
        instance = super().__new__(cls, value)
        instance.autor = autor
        instance.time = time()
        return instance


class Archive:
    """
    Archive класс. Хранит пару свойств - число и строку.
    При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются
    в пару списковархивов.
    """
    _count = None

    def __init__(self, num, string):
        """Конструктор класса, инициализирует атрибуты экземпляра класса."""
        self.num = num
        self.string = string

    def __new__(cls, *args, **kwargs):
        """Метод добавляет атрибуты предыдущего экземпляра в списки при создании нового экземпляра."""
        if cls._count is None:
            cls._count = super().__new__(cls)
            cls._count.list_num = []
            cls._count.list_str = []
        else:
            cls._count.list_num.append(cls._count.num)
            cls._count.list_str.append(cls._count.string)
        return cls._count
    
    def __str__(self):
        """Метод выводит представление экземпляра класса для пользователя."""
        return f'Число: {self.num}, строка: {self.string}'
    
    def __repr__(self):
        """Метод выводит представление для создания экземпляра класса."""
        return f'Экземпляр класса Archive хранит строку {self.string} и число {self.num}\n\'' \
               f'Ранее сохранено {self.list_str} и {self.list_num}'



if __name__ == '__main__':
    help(MyStr)
    help(Archive)

    string = MyStr('Pushkin', 'U Lukomoriya...')
    print(string)
    print(string.upper())
    print(string.split())
    print(string.autor)
    print(string.time)

    a = Archive(4, "qwerty")
    print(a)
    print(f'{a = }')
    b = Archive(3, "asdf")
    print(b)
    print(f'{b = }')
    c = Archive(125, 'zxcv')
    print(c)
    print(f'{c = }')
