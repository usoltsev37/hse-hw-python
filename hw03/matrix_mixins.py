import numpy as np


class MatrixMixins:
    def __init__(self, matrix):
        self._matrix = matrix

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = np.asarray(value)

    def __str__(self):
        return '\n'.join(
            ['\t'.join(map(str, row)) for row in self.matrix]
        )

    def __repr__(self):
        return '%s(%r)' % (MatrixMixins.__name__, self.matrix)


class MatrixMixinsMedium(np.lib.mixins.NDArrayOperatorsMixin, MatrixMixins):
    def __array_ufunc__(self, f, method, *inputs, **kwargs):
        for i in inputs:
            if not isinstance(i, MatrixMixinsMedium):
                return ValueError
        inputs = [i.matrix for i in inputs]
        return MatrixMixinsMedium(getattr(f, method)(*inputs, **kwargs))
