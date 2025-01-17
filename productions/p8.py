from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.production import Production


class P8(Production):
    @property
    def _name(self) -> str:
        return "P8"

    @property
    def _left_side(self) -> HyperGraph:
        nodes = [Node(0, 0, False, is_production_relevant=False),
                 Node(1, 0, False, is_production_relevant=False),
                 Node(1, 1, False, is_production_relevant=False),
                 Node(0, 1, False, is_production_relevant=False),
                 Node(1, 0.5, True),
                 Node(2, 0.5, False, is_production_relevant=False),
                 Node(2, 1, False, is_production_relevant=False)]
        edges = [Edge(nodes[1], nodes[4], False),
                 Edge(nodes[2], nodes[4], False)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], False),
                      HyperEdge([nodes[2], nodes[4], nodes[5], nodes[6]], True, label="8")]
        return HyperGraph(
            nodes=nodes,
            edges=edges,
            hyperedges=hyperedges
        )

    @property
    def _right_side(self) -> HyperGraph:
        nodes = [Node(0, 0, False),
                 Node(1, 0, False),
                 Node(1, 1, False),
                 Node(0, 1, False),
                 Node(1, 0.5, True),
                 Node(2, 0.5, False),
                 Node(2, 1, False)]
        edges = [Edge(nodes[1], nodes[4], False),
                 Edge(nodes[2], nodes[4], False)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True),
                      HyperEdge([nodes[2], nodes[4], nodes[5], nodes[6]], True)]
        return HyperGraph(
            nodes=nodes,
            edges=edges,
            hyperedges=hyperedges
        )

    def transform(self, graph: HyperGraph, node_map: dict[Node, Node], left_side: HyperGraph) -> (bool, HyperGraph):
        graph.remove_hyperedge([node_map[left_side.nodes[0]], node_map[left_side.nodes[1]],
                                node_map[left_side.nodes[2]], node_map[left_side.nodes[3]]])
        graph.add_hyperedge([node_map[left_side.nodes[0]], node_map[left_side.nodes[1]],
                             node_map[left_side.nodes[2]], node_map[left_side.nodes[3]]], True)
        return True, graph
