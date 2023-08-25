# 📌Создайте класс Матрица.
# Добавьте методы для:
# ○вывода на печать,
# ○сравнения,
# ○сложения,
# ○*умножения матриц


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(str(element) for element in row) + "\n"
        return matrix_str

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __add__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            raise ValueError("Matrices must have the same dimensions for addition.")

    def __mul__(self, other):
        if isinstance(other, Matrix) and self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication.")


# Пример использования класса Matrix
matrix1 = Matrix(2, 2)
matrix1.data = [[1, 2], [3, 4]]

matrix2 = Matrix(2, 2)
matrix2.data = [[5, 6], [7, 8]]

print(matrix1)  # Выводит:
# 1 2
# 3 4

print(matrix1 == matrix2)  # Выводит: False

matrix3 = matrix1 + matrix2
print(matrix3)


matrix4 = matrix1 * matrix2
print(matrix4)
