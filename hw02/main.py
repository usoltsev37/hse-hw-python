from visualization_ast_usoltsev.visualization import ASTVisualization
import visualization_ast_usoltsev.fibonacci as fb
import ast
import inspect
import os


def draw_table(table):
    cnt_cols = max(map(len, table))
    visualization = ASTVisualization("artifacts/ast")
    visualization.build(ast.parse(inspect.getsource(fb)))
    visualization.show()
    with open("artifacts/hard.tex", "w") as tex_file:
        tex_file.write(
            "\\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}\n"
            + "\\title{HW02}\n\\author{Nikita}\n\\date{March 2023}\n" \
            + f"\\begin{{center}}\n\\begin{{tabular}}{{{'|' + '|'.join(['c' for _ in range(cnt_cols)]) + '|'}}}\n\\hline\n" \
            + "\n".join(map(lambda row: " & ".join(str(value) for value in row) + " \\\\", table)) \
            + "\n\\hline\n\\end{tabular}\n\\end{center}\n"
            + "\\begin{center}\n\\end{center}\n"
            + "\\end{document}"
        )


if __name__ == '__main__':
    draw_table([[1, 2, 3, 4],
                [-1, 2, 3, -4],
                [1, 2, -3, 4],
                [1, -2, 3, 4]]
               )

    os.system("pdflatex -halt-on-error -output-directory artifacts artifacts/hard.tex artifacts/ast.png")
    os.system("rm artifacts/hard.aux artifacts/hard.log")
