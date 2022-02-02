from _ast import AST
import random
import networkx
import ast
import astunparse
from networkx.drawing.nx_pydot import graphviz_layout
from matplotlib import pyplot as plt


class ASTVisualization:
    def __init__(self, path: str):
        self._SIZE_X = 50
        self._SIZE_Y = 70
        self._NODE_SIZE = 5000
        self._ast_size = 0
        self._BLACK = "#000000"
        self._colours = []
        self._colours_ord = []
        self._SPECIAL_PARSING_COMPS = [ast.Compare, ast.Constant, ast.Name, ast.BinOp, ast.arguments]
        self._SPECIAL_PARSING_COLOURS = {comp: self._gen_rand_colour() for comp in self._SPECIAL_PARSING_COMPS}
        self._map_name_colour = {}
        self._path = path
        self._graph = networkx.Graph()
        self._map_id_name = {}

    def set_name_colour(self, node: AST, node_id: int):
        cl = node.__class__
        if cl in self._SPECIAL_PARSING_COMPS:
            name, colour = astunparse.unparse(node), self._SPECIAL_PARSING_COLOURS[cl]
        elif self._map_name_colour.__contains__(cl):
            name, colour = self._map_name_colour[cl]
        else:
            self._map_name_colour[cl] = str(cl), self._gen_rand_colour()
            name, colour = self._map_name_colour[cl]
        self._map_id_name[node_id] = name
        self._colours_ord.append(colour)

    def build(self, node: AST):
        self._dfs(node=node, parent_id=0)

    def show(self):
        plt.gcf().set_size_inches(self._SIZE_X, self._SIZE_Y)
        pos = graphviz_layout(self._graph, prog='dot')
        networkx.draw(self._graph,
                      pos=pos,
                      with_labels=True,
                      node_color=self._colours_ord,
                      labels=self._map_id_name,
                      node_size=self._NODE_SIZE,
                      node_shape='o')
        plt.savefig(self._path)

    def _gen_colour(self) -> str:
        return "#"+''.join([random.choice("ABCDEF0123456789") for _ in range(6)])

    def _gen_rand_colour(self) -> str:
        colour = self._gen_colour()
        while self._colours.count(colour) > 0 or self._BLACK == colour:
            colour = self._gen_colour()
        self._colours.append(colour)
        return colour

    def _dfs(self, node: AST, parent_id: int, depth=0):
        node_id = self._ast_size
        self._graph.add_node(node_id)
        if depth != 0:
            self._graph.add_edge(parent_id, node_id)
        self.set_name_colour(node, node_id)
        self._ast_size += 1
        if node is not ast.Name:
            for child in ast.iter_child_nodes(node):
                self._dfs(child, node_id, depth + 1)
        else:
            return
