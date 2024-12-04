from unittest import TestCase

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p1 import P1
from productions.production import Production


class TestP1(TestCase):

    def test_apply_exact_graph(self):
        nodes = [Node(0, 0, False, "V"),
                 Node(1, 0, False, "V"),
                 Node(1, 1, False, "V"),
                 Node(0, 1, False, "V")]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]

        hypergraph_example = HyperGraph(nodes, edges, hyperedges)
        p1 = P1()
        successful, hypergraph_example_after_p1 = p1.apply(hypergraph_example)
        self.assertTrue(successful)
        self.assertTrue(Production.check(hypergraph_example_after_p1, p1.get_right_side()))

    def test_apply_extended_graph(self):
        nodes = [Node(0, 0, False, "V"),
                 Node(1, 0, False, "V"),
                 Node(1, 1, False, "V"),
                 Node(0, 1, False, "V"),
                 Node(1, 2, False, "V"),
                 Node(0, 2, False, "V")]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True),
                 Edge(nodes[2], nodes[4], True),
                 Edge(nodes[3], nodes[5], True),
                 Edge(nodes[4], nodes[5], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]

        hypergraph_example = HyperGraph(nodes, edges, hyperedges)
        p1 = P1()
        successful, hypergraph_example_after_p1 = p1.apply(hypergraph_example)
        self.assertTrue(successful)
        self.assertTrue(Production.check(hypergraph_example_after_p1, p1.get_right_side()))

    def test_apply_invalid_graph(self):
        nodes = [Node(0, 0, False, "V"),
                 Node(1, 0, True, "V"),
                 Node(1, 1, False, "V"),
                 Node(0, 1, False, "V")]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]

        hypergraph_example = HyperGraph(nodes, edges, hyperedges)
        p1 = P1()
        successful, hypergraph_example_after_p1 = p1.apply(hypergraph_example)
        self.assertFalse(successful)
