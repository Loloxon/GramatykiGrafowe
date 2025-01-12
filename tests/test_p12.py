from unittest import TestCase

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p12 import P12
from utils import equals
from tests.test import TestProduction


class TestP12(TestProduction, TestCase):
    def test_apply_exact_graph(self):
        nodes = [
            Node(0, 0, False),
            Node(1, 0, False),
            Node(1, 1, False),
            Node(0, 1, False),
            Node(1.5, 0.5, False),
            Node(0.5, 0, True),
            Node(0.5, 1, True),
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),
            Edge(nodes[5], nodes[1], True),
            Edge(nodes[1], nodes[4], True),
            Edge(nodes[4], nodes[2], True),
            Edge(nodes[2], nodes[6], True),
            Edge(nodes[6], nodes[3], True),
            Edge(nodes[3], nodes[0], True),
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            )
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes = [
            Node(0.0, 0.0, False),
            Node(1.0, 0.0, False),
            Node(1.0, 1.0, False),
            Node(0.0, 1.0, False),
            Node(1.5, 0.5, False),
            Node(0.5, 0.0, False),
            Node(0.5, 1.0, False),
            Node(0.0, 0.5, False),
            Node(1.25, 0.25, False),
            Node(1.25, 0.75, False),
            Node(0.7, 0.5, False),
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),
            Edge(nodes[5], nodes[1], True),
            Edge(nodes[2], nodes[6], True),
            Edge(nodes[6], nodes[3], True),
            Edge(nodes[3], nodes[7], True),
            Edge(nodes[7], nodes[0], True),
            Edge(nodes[1], nodes[8], True),
            Edge(nodes[8], nodes[4], True),
            Edge(nodes[4], nodes[9], True),
            Edge(nodes[9], nodes[2], True),
            Edge(nodes[7], nodes[10], False),
            Edge(nodes[5], nodes[10], False),
            Edge(nodes[6], nodes[10], False),
            Edge(nodes[8], nodes[10], False),
            Edge(nodes[9], nodes[10], False),
        ]
        hyperedges = [
            HyperEdge([nodes[7], nodes[3], nodes[6], nodes[10]], False),
            HyperEdge([nodes[5], nodes[0], nodes[7], nodes[10]], False),
            HyperEdge([nodes[1], nodes[8], nodes[10], nodes[5]], False),
            HyperEdge([nodes[4], nodes[8], nodes[10], nodes[9]], False),
            HyperEdge([nodes[2], nodes[6], nodes[10], nodes[9]], False),
        ]

        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p12 = P12()
        successful, tested_hypergraph_after_p12 = p12.apply(tested_hypergraph)
        self.assertTrue(successful)

        self.assertTrue(equals(tested_hypergraph_after_p12, expected_hypergraph))

    def test_apply_invalid_graph(self):
        nodes = [
            Node(0, 0, False),
            Node(1, 0, False),
            Node(1, 1, False),
            Node(0, 1, False),
            Node(1.5, 0.5, False),
            Node(0.5, 1, True),
            Node(0, 0.5, True),
        ]
        edges = [
            Edge(nodes[2], nodes[5], True),
            Edge(nodes[5], nodes[3], True),
            Edge(nodes[1], nodes[4], True),
            Edge(nodes[4], nodes[2], True),
            Edge(nodes[0], nodes[1], True),
            Edge(nodes[3], nodes[6], True),
            Edge(nodes[6], nodes[0], True),
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            )
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p12 = P12()
        successful, tested_hypergraph_after_p12 = p12.apply(tested_hypergraph)

        self.assertFalse(successful)

    def test_apply_extended_graph(self):
        nodes = [
            Node(0, 0, False),
            Node(1, 0, False),
            Node(1, 1, False),
            Node(0, 1, False),
            Node(1.5, 0.5, False),
            Node(0.5, 0, True),
            Node(0.5, 1, True),
            Node(1.5, 1, True),
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),
            Edge(nodes[5], nodes[1], True),
            Edge(nodes[1], nodes[4], True),
            Edge(nodes[4], nodes[2], True),
            Edge(nodes[2], nodes[6], True),
            Edge(nodes[6], nodes[3], True),
            Edge(nodes[3], nodes[0], True),
            Edge(nodes[7], nodes[5], True),
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            )
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes = [
            Node(0.0, 0.0, False),
            Node(1.0, 0.0, False),
            Node(1.0, 1.0, False),
            Node(0.0, 1.0, False),
            Node(1.5, 0.5, False),
            Node(0.5, 0.0, False),
            Node(0.5, 1.0, False),
            Node(0.0, 0.5, False),
            Node(1.25, 0.25, False),
            Node(1.25, 0.75, False),
            Node(0.7, 0.5, False),
            Node(1.5, 1, True),
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),
            Edge(nodes[5], nodes[1], True),
            Edge(nodes[2], nodes[6], True),
            Edge(nodes[6], nodes[3], True),
            Edge(nodes[3], nodes[7], True),
            Edge(nodes[7], nodes[0], True),
            Edge(nodes[1], nodes[8], True),
            Edge(nodes[8], nodes[4], True),
            Edge(nodes[4], nodes[9], True),
            Edge(nodes[9], nodes[2], True),
            Edge(nodes[7], nodes[10], False),
            Edge(nodes[5], nodes[10], False),
            Edge(nodes[6], nodes[10], False),
            Edge(nodes[8], nodes[10], False),
            Edge(nodes[9], nodes[10], False),
            Edge(nodes[11], nodes[5], True),
        ]
        hyperedges = [
            HyperEdge([nodes[7], nodes[3], nodes[6], nodes[10]], False),
            HyperEdge([nodes[5], nodes[0], nodes[7], nodes[10]], False),
            HyperEdge([nodes[1], nodes[8], nodes[10], nodes[5]], False),
            HyperEdge([nodes[4], nodes[8], nodes[10], nodes[9]], False),
            HyperEdge([nodes[2], nodes[6], nodes[10], nodes[9]], False),
        ]
        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p12 = P12()
        successful, tested_hypergraph_after_p12 = p12.apply(tested_hypergraph)

        self.assertTrue(successful)
        self.assertTrue(equals(tested_hypergraph_after_p12, expected_hypergraph))

    def test_apply_invalid_graph_missing_node(self):
        nodes = [
            Node(0, 0, False),
            Node(1, 0, False),
            Node(1, 1, False),
            Node(0, 1, False),
            Node(1.5, 0.5, False),
            Node(0.5, 0, True),
            Node(0.5, 1, False),
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),
            Edge(nodes[5], nodes[1], True),
            Edge(nodes[1], nodes[4], True),
            Edge(nodes[4], nodes[2], True),
            Edge(nodes[2], nodes[6], True),
            Edge(nodes[6], nodes[3], True),
            Edge(nodes[3], nodes[0], True),
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            )
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p12 = P12()
        successful, tested_hypergraph_after_p12 = p12.apply(tested_hypergraph)

        self.assertFalse(successful)

    def test_apply_invalid_graph_missing_edge(self):
        nodes = [
            Node(0, 0, False),
            Node(1, 0, False),
            Node(1, 1, False),
            Node(0, 1, False),
            Node(1.5, 0.5, False),
            Node(0.5, 0, True),
            Node(0.5, 1, True),
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),
            Edge(nodes[5], nodes[1], True),
            Edge(nodes[1], nodes[4], True),
            Edge(nodes[4], nodes[2], True),
            Edge(nodes[2], nodes[6], True),
            Edge(nodes[6], nodes[3], True),
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            )
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p12 = P12()
        successful, tested_hypergraph_after_p12 = p12.apply(tested_hypergraph)

        self.assertFalse(successful)

    def test_apply_invalid_graph_invalid_label(self):
        nodes = [
            Node(0, 0, False, label="W"),
            Node(1, 0, False),
            Node(1, 1, False),
            Node(0, 1, False),
            Node(1.5, 0.5, False),
            Node(0.5, 0, True),
            Node(0.5, 1, True),
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),
            Edge(nodes[5], nodes[1], True),
            Edge(nodes[1], nodes[4], True),
            Edge(nodes[4], nodes[2], True),
            Edge(nodes[2], nodes[6], True),
            Edge(nodes[6], nodes[3], True),
            Edge(nodes[3], nodes[0], True),
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            )
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p12 = P12()
        successful, tested_hypergraph_after_p12 = p12.apply(tested_hypergraph)

        self.assertFalse(successful)
