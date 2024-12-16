from unittest import TestCase

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p1 import P1
from utils import equals
from tests.test import TestProduction


class TestP1(TestProduction, TestCase):

    def test_apply_exact_graph(self):
        nodes = [
            Node(0, 0, False),
            Node(1, 0, False),
            Node(1, 1, False),
            Node(0, 1, False),
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),
            Edge(nodes[1], nodes[2], True),
            Edge(nodes[2], nodes[3], True),
            Edge(nodes[3], nodes[0], True),
        ]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes = [
            Node(0, 0, False),
            Node(0.5, 0, True),
            Node(1, 0, False),
            Node(0, 0.5, True),
            Node(0.5, 0.5, False),
            Node(1, 0.5, True),
            Node(0, 1, False),
            Node(0.5, 1, True),
            Node(1, 1, False),
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),
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
            Edge(nodes[5], nodes[8], True),
        ]
        hyperedges = [
            HyperEdge([nodes[0], nodes[1], nodes[3], nodes[4]], False),
            HyperEdge([nodes[1], nodes[2], nodes[4], nodes[5]], False),
            HyperEdge([nodes[3], nodes[4], nodes[6], nodes[7]], False),
            HyperEdge([nodes[4], nodes[5], nodes[7], nodes[8]], False),
        ]
        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p1 = P1()
        successful, tested_hypergraph_after_p1 = p1.apply(tested_hypergraph)
        self.assertTrue(successful)
        self.assertTrue(equals(tested_hypergraph_after_p1, expected_hypergraph))

    def test_apply_extended_graph(self):
        nodes = [
            Node(0, 0, False),
            Node(1, 0, False),
            Node(1, 1, False),
            Node(0, 1, False),
            Node(1, 2, False),
            Node(0, 2, False),
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),
            Edge(nodes[1], nodes[2], True),
            Edge(nodes[2], nodes[3], True),
            Edge(nodes[3], nodes[0], True),
            Edge(nodes[2], nodes[4], True),
            Edge(nodes[3], nodes[5], True),
            Edge(nodes[4], nodes[5], True),
        ]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes = [
            Node(0, 0, False),
            Node(0.5, 0, True),
            Node(1, 0, False),
            Node(0, 0.5, True),
            Node(0.5, 0.5, False),
            Node(1, 0.5, True),
            Node(0, 1, False),
            Node(0.5, 1, True),
            Node(1, 1, False),
            Node(1, 2, False),
            Node(0, 2, False),
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),
            Edge(nodes[1], nodes[2], True),
            Edge(nodes[3], nodes[4], False),
            Edge(nodes[4], nodes[5], False),
            Edge(nodes[6], nodes[7], True),
            Edge(nodes[7], nodes[8], True),
            Edge(nodes[8], nodes[9], True),
            Edge(nodes[6], nodes[10], True),
            Edge(nodes[9], nodes[10], True),
            Edge(nodes[0], nodes[3], True),
            Edge(nodes[3], nodes[6], True),
            Edge(nodes[1], nodes[4], False),
            Edge(nodes[4], nodes[7], False),
            Edge(nodes[2], nodes[5], True),
            Edge(nodes[5], nodes[8], True),
        ]
        hyperedges = [
            HyperEdge([nodes[0], nodes[1], nodes[3], nodes[4]], False),
            HyperEdge([nodes[1], nodes[2], nodes[4], nodes[5]], False),
            HyperEdge([nodes[3], nodes[4], nodes[6], nodes[7]], False),
            HyperEdge([nodes[4], nodes[5], nodes[7], nodes[8]], False),
        ]
        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p1 = P1()
        successful, tested_hypergraph_after_p1 = p1.apply(tested_hypergraph)
        self.assertTrue(successful)
        self.assertTrue(equals(tested_hypergraph_after_p1, expected_hypergraph))

    def test_apply_invalid_graph_missing_node(self):
        nodes = [Node(0, 0, False), Node(1, 0, False), Node(1, 1, False)]
        edges = [
            Edge(nodes[0], nodes[1], True),
            Edge(nodes[1], nodes[2], True),
            Edge(nodes[2], nodes[0], True),
            Edge(nodes[2], nodes[0], True),
        ]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2]], True)]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p1 = P1()
        successful, tested_hypergraph_after_p1 = p1.apply(tested_hypergraph)
        self.assertFalse(successful)

    def test_apply_invalid_graph_missing_edge(self):
        nodes = [
            Node(0, 0, False),
            Node(1, 0, False),
            Node(1, 1, False),
            Node(0, 1, False),
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),
            Edge(nodes[1], nodes[2], True),
            Edge(nodes[2], nodes[3], True),
        ]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p1 = P1()
        successful, tested_hypergraph_after_p1 = p1.apply(tested_hypergraph)
        self.assertFalse(successful)

    def test_apply_invalid_graph_invalid_label(self):
        nodes = [
            Node(0, 0, False, label="X"),
            Node(1, 0, False),
            Node(1, 1, False),
            Node(0, 1, False),
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),
            Edge(nodes[1], nodes[2], True),
            Edge(nodes[2], nodes[3], True),
            Edge(nodes[3], nodes[0], True),
        ]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p1 = P1()
        successful, tested_hypergraph_after_p1 = p1.apply(tested_hypergraph)
        self.assertFalse(successful)
