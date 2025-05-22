from classes import Graph
from pprint import pprint

if __name__ == "__main__":
    graph = Graph()

    graph.add_node(1)
    graph.add_node(3)
    graph.add_node(2)

    graph.set_edge(1, 2)

    pprint(graph.matrix)
