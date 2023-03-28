class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix
        self.cnt_rows = len(self._matrix)
        self.cnt_cols = len(self._matrix[0])
        self._cache = {}

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        self._matrix = matrix

    def __add__(self, other):
        self.__check_dimensions__(other)
        matrix = []
        for i, m in enumerate(other.matrix):
            matrix.append([m[j] + self._matrix[i][j] for j in range(len(m))])
        return Matrix(matrix)

    def __mul__(self, other):
        self.__check_dimensions__(other)
        matrix = []
        for i, m in enumerate(other.matrix):
            matrix.append([m[j] * self._matrix[i][j] for j in range(len(m))])
        return Matrix(matrix)

    def __matmul__(self, other):
        self.__check_dimensions__(other)
        if self.cnt_cols != other.cnt_rows:
            raise ValueError
        key = self.__hash__(), other.__hash__()
        if key in self._cache:
            return self._cache[key]
        matrix = [
            [sum(i * j for i, j in zip(row, col)) for col in list(zip(*other.matrix))] for row in self._matrix
        ]
        self._cache[key] = Matrix(matrix)
        return Matrix(matrix)

    def __str__(self):
        return '\n'.join(
            ['\t'.join(map(str, row)) for row in self._matrix]
        )

    def __check_dimensions__(self, other):
        if self.cnt_cols != other.cnt_cols or self.cnt_rows != other.cnt_rows:
            raise ValueError

    def __hash__(self):
        '''
        Сумма всех чисел матрицы по стадандартному простому модулю
        '''
        return sum(map(sum, self._matrix)) % (10 ** 9 + 7)
