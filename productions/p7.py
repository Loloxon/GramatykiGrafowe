from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.production import Production
from utils import find_subgraphs


class P7(Production):
    @property
    def _name(self) -> str:
        return "P7"

    @property
    def _left_side(self) -> HyperGraph:
        nodes = [Node(0, 0, False, False),
                 Node(1, 0, False, False),
                 Node(1, 1, False, False),
                 Node(0, 1, False, False)]
        edges = []
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], False)]
        return HyperGraph(
            nodes=nodes,
            edges=edges,
            hyperedges=hyperedges
        )

    @property
    def _right_side(self) -> HyperGraph:
        nodes = [Node(0, 0, False, False),
                 Node(1, 0, False, False),
                 Node(1, 1, False, False),
                 Node(0, 1, False, False)]
        edges = []
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]
        return HyperGraph(
            nodes=nodes,
            edges=edges,
            hyperedges=hyperedges
        )

    def transform(self, graph: HyperGraph, node_map: dict[Node, Node], left_side: HyperGraph) -> (bool, HyperGraph):
        node_1 = node_map[left_side.nodes[0]]
        node_2 = node_map[left_side.nodes[1]]
        node_3 = node_map[left_side.nodes[2]]
        node_4 = node_map[left_side.nodes[3]]

        graph.remove_hyperedge(list(node_map.values()))

        graph.add_hyperedge([node_1, node_2, node_3, node_4], True)

        return True, graph

    def apply_with_predicate(self, graph: HyperGraph) -> (bool, HyperGraph):
        left_side = self.get_left_side()
        node_maps = find_subgraphs(graph, left_side)

        for node_map in node_maps:
            if predicate(node_map):
                reversed_node_map = {v: k for k, v in node_map.items() if isinstance(v, Node) and isinstance(k, Node)}
                return self.transform(graph, reversed_node_map, left_side)

        return False, graph


def predicate(node_map):
    has_correct_node = False
    has_wrong_node = False
    for node in node_map.keys():
        if isinstance(node, Node):
            if node.x == 0.3 and node.y == 0.7:
                has_wrong_node = True
            elif node.x == 0.5 and node.y == 0.7:
                has_wrong_node = True
            elif node.x == 0.3 and node.y == 0.3:
                has_wrong_node = True
            elif node.x == 0.7 and node.y == 0.7:
                has_correct_node = True
    return has_correct_node and not has_wrong_node
