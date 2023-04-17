from random import randint

# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix:

    def __init__(self, lines, columns, matrix=[[]]):
        self.lines = lines
        self.columns = columns
        if self.lines == self.columns == 0:
            self.matrix = matrix
        else:
            self.matrix = [[0] * self.columns for _ in range(self.lines)]
            for i in range(self.lines):
                for j in range(self.columns):
                    self.matrix[i][j] = randint(1, 9)

    def __str__(self):
        result = ''
        for i in range(self.lines):
            for j in range(self.columns):
                result += f'{self.matrix[i][j]}  '
            result += '\n'
        return result
    
    def __eq__(self, other):
        if self.lines != other.lines or self.columns != other.columns:
            return False
        for i in range(self.lines):
            for j in range(self.columns):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True     

    def __ne__(self, other):
        if self.lines != other.lines or self.columns != other.columns:
            return True
        for i in range(self.lines):
            for j in range(self.columns):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return True
        return False       

    def __add__(self, other):
        if self.lines != other.lines or self.columns != other.columns:
            return 'Складывать можно только матрицы одинакового размера.'
        else:
            matrix = [[0] * self.columns for _ in range(self.lines)]
            result = ''
            for i in range(self.lines):
                for j in range(self.columns):
                    matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                    result += f'{matrix[i][j]:>2}  '
                result += '\n'
            return result   

    def __mul__(self, other):
        if self.columns != other.lines:
            return 'Уножать можно только согласованные матрицы.'
        else:
            matrix = [[0] * other.columns for _ in range(self.lines)]
            result = ''
            for i in range(self.lines):
                for j in range(other.columns):
                    for k in range(other.lines):
                        matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                    result += f'{matrix[i][j]:>2}  '
                result += '\n'
            return result   


if __name__ == '__main__':
    m1 = Matrix(5, 7)
    m2 = Matrix(5, 7)
    print(m1)
    print(m2)
    print(m1 + m2)
    print(m1 == m2)
    print(m1 == m1)
    print(m2 == m2)
    print(m1 != m2)
    print(m1 != m1)
    print(m2 != m2)

    m3 = Matrix(2, 2)
    m4 = Matrix(2, 3)
    print(m3)
    print(m4)
    print(m3 * m4)
    print(m1 * m2)



