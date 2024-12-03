from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.production import Production


class P2(Production):
    @property
    def _name(self) -> str:
        return "P2"

    @property
    def _left_side(self) -> HyperGraph:
        nodes = [Node(0, 0, False, "V"),
                 Node(1, 0, False, "V"),
                 Node(1, 1, False, "V"),
                 Node(0, 1, False, "V"),
                 Node(1, 0.5, True, "V")]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[4], True),
                 Edge(nodes[4], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]
        return HyperGraph(
            nodes=nodes,
            edges=edges,
            hyperedges=hyperedges
        )

    @property
    def _right_side(self) -> HyperGraph:
        nodes = [Node(0, 0, False, "V"),
                 Node(0.5, 0, True, "V"),
                 Node(1, 0, False, "V"),
                 Node(0, 0.5, True, "V"),
                 Node(0.5, 0.5, False, "V"),
                 Node(1, 0.5, False, "V"),
                 Node(0, 1, False, "V"),
                 Node(0.5, 1, True, "V"),
                 Node(1, 1, False, "V")]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[3], nodes[4], False),
                 Edge(nodes[4], nodes[5], False),
                 Edge(nodes[6], nodes[7], True),
                 Edge(nodes[7], nodes[8], True),

                 Edge(nodes[0], nodes[3], True),
                 Edge(nodes[3], nodes[6], True),
                 Edge(nodes[1], nodes[4], False),
                 Edge(nodes[4], nodes[7], False),
                 Edge(nodes[2], nodes[5], True),
                 Edge(nodes[5], nodes[8], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[3], nodes[4]], False),
                      HyperEdge([nodes[1], nodes[2], nodes[4], nodes[5]], False),
                      HyperEdge([nodes[3], nodes[4], nodes[6], nodes[7]], False),
                      HyperEdge([nodes[4], nodes[5], nodes[7], nodes[8]], False)]
        return HyperGraph(
            nodes=nodes,
            edges=edges,
            hyperedges=hyperedges
        )

    def apply(self, graph: HyperGraph) -> HyperGraph:
        pass
