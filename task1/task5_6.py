# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

class Rectangle:
    """Rectangle класс. Предназначен для выполнения различных вычислений с прямоугольниками."""

    def __init__(self, length, width=None):
        """Конструктор класса, инициализирует атрибуты экземпляра класса(длину и ширину)."""
        self.length = length
        self.width = width or length

    def get_perimeter(self):
        """Метод определяет периметр экземпляра класса."""
        return 2 * (self.length + self.width)

    def get_square(self):
        """Метод определяет площадь экземпляра класса."""
        return self.length * self.width

    def __add__(self, other):
        """
        Метод создает новый экземпляр класса получаемый в результате сложения 
        двух экземпляров (по периметру).
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Rectangle' instance")
        ratio_width = self.width / self.get_perimeter()
        ratio_length = self.length / self.get_perimeter()
        new_perimetr = self.get_perimeter() + other.get_perimeter()
        return Rectangle(new_perimetr * ratio_length, new_perimetr * ratio_width)

    def __sub__(self, other):
        """
        Метод создает новый экземпляр класса получаемый в результате вычитания 
        двух экземпляров (по периметру, исключая отрицательные значения).
        """
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Rectangle' instance")
        ratio_width = self.width / self.get_perimeter()
        ratio_length = self.length / self.get_perimeter()
        new_perimetr = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(new_perimetr * ratio_length, new_perimetr * ratio_width)
    
    def __eq__(self, other):
        """Метод определяет, равны ли площади двух экземпляров класса."""
        return self.get_square() is other.get_square()

    def __ne__(self, other):
        """Метод определяет, не равны ли площади двух экземпляров класса."""
        return self.get_square() is not other.get_square()

    def __gt__(self, other):
        """Метод определяет, больше ли площадь первого экземпляра класса, чем второго."""
        return self.get_square() > other.get_square()

    def __lt__(self, other):
        """Метод определяет,меньше ли площадь первого экземпляра класса, чем второго."""
        return self.get_square() < other.get_square()
    
    def __le__(self, other):
        """Метод определяет,не больше ли площадь первого экземпляра класса, чем второго."""
        return self.get_square() <= other.get_square()
    
    def __ge__(self, other):
        """Метод определяет,не меньше ли площадь первого экземпляра класса, чем второго."""
        return self.get_square() >= other.get_square()
    
    def __str__(self):
        """Метод выводит представление экземпляра класса для пользователя."""
        return (f'\nПрямоугольник:\n{self.length} X {self.width}'
                f'\nПериметр: {self.get_perimeter()}'
                f'\nПлощадь:   {self.get_square()}')

    def __repr__(self):
        """Метод выводит представление для создания экземпляра класса."""
        return f'Rectangle({self.length}, {self.width})'


if __name__ == '__main__':
    help(Rectangle)

    a = Rectangle(10, 20)
    b = Rectangle(14,   7)
    print(a)
    print(repr(a))
    print(b)
    print(f'{b = }')
    print(a + b)
    print(b - a)
    print(a == b)
    print(a != b)
    print(a > b)
    print(b >= a)
    print(a < b)
    print(b <= a)