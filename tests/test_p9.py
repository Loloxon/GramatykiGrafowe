from unittest import TestCase

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p9 import P9
from tests.test import TestProduction
from utils import equals, visualize_hypergraph


class TestP9(TestProduction, TestCase):

    def test_apply_exact_graph(self):
        nodes = [
            Node(0, 0, False),  # 1
            Node(1, 0, False),  # 2
            Node(1.5, 0.5, False),  # 5
            Node(1, 1, False),  # 3
            Node(0, 1, False)  # 4
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),  # 1-2
            Edge(nodes[1], nodes[2], True),  # 2-5
            Edge(nodes[2], nodes[3], True),  # 5-3
            Edge(nodes[3], nodes[4], True),  # 3-4
            Edge(nodes[4], nodes[0], True)  # 4-1
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]],
                True,
                label="P"
            )
        ]

        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes = [
            Node(0, 0, False),  # 1
            Node(0.5, 0, False),  # 1-v-2
            Node(1, 0, False),  # 2
            Node(1.25, 0.25, False),  # 2-v-5
            Node(1.5, 0.5, False),  # 5
            Node(1.25, 0.75, False),  # 5-v-3
            Node(1, 1, False),  # 3
            Node(0.5, 1, False),  # 3-v-4
            Node(0, 1, False),  # 4
            Node(0, 0.5, False),  # 4-v-1
            Node(0.7, 0.5, False)  # center
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),  # 1-v
            Edge(nodes[1], nodes[2], True),  # v-2
            Edge(nodes[2], nodes[3], True),  # 2-v
            Edge(nodes[3], nodes[4], True),  # v-5
            Edge(nodes[4], nodes[5], True),  # 5-v
            Edge(nodes[5], nodes[6], True),  # v-3
            Edge(nodes[6], nodes[7], True),  # 3-v
            Edge(nodes[7], nodes[8], True),  # v-4
            Edge(nodes[8], nodes[9], True),  # 4-v
            Edge(nodes[9], nodes[0], True),  # v-1
            Edge(nodes[1], nodes[10], True),  # 1-center
            Edge(nodes[3], nodes[10], True),  # 2-center
            Edge(nodes[5], nodes[10], True),  # 5-center
            Edge(nodes[7], nodes[10], True),  # 3-center
            Edge(nodes[9], nodes[10], True),  # 4-center
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[10], nodes[9]], False
            ),
            HyperEdge(
                [nodes[1], nodes[2], nodes[3], nodes[10]], False
            ),
            HyperEdge(
                [nodes[3], nodes[4], nodes[5], nodes[10]], False
            ),
            HyperEdge(
                [nodes[5], nodes[6], nodes[7], nodes[10]], False
            ),
            HyperEdge(
                [nodes[7], nodes[8], nodes[9], nodes[10]], False
            )
        ]

        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nx_tested_graph = tested_hypergraph.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_tested_graph, "TEST - Graph before P9", True, True, True)

        p9 = P9()
        successful, tested_hypergraph_after_p9 = p9.apply(tested_hypergraph)

        nx_graph_after_production = tested_hypergraph_after_p9.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_after_production, "TEST - Graph after P9", True, True, True)

        self.assertTrue(successful)
        self.assertTrue(equals(tested_hypergraph_after_p9, expected_hypergraph))

    def test_apply_extended_graph(self):
        nodes = [
            Node(0, 0, False),  # 1
            Node(1, 0, False),  # 2
            Node(1.5, 0.5, False),  # 5
            Node(1, 1, False),  # 3
            Node(0, 1, False),  # 4
            Node(0, 2, False),
            Node(1, 2, False),
            Node(0.5, 2.5, False)
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),  # 1-2
            Edge(nodes[1], nodes[2], True),  # 2-5
            Edge(nodes[2], nodes[3], True),  # 5-3
            Edge(nodes[3], nodes[4], True),  # 3-4
            Edge(nodes[4], nodes[0], True),  # 4-1
            Edge(nodes[4], nodes[5], True),
            Edge(nodes[3], nodes[6], True),
            Edge(nodes[5], nodes[7], True),
            Edge(nodes[6], nodes[7], True)
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]],
                True,
                label="P"
            )
        ]

        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes = [
            Node(0, 0, False),  # 1
            Node(0.5, 0, False),  # 1-v-2
            Node(1, 0, False),  # 2
            Node(1.25, 0.25, False),  # 2-v-5
            Node(1.5, 0.5, False),  # 5
            Node(1.25, 0.75, False),  # 5-v-3
            Node(1, 1, False),  # 3
            Node(0.5, 1, False),  # 3-v-4
            Node(0, 1, False),  # 4
            Node(0, 0.5, False),  # 4-v-1
            Node(0.7, 0.5, False),  # center
            Node(0, 2, False),
            Node(1, 2, False),
            Node(0.5, 2.5, False)
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),  # 1-v
            Edge(nodes[1], nodes[2], True),  # v-2
            Edge(nodes[2], nodes[3], True),  # 2-v
            Edge(nodes[3], nodes[4], True),  # v-5
            Edge(nodes[4], nodes[5], True),  # 5-v
            Edge(nodes[5], nodes[6], True),  # v-3
            Edge(nodes[6], nodes[7], True),  # 3-v
            Edge(nodes[7], nodes[8], True),  # v-4
            Edge(nodes[8], nodes[9], True),  # 4-v
            Edge(nodes[9], nodes[0], True),  # v-1
            Edge(nodes[1], nodes[10], True),  # 1-center
            Edge(nodes[3], nodes[10], True),  # 2-center
            Edge(nodes[5], nodes[10], True),  # 5-center
            Edge(nodes[7], nodes[10], True),  # 3-center
            Edge(nodes[9], nodes[10], True),  # 4-center
            Edge(nodes[6], nodes[12], True),
            Edge(nodes[8], nodes[11], True),
            Edge(nodes[11], nodes[13], True),
            Edge(nodes[12], nodes[13], True)
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[10], nodes[9]], False
            ),
            HyperEdge(
                [nodes[1], nodes[2], nodes[3], nodes[10]], False
            ),
            HyperEdge(
                [nodes[3], nodes[4], nodes[5], nodes[10]], False
            ),
            HyperEdge(
                [nodes[5], nodes[6], nodes[7], nodes[10]], False
            ),
            HyperEdge(
                [nodes[7], nodes[8], nodes[9], nodes[10]], False
            )
        ]

        expected_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nx_tested_graph = tested_hypergraph.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_tested_graph, "TEST - Graph before P9", True, True, True)

        nx_tested_graph = expected_hypergraph.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_tested_graph, "TEST - Expected graph after P9", True, True, True)

        p9 = P9()
        successful, tested_hypergraph_after_p9 = p9.apply(tested_hypergraph)

        nx_graph_after_production = tested_hypergraph_after_p9.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_after_production, "TEST - Graph after P9", True, True, True)

        self.assertTrue(successful)
        self.assertTrue(equals(tested_hypergraph_after_p9, expected_hypergraph))

    def test_apply_invalid_graph_missing_node(self):
        nodes = [
            Node(0, 0, False),  # 1
            Node(1.5, 0.5, False),  # 5
            Node(1, 1, False),  # 3
            Node(0, 1, False)  # 4
        ]
        edges = [
            Edge(nodes[1], nodes[2], True),  # 5-3
            Edge(nodes[2], nodes[3], True),  # 3-4
            Edge(nodes[3], nodes[0], True),  # 4-1
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3]],
                True,
                label="P"
            )
        ]

        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nx_tested_graph = tested_hypergraph.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_tested_graph, "TEST - Graph before P9", True, True, True)

        p9 = P9()
        successful, tested_hypergraph_after_p9 = p9.apply(tested_hypergraph)
        self.assertFalse(successful)

    def test_apply_invalid_graph_missing_edge(self):
        nodes = [
            Node(0, 0, False),  # 1
            Node(1, 0, False),  # 2
            Node(1.5, 0.5, False),  # 5
            Node(1, 1, False),  # 3
            Node(0, 1, False)  # 4
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),  # 1-2
            Edge(nodes[1], nodes[2], True),  # 2-5
            Edge(nodes[2], nodes[3], True),  # 5-3
            Edge(nodes[3], nodes[4], True),  # 3-4
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]],
                True,
                label="P"
            )
        ]

        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nx_tested_graph = tested_hypergraph.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_tested_graph, "TEST - Graph before P9", True, True, True)

        p9 = P9()
        successful, tested_hypergraph_after_p9 = p9.apply(tested_hypergraph)
        self.assertFalse(successful)

    def test_apply_invalid_graph_invalid_label(self):
        nodes = [
            Node(0, 0, False, label="D"),  # 1
            Node(1, 0, False),  # 2
            Node(1.5, 0.5, False),  # 5
            Node(1, 1, False),  # 3
            Node(0, 1, False)  # 4
        ]
        edges = [
            Edge(nodes[0], nodes[1], True),  # 1-2
            Edge(nodes[1], nodes[2], True),  # 2-5
            Edge(nodes[2], nodes[3], True),  # 5-3
            Edge(nodes[3], nodes[4], True),  # 3-4
            Edge(nodes[4], nodes[0], True)  # 4-1
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]],
                True,
                label="P"
            )
        ]

        tested_hypergraph = HyperGraph(nodes, edges, hyperedges)

        nx_tested_graph = tested_hypergraph.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_tested_graph, "TEST - Graph before P9", True, True, True)

        p9 = P9()
        successful, tested_hypergraph_after_p9 = p9.apply(tested_hypergraph)
        self.assertFalse(successful)
