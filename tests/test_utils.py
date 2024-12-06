from unittest import TestCase

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from utils import check, _find_subgraphs


class TestUtils(TestCase):
    def test_find_subgraphs(self):
        nodes = [Node(0, 0, False, label="A"),
                 Node(0, 1, False, label="B"),
                 Node(1, 1, False, label="C"),
                 Node(1, 0, False, label="D")]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]

        hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes2 = [Node(0, 0, False, label="A"),
                  Node(0, 1, False, label="B"),
                  Node(1, 1, False, label="C"),
                  Node(1, 0, False, label="D")]
        edges2 = [Edge(nodes2[0], nodes2[1], True),
                  Edge(nodes2[1], nodes2[2], True),
                  Edge(nodes2[2], nodes2[3], True),
                  Edge(nodes2[3], nodes2[0], True)]
        hyperedges2 = [HyperEdge([nodes2[0], nodes2[1], nodes2[2], nodes2[3]], True)]

        hypergraph2 = HyperGraph(nodes2, edges2, hyperedges2)

        result = _find_subgraphs(hypergraph, hypergraph2)
        self.assertTrue(result)
        self.assertEqual(1, len(result))

    def test_find_subgraphs(self):
        nodes = [Node(0, 0, False),
                 Node(0, 1, False),
                 Node(1, 1, False),
                 Node(1, 0, False, )]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]

        hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes2 = [Node(0, 0, False),
                  Node(0, 1, False),
                  Node(1, 1, False),
                  Node(1, 0, False)]
        edges2 = [Edge(nodes2[0], nodes2[1], True),
                  Edge(nodes2[1], nodes2[2], True),
                  Edge(nodes2[2], nodes2[3], True),
                  Edge(nodes2[3], nodes2[0], True)]
        hyperedges2 = [HyperEdge([nodes2[0], nodes2[1], nodes2[2], nodes2[3]], True)]

        hypergraph2 = HyperGraph(nodes2, edges2, hyperedges2)

        result = _find_subgraphs(hypergraph, hypergraph2)
        self.assertTrue(result)
        self.assertEqual(8, len(result))

    def test_check_fail(self):
        nodes = [Node(0, 0, False, label="A"),
                 Node(0, 1, False, label="B"),
                 Node(1, 1, False, label="C"),
                 Node(1, 0, False, label="D")]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]

        hypergraph = HyperGraph(nodes, edges, hyperedges)

        nodes2 = [Node(0, 0, False, label="X"),
                  Node(0, 1, False, label="B"),
                  Node(1, 1, False, label="C"),
                  Node(1, 0, False, label="D")]
        edges2 = [Edge(nodes2[0], nodes2[1], True),
                  Edge(nodes2[1], nodes2[2], True),
                  Edge(nodes2[2], nodes2[3], True),
                  Edge(nodes2[3], nodes2[0], True)]
        hyperedges2 = [HyperEdge([nodes2[0], nodes2[1], nodes2[2], nodes2[3]], True)]

        hypergraph2 = HyperGraph(nodes2, edges2, hyperedges2)

        result = check(hypergraph, hypergraph2)
        self.assertFalse(result)
