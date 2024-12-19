from unittest import TestCase

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p13 import P13
from utils import equals
from tests.test import TestProduction


class TestP13(TestProduction, TestCase):
    def test_apply_exact_graph(self):
        p13 = P13()
        tested_hypergraph = p13._left_side
        expected_hypergraph = p13._right_side
        successful, tested_hypergraph_after_p13 = p13.apply(tested_hypergraph)
        self.assertTrue(successful)
        self.assertTrue(equals(tested_hypergraph_after_p13, expected_hypergraph))

    def test_apply_extended_graph(self):
        nodes = [
            Node(0, 0, False),  # 1
            Node(1, 0, False),  # 2
            Node(1, 1, False),  # 3
            Node(0, 1, False),  # 4
            Node(1.5, 0.5, False),  # 5
            Node(0.5, 0, True),  # 6
            Node(0, 0.5, True),  # 7
            Node(0.5, 1, True),  # 8
            Node(-1, 1, False),  # 9
            Node(-1, 0.5, False),  # 10
            Node(-1, 0, False),  # 11
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),  # 1 - 6
            Edge(nodes[5], nodes[1], True),  # 6 - 2
            Edge(nodes[1], nodes[4], True),  # 2 - 5
            Edge(nodes[4], nodes[2], True),  # 5 - 3
            Edge(nodes[2], nodes[7], True),  # 3 - 8
            Edge(nodes[7], nodes[3], True),  # 8 - 4
            Edge(nodes[3], nodes[6], False),  # 4 - 7
            Edge(nodes[6], nodes[0], False),  # 7 - 1
            Edge(nodes[3], nodes[8], True),  # 4 - 9
            Edge(nodes[8], nodes[9], True),  # 9 - 10
            Edge(nodes[9], nodes[6], False),  # 10 - 7
            Edge(nodes[9], nodes[10], True),  # 10 - 11
            Edge(nodes[10], nodes[0], True),  # 11 - 1
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            ),
            HyperEdge(
                [nodes[6], nodes[3], nodes[8], nodes[9]], True, label="Q"
            ),
            HyperEdge(
                [nodes[9], nodes[10], nodes[0], nodes[6]], True, label="Q"
            ),
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)
        successful, tested_hypergraph_after_p13 = P13().apply(tested_hypergraph)
        self.assertTrue(successful)

        nodes = [
            Node(0, 0, False),  # 1
            Node(1, 0, False),  # 2
            Node(1, 1, False),  # 3
            Node(0, 1, False),  # 4
            Node(1.5, 0.5, False),  # 5
            Node(0.5, 0, False),  # 6
            Node(0, 0.5, False),  # 7
            Node(0.5, 1, False),  # 8

            Node(1.25, 0.75, False),  # 9
            Node(1.25, 0.25, False),  # 10
            Node(0.7, 0.5, False),  # 11

            Node(-1, 1, False),  # 12
            Node(-1, 0.5, False),  # 13
            Node(-1, 0, False),  # 14
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),  # 1 - 6
            Edge(nodes[5], nodes[1], True),  # 6 - 2
            Edge(nodes[1], nodes[9], True),  # 2 - 10
            Edge(nodes[9], nodes[4], True),  # 10 - 5
            Edge(nodes[4], nodes[8], True),  # 5 - 9
            Edge(nodes[8], nodes[2], True),  # 9 - 3
            Edge(nodes[2], nodes[7], True),  # 3 - 8
            Edge(nodes[7], nodes[3], True),  # 8 - 4
            Edge(nodes[3], nodes[6], True),  # 4 - 7
            Edge(nodes[6], nodes[0], True),  # 7 - 1

            Edge(nodes[5], nodes[10], False),  # 6 - 11
            Edge(nodes[6], nodes[10], False),  # 7 - 11
            Edge(nodes[7], nodes[10], False),  # 8 - 11
            Edge(nodes[8], nodes[10], False),  # 9 - 11
            Edge(nodes[9], nodes[10], False),  # 10 - 11

            Edge(nodes[3], nodes[11], True),  # 4 - 12
            Edge(nodes[11], nodes[12], True),  # 12 - 13
            Edge(nodes[12], nodes[6], False),  # 13 - 7
            Edge(nodes[12], nodes[13], True),  # 13 - 14
            Edge(nodes[13], nodes[0], True),  # 14 - 1
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[5], nodes[10], nodes[6]], False, label="Q",
            ),
            HyperEdge(
                [nodes[5], nodes[1], nodes[9], nodes[10]], False, label="Q",
            ),
            HyperEdge(
                [nodes[9], nodes[4], nodes[8], nodes[10]], False, label="Q",
            ),
            HyperEdge(
                [nodes[8], nodes[2], nodes[7], nodes[10]], False, label="Q",
            ),
            HyperEdge(
                [nodes[7], nodes[3], nodes[6], nodes[10]], False, label="Q",
            ),

            HyperEdge(
                [nodes[6], nodes[3], nodes[11], nodes[12]], True, label="Q"
            ),
            HyperEdge(
                [nodes[12], nodes[13], nodes[0], nodes[6]], True, label="Q"
            ),
        ]
        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)
        self.assertTrue(equals(tested_hypergraph_after_p13, expected_hypergraph))

    def test_apply_invalid_graph_missing_node(self):
        nodes = [
            Node(0, 0, False),  # 1
            Node(1, 0, False),  # 2
            Node(1, 1, False),  # 3
            Node(0, 1, False),  # 4
            Node(1.5, 0.5, False),  # 5
            Node(0.5, 0, True),  # 6
            Node(0, 0.5, True),  # 7
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),  # 1 - 6
            Edge(nodes[5], nodes[1], True),  # 6 - 2
            Edge(nodes[1], nodes[4], True),  # 2 - 5
            Edge(nodes[4], nodes[2], True),  # 5 - 3
            Edge(nodes[2], nodes[3], True),  # 3 - 4
            Edge(nodes[3], nodes[6], True),  # 4 - 7
            Edge(nodes[6], nodes[0], True),  # 7 - 1
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            )
        ]

        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)
        successful, _ = P13().apply(tested_hypergraph)
        self.assertFalse(successful)

    def test_apply_invalid_graph_missing_edge(self):
        nodes = [
            Node(0, 0, False),  # 1
            Node(1, 0, False),  # 2
            Node(1, 1, False),  # 3
            Node(0, 1, False),  # 4
            Node(1.5, 0.5, False),  # 5
            Node(0.5, 0, True),  # 6
            Node(0, 0.5, True),  # 7
            Node(0.5, 1, True),  # 8
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),  # 1 - 6
            Edge(nodes[5], nodes[1], True),  # 6 - 2
            Edge(nodes[1], nodes[4], True),  # 2 - 5
            Edge(nodes[4], nodes[2], True),  # 5 - 3
            Edge(nodes[2], nodes[7], True),  # 3 - 8
            Edge(nodes[7], nodes[3], True),  # 8 - 4
            Edge(nodes[3], nodes[6], True),  # 4 - 7
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            )
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)
        successful, _ = P13().apply(tested_hypergraph)
        self.assertFalse(successful)

        nodes = [
            Node(0, 0, False),  # 1
            Node(1, 0, False),  # 2
            Node(1, 1, False),  # 3
            Node(0, 1, False),  # 4
            Node(1.5, 0.5, False),  # 5
            Node(0.5, 0, True),  # 6
            Node(0, 0.5, True),  # 7
            Node(0.5, 1, True),  # 8
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),  # 1 - 6
            Edge(nodes[5], nodes[1], True),  # 6 - 2
            Edge(nodes[1], nodes[4], True),  # 2 - 5
            Edge(nodes[2], nodes[7], True),  # 3 - 8
            Edge(nodes[7], nodes[3], True),  # 8 - 4
            Edge(nodes[3], nodes[6], True),  # 4 - 7
            Edge(nodes[6], nodes[0], True),  # 7 - 1
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            )
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)
        successful, _ = P13().apply(tested_hypergraph)
        self.assertFalse(successful)

        nodes = [
            Node(0, 0, False),  # 1
            Node(1, 0, False),  # 2
            Node(1, 1, False),  # 3
            Node(0, 1, False),  # 4
            Node(1.5, 0.5, False),  # 5
            Node(0.5, 0, True),  # 6
            Node(0, 0.5, True),  # 7
            Node(0.5, 1, True),  # 8
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),  # 1 - 6
            Edge(nodes[1], nodes[4], True),  # 2 - 5
            Edge(nodes[4], nodes[2], True),  # 5 - 3
            Edge(nodes[2], nodes[7], True),  # 3 - 8
            Edge(nodes[7], nodes[3], True),  # 8 - 4
            Edge(nodes[3], nodes[6], True),  # 4 - 7
            Edge(nodes[6], nodes[0], True),  # 7 - 1
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            )
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)
        successful, _ = P13().apply(tested_hypergraph)
        self.assertFalse(successful)

    def test_apply_invalid_graph_invalid_label(self):
        nodes = [
            Node(0, 0, False),  # 1
            Node(1, 0, False),  # 2
            Node(1, 1, False),  # 3
            Node(0, 1, False),  # 4
            Node(1.5, 0.5, False),  # 5
            Node(0.5, 0, True),  # 6
            Node(0, 0.5, True),  # 7
            Node(0.5, 1, True, label='A'),  # 8
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),  # 1 - 6
            Edge(nodes[5], nodes[1], True),  # 6 - 2
            Edge(nodes[1], nodes[4], True),  # 2 - 5
            Edge(nodes[4], nodes[2], True),  # 5 - 3
            Edge(nodes[2], nodes[7], True),  # 3 - 8
            Edge(nodes[7], nodes[3], True),  # 8 - 4
            Edge(nodes[3], nodes[6], True),  # 4 - 7
            Edge(nodes[6], nodes[0], True),  # 7 - 1
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            )
        ]
        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)
        successful, _ = P13().apply(tested_hypergraph)
        self.assertFalse(successful)
