import fibonacci as fb
import inspect
import ast
from visualization import ASTVisualization


if __name__ == '__main__':
    visualization = ASTVisualization("artifacts/ast")
    visualization.build(ast.parse(inspect.getsource(fb)))
    visualization.show()
