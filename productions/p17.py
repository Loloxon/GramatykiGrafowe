from copy import deepcopy

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.production import Production


class P17(Production):
    @property
    def _name(self) -> str:
        return "P17"

    @property
    def _left_side(self) -> HyperGraph:
        nodes = [
            Node(0, 0, False, is_production_relevant=False),  # 1
            Node(1, 0, False, is_production_relevant=False),  # 2
            Node(1, 1, False, is_production_relevant=False),  # 3
            Node(0, 1, False, is_production_relevant=False),  # 4
            Node(1, 0.5, True),  # 5
            Node(2, 0.5, False, is_production_relevant=False),  # 6
            Node(2, 1, False, is_production_relevant=False),  # 7
            Node(0.5, 0, False, is_production_relevant=False),  # 8
        ]
        edges = [
            Edge(nodes[2], nodes[4], True),  # 3 - 5
            Edge(nodes[4], nodes[1], True),  # 5 - 2
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[7]], False, label="P"
            ),
            HyperEdge([nodes[2], nodes[4], nodes[5], nodes[6]], True, label="Q"),
        ]
        return HyperGraph(nodes=nodes, edges=edges, hyperedges=hyperedges)

    def transform(
        self, graph: HyperGraph, node_map: dict[Node, Node], left_side: HyperGraph
    ) -> (bool, HyperGraph):
        node_mapper = lambda i: node_map[left_side.nodes[i - 1]]

        hyper_edge_nodes = [node_mapper(i) for i in [1, 8, 2, 3, 4]]
        graph.remove_hyperedge(hyper_edge_nodes)
        graph.add_hyperedge(hyper_edge_nodes, True, "P")

        return True, graph
