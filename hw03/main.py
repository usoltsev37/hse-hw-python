from pathlib import Path

import numpy as np

from matrix import Matrix
from matrix_mixins import MatrixMixinsMedium

output_dirs = [
    Path('artifacts/easy'),
    Path('artifacts/medium'),
    Path('artifacts/hard')
]


def easy():
    np.random.seed(0)
    m1 = Matrix(np.random.randint(0, 10, (10, 10)))
    m2 = Matrix(np.random.randint(0, 10, (10, 10)))
    with open(output_dirs[0] / 'matrix+.txt', 'w') as f:
        f.write((m1 + m2).__str__())
    with open(output_dirs[0] / 'matrix*.txt', 'w') as f:
        f.write((m1 * m2).__str__())
    with open(output_dirs[0] / 'matrix@.txt', 'w') as f:
        f.write((m1 @ m2).__str__())


def medium():
    np.random.seed(0)
    m1 = MatrixMixinsMedium(np.random.randint(0, 10, (10, 10)))
    m2 = MatrixMixinsMedium(np.random.randint(0, 10, (10, 10)))
    with open(output_dirs[1] / 'matrix+.txt', 'w') as f:
        f.write((m1 + m2).__str__())
    with open(output_dirs[1] / 'matrix*.txt', 'w') as f:
        f.write((m1 * m2).__str__())
    with open(output_dirs[1] / 'matrix@.txt', 'w') as f:
        f.write((m1 @ m2).__str__())


def hard():
    A = Matrix([[0, 1], [7, 3]])
    C = Matrix([[6, 4], [1, 0]])
    B = Matrix([[0, 1], [2, 3]])
    D = Matrix([[0, 1], [2, 3]])
    AB = A @ B
    CD = C @ D
    with open(output_dirs[2] / 'A.txt', 'w') as f:
        f.write(A.__str__())
    with open(output_dirs[2] / 'B.txt', 'w') as f:
        f.write(B.__str__())
    with open(output_dirs[2] / 'C.txt', 'w') as f:
        f.write(C.__str__())
    with open(output_dirs[2] / 'D.txt', 'w') as f:
        f.write(D.__str__())
    with open(output_dirs[2] / 'B.txt', 'w') as f:
        f.write(AB.__str__())
    with open(output_dirs[2] / 'CD.txt', 'w') as f:
        f.write(CD.__str__())
    with open(output_dirs[2] / 'hash.txt', 'w') as fp:
        fp.write("Hash A @ B = " + str(AB.__hash__()))
        fp.write("\nHash C @ D = " + str(CD.__hash__()))


if __name__ == '__main__':
    for dir in output_dirs:
        dir.mkdir(exist_ok=True, parents=True)

    easy()
    medium()
    hard()
