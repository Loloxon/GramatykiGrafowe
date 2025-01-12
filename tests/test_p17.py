from unittest import TestCase

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p17 import P17
from utils import equals, visualize_hypergraph
from tests.test import TestProduction


class TestP17(TestProduction, TestCase):
    def test_apply_exact_graph(self):
        nodes = [
            Node(0, 0, False, is_production_relevant=False),
            Node(1, 0, False, is_production_relevant=False),
            Node(1, 1, False, is_production_relevant=False),
            Node(0, 1, False, is_production_relevant=False),
            Node(1, 0.5, True),
            Node(2, 0.5, False, is_production_relevant=False),
            Node(2, 1, False, is_production_relevant=False),
            Node(0.5, 0, False, is_production_relevant=False),
        ]
        edges = [
            Edge(nodes[2], nodes[4], True),
            Edge(nodes[4], nodes[1], True),
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[7]], False, label="P"
            ),
            HyperEdge([nodes[2], nodes[4], nodes[5], nodes[6]], True, label="Q"),
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes = [
            Node(0.0, 0.0, False, False),
            Node(1.0, 0.0, False, False),
            Node(1.0, 1.0, False, False),
            Node(0.0, 1.0, False, False),
            Node(1.0, 0.5, True, True),
            Node(2.0, 0.5, False, False),
            Node(2.0, 1.0, False, False),
            Node(0.5, 0.0, False, False),
        ]
        edges = [
            Edge(nodes[2], nodes[4], True),
            Edge(nodes[4], nodes[1], True),
        ]
        hyperedges = [
            HyperEdge([nodes[2], nodes[4], nodes[5], nodes[6]], True, "Q"),
            HyperEdge([nodes[0], nodes[7], nodes[1], nodes[2], nodes[3]], True, "P"),
        ]
        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p17 = P17()
        successful, tested_hypergraph_after_p17 = p17.apply(tested_hypergraph)

        self.assertTrue(successful)
        self.assertTrue(equals(tested_hypergraph_after_p17, expected_hypergraph))

    def test_apply_invalid_graph(self):
        nodes = [
            Node(2, 2, False, is_production_relevant=False),
            Node(0.5, 1, False, is_production_relevant=False),
            Node(1, 1, False, is_production_relevant=False),
            Node(0, 1, False, is_production_relevant=False),
            Node(1, 0.5, False),
            Node(2, 0.5, False, is_production_relevant=False),
            Node(2, 1, False, is_production_relevant=False),
            Node(0.5, 0, False, is_production_relevant=False),
        ]
        edges = [
            Edge(nodes[2], nodes[4], True),
            Edge(nodes[4], nodes[1], True),
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[7]], False, label="P"
            ),
            HyperEdge([nodes[2], nodes[4], nodes[5], nodes[6]], True, label="Q"),
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes = [
            Node(0.0, 0.0, False, False),
            Node(1.0, 0.0, False, False),
            Node(1.0, 1.0, False, False),
            Node(0.0, 1.0, False, False),
            Node(1.0, 0.5, True, True),
            Node(2.0, 0.5, False, False),
            Node(2.0, 1.0, False, False),
            Node(0.5, 0.0, False, False),
        ]
        edges = [
            Edge(nodes[2], nodes[4], True),
            Edge(nodes[4], nodes[1], True),
        ]
        hyperedges = [
            HyperEdge([nodes[2], nodes[4], nodes[5], nodes[6]], True, "Q"),
            HyperEdge([nodes[0], nodes[7], nodes[1], nodes[2], nodes[3]], True, "P"),
        ]
        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p17 = P17()
        successful, tested_hypergraph_after_p17 = p17.apply(tested_hypergraph)

        self.assertFalse(successful)
        self.assertFalse(equals(tested_hypergraph_after_p17, expected_hypergraph))

    def test_apply_extended_graph(self):
        nodes = [
            Node(0, 0, False, is_production_relevant=False),
            Node(1, 0, False, is_production_relevant=False),
            Node(1, 1, False, is_production_relevant=False),
            Node(0, 1, False, is_production_relevant=False),
            Node(1, 0.5, True),
            Node(2, 0.5, False, is_production_relevant=False),
            Node(2, 1, False, is_production_relevant=False),
            Node(0.5, 0, False, is_production_relevant=False),
            Node(0.5, 1, False),
        ]
        edges = [
            Edge(nodes[2], nodes[4], True),
            Edge(nodes[4], nodes[1], True),
            Edge(nodes[8], nodes[1], True),
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[7]], False, label="P"
            ),
            HyperEdge([nodes[2], nodes[4], nodes[5], nodes[6]], True, label="Q"),
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes = [
            Node(0.0, 0.0, False, False),
            Node(1.0, 0.0, False, False),
            Node(1.0, 1.0, False, False),
            Node(0.0, 1.0, False, False),
            Node(1.0, 0.5, True, True),
            Node(2.0, 0.5, False, False),
            Node(2.0, 1.0, False, False),
            Node(0.5, 0.0, False, False),
            Node(0.5, 1, False),
        ]
        edges = [
            Edge(nodes[2], nodes[4], True),
            Edge(nodes[4], nodes[1], True),
            Edge(nodes[8], nodes[1], True),
        ]
        hyperedges = [
            HyperEdge([nodes[2], nodes[4], nodes[5], nodes[6]], True, "Q"),
            HyperEdge([nodes[0], nodes[7], nodes[1], nodes[2], nodes[3]], True, "P"),
        ]
        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p17 = P17()
        successful, tested_hypergraph_after_p17 = p17.apply(tested_hypergraph)

        self.assertTrue(successful)
        self.assertTrue(equals(tested_hypergraph_after_p17, expected_hypergraph))

    def test_apply_invalid_graph_missing_node(self):
        nodes = [
            Node(0, 0, False, is_production_relevant=False),
            Node(1, 0, False, is_production_relevant=False),
            Node(1, 1, False, is_production_relevant=False),
            Node(0, 1, False, is_production_relevant=False),
            Node(1, 0.5, True),
            Node(2, 0.5, False, is_production_relevant=False),
            Node(2, 1, False, is_production_relevant=False),
        ]
        edges = [
            Edge(nodes[2], nodes[4], True),
            Edge(nodes[4], nodes[1], True),
        ]
        hyperedges = [
            HyperEdge([nodes[2], nodes[4], nodes[5], nodes[6]], True, label="Q"),
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p17 = P17()
        successful, tested_hypergraph_after_p17 = p17.apply(tested_hypergraph)

        self.assertFalse(successful)

    def test_apply_invalid_graph_missing_edge(self):
        nodes = [
            Node(0, 0, False, is_production_relevant=False),
            Node(1, 0, False, is_production_relevant=False),
            Node(1, 1, False, is_production_relevant=False),
            Node(0, 1, False, is_production_relevant=False),
            Node(1, 0.5, True),
            Node(2, 0.5, False, is_production_relevant=False),
            Node(2, 1, False, is_production_relevant=False),
            Node(0.5, 0, False, is_production_relevant=False),
        ]
        edges = [
            Edge(nodes[2], nodes[4], True),
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[7]], False, label="P"
            ),
            HyperEdge([nodes[2], nodes[4], nodes[5], nodes[6]], True, label="Q"),
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p17 = P17()
        successful, tested_hypergraph_after_p17 = p17.apply(tested_hypergraph)

        self.assertFalse(successful)

    def test_apply_invalid_graph_invalid_label(self):
        nodes = [
            Node(0, 0, False, is_production_relevant=False),
            Node(1, 0, False, is_production_relevant=False),
            Node(1, 1, False, is_production_relevant=False),
            Node(0, 1, False, is_production_relevant=False),
            Node(1, 0.5, True, label="W"),
            Node(2, 0.5, False, is_production_relevant=False),
            Node(2, 1, False, is_production_relevant=False),
            Node(0.5, 0, False, is_production_relevant=False),
        ]
        edges = [
            Edge(nodes[2], nodes[4], True),
            Edge(nodes[4], nodes[1], True),
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[7]], False, label="P"
            ),
            HyperEdge([nodes[2], nodes[4], nodes[5], nodes[6]], True, label="P"),
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        p17 = P17()
        successful, tested_hypergraph_after_p17 = p17.apply(tested_hypergraph)

        self.assertFalse(successful)
