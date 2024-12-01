import networkx as nx

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph

nodes = [Node(0, 0, False, "A"),
         Node(0, 1, False, "B"),
         Node(1, 1, False, "C"),
         Node(1, 0, False, "D")]
edges = [Edge(nodes[0], nodes[1], True),
         Edge(nodes[1], nodes[2], True),
         Edge(nodes[2], nodes[3], True),
         Edge(nodes[3], nodes[0], True)]
hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]

hypergraph = HyperGraph(nodes, edges, hyperedges)
nx_graph = hypergraph.parse_hypergraph_to_networkx()

hypergraph.visualize_hypergraph(nx_graph)