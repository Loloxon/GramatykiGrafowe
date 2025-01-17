from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.production import Production


class P16(Production):
    @property
    def _name(self) -> str:
        return "P16"

    @property
    def _left_side(self) -> HyperGraph:
        nodes = [
            Node(0, 0, False, is_production_relevant=False),  # 1
            Node(1, 0, False, is_production_relevant=False),  # 2
            Node(1, 1, False, is_production_relevant=False),  # 3
            Node(0, 1, False, is_production_relevant=False),  # 4
            Node(-0.5, 0.5, False, is_production_relevant=False)  # 5
        ]
        edges = []
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]],
                False,
                label="P"
            )
        ]
        return HyperGraph(
            nodes=nodes,
            edges=edges,
            hyperedges=hyperedges
        )

    @property
    def _right_side(self) -> HyperGraph:
        nodes = [
            Node(0, 0, False, is_production_relevant=False),  # 1
            Node(1, 0, False, is_production_relevant=False),  # 2
            Node(1, 1, False, is_production_relevant=False),  # 3
            Node(0, 1, False, is_production_relevant=False),  # 4
            Node(-0.5, 0.5, False, is_production_relevant=False)  # 5
        ]
        edges = []
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]],
                True,
                label="P"
            )
        ]
        return HyperGraph(
            nodes=nodes,
            edges=edges,
            hyperedges=hyperedges
        )

    def transform(self, graph: HyperGraph, node_map: dict[Node, Node], left_side: HyperGraph) -> (bool, HyperGraph):
        graph.hyperedges[0].is_removable = not graph.hyperedges[0].is_removable

        return True, graph