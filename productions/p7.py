from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.production import Production


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
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], False, label="7")]
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

        graph.remove_hyperedge(list(filter(lambda x: not x.is_hanging, list(node_map.values()))))

        graph.add_hyperedge([node_1, node_2, node_3, node_4], True, label="8")

        return True, graph