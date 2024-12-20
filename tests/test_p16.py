from unittest import TestCase

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p16 import P16
from tests.test import TestProduction
from utils import equals, visualize_hypergraph


class TestP16(TestProduction, TestCase):

    def test_apply_exact_graph(self):
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

        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

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

        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nx_tested_graph = tested_hypergraph.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_tested_graph, "TEST - Graph before P16", True, True, True)

        p16 = P16()
        successful, tested_hypergraph_after_p16 = p16.apply(tested_hypergraph)

        nx_graph_after_production = tested_hypergraph_after_p16.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_after_production, "TEST - Graph after P16", True, True, True)

        self.assertTrue(successful)
        self.assertTrue(equals(tested_hypergraph_after_p16, expected_hypergraph))

    def test_apply_extended_graph(self):
        nodes = [
            Node(0, 0, False, is_production_relevant=False),  # 1
            Node(1, 0, False, is_production_relevant=False),  # 2
            Node(1, 1, False, is_production_relevant=False),  # 3
            Node(0, 1, False, is_production_relevant=False),  # 4
            Node(-0.5, 0.5, False, is_production_relevant=False)  # 5
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),
            Edge(nodes[1], nodes[2], True),
            Edge(nodes[2], nodes[3], True),
            Edge(nodes[3], nodes[4], True),
            Edge(nodes[4], nodes[0], True)
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]],
                False,
                label="P"
            )
        ]

        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes = [
            Node(0, 0, False, is_production_relevant=False),  # 1
            Node(1, 0, False, is_production_relevant=False),  # 2
            Node(1, 1, False, is_production_relevant=False),  # 3
            Node(0, 1, False, is_production_relevant=False),  # 4
            Node(-0.5, 0.5, False, is_production_relevant=False)  # 5
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),
            Edge(nodes[1], nodes[2], True),
            Edge(nodes[2], nodes[3], True),
            Edge(nodes[3], nodes[4], True),
            Edge(nodes[4], nodes[0], True)
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]],
                True,
                label="P"
            )
        ]

        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nx_tested_graph = tested_hypergraph.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_tested_graph, "TEST - Graph before P16", True, True, True)

        p16 = P16()
        successful, tested_hypergraph_after_p16 = p16.apply(tested_hypergraph)

        nx_graph_after_production = tested_hypergraph_after_p16.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_after_production, "TEST - Graph after P16", True, True, True)

        self.assertTrue(successful)
        self.assertTrue(equals(tested_hypergraph_after_p16, expected_hypergraph))

    def test_apply_invalid_graph_missing_node(self):
        nodes = [
            Node(0, 0, False, is_production_relevant=False),  # 1
            Node(1, 1, False, is_production_relevant=False),  # 3
            Node(0, 1, False, is_production_relevant=False),  # 4
            Node(-0.5, 0.5, False, is_production_relevant=False)  # 5
        ]
        edges = []
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3]],
                False,
                label="P"
            )
        ]

        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nx_tested_graph = tested_hypergraph.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_tested_graph, "TEST - Graph before P16", True, True, True)

        p16 = P16()
        successful, tested_hypergraph_after_p16 = p16.apply(tested_hypergraph)

        nx_graph_after_production = tested_hypergraph_after_p16.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_after_production, "TEST - Graph after P16", True, True, True)

        self.assertFalse(successful)

    def test_apply_invalid_graph_missing_edge(self):
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
                [nodes[0], nodes[1], nodes[2], nodes[3]],
                False,
                label="P"
            )
        ]

        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nx_tested_graph = tested_hypergraph.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_tested_graph, "TEST - Graph before P16", True, True, True)

        p16 = P16()
        successful, tested_hypergraph_after_p16 = p16.apply(tested_hypergraph)

        nx_graph_after_production = tested_hypergraph_after_p16.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_after_production, "TEST - Graph after P16", True, True, True)

        self.assertFalse(successful)

    def test_apply_invalid_graph_invalid_label(self):
        nodes = [
            Node(0, 0, False, is_production_relevant=False),  # 1
            Node(1, 0, False, is_production_relevant=False),  # 2
            Node(1, 1, False, is_production_relevant=False, label="D"),  # 3
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

        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nx_tested_graph = tested_hypergraph.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_tested_graph, "TEST - Graph before P16", True, True, True)

        p16 = P16()
        successful, tested_hypergraph_after_p16 = p16.apply(tested_hypergraph)

        nx_graph_after_production = tested_hypergraph_after_p16.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_after_production, "TEST - Graph after P16", True, True, True)

        self.assertFalse(successful)
