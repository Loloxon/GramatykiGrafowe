from unittest import TestCase

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p7 import P7
from utils import equals
from tests.test import TestProduction


class TestP7(TestProduction, TestCase):

    def test_apply_exact_graph(self):
        nodes = [Node(0, 0, False),
                 Node(1, 0, False),
                 Node(1, 1, False),
                 Node(0, 1, False)]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], False)]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes = [Node(0, 0, False),
                 Node(1, 0, False),
                 Node(1, 1, False),
                 Node(0, 1, False)]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]
        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p7 = P7()
        successful, tested_hypergraph_after_p7 = p7.apply(tested_hypergraph)
        self.assertTrue(successful)
        self.assertTrue(equals(tested_hypergraph_after_p7, expected_hypergraph))

    def test_apply_extended_graph(self):
        nodes = [Node(0, 0, False),
                 Node(1, 0, False),
                 Node(1, 1, False),
                 Node(0, 1, False),
                 Node(1, 2, False),
                 Node(0, 2, False)]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True),
                 Edge(nodes[2], nodes[4], True),
                 Edge(nodes[3], nodes[5], True),
                 Edge(nodes[4], nodes[5], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], False)]

        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes = [Node(0, 0, False),
                 Node(1, 0, False),
                 Node(1, 1, False),
                 Node(0, 1, False),
                 Node(1, 2, False),
                 Node(0, 2, False)]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True),
                 Edge(nodes[2], nodes[4], True),
                 Edge(nodes[3], nodes[5], True),
                 Edge(nodes[4], nodes[5], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]
        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p7 = P7()
        successful, tested_hypergraph_after_p7 = p7.apply(tested_hypergraph)
        self.assertTrue(successful)
        self.assertTrue(equals(tested_hypergraph_after_p7, expected_hypergraph))

    def test_apply_invalid_graph_missing_node(self):
        nodes = [Node(0, 0, False),
                 Node(1, 0, False),
                 Node(1, 1, False)]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[0], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2]], False)]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p7 = P7()
        successful, tested_hypergraph_after_p7 = p7.apply(tested_hypergraph)
        self.assertFalse(successful)

    def test_apply_invalid_graph_missing_edge(self):
        nodes = [Node(0, 0, False),
                 Node(1, 0, False),
                 Node(1, 1, False),
                 Node(0, 1, False)]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2]], False)]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p7 = P7()
        successful, tested_hypergraph_after_p7 = p7.apply(tested_hypergraph)
        self.assertFalse(successful)

    def test_apply_invalid_graph_invalid_label(self):
        nodes = [Node(0, 0, False, label="X"),
                 Node(1, 0, False),
                 Node(1, 1, False),
                 Node(0, 1, False)]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], False)]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p7 = P7()
        successful, tested_hypergraph_after_p7 = p7.apply(tested_hypergraph)
        self.assertFalse(successful)
