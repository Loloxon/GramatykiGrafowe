from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p1 import P1


def sample_visualization():
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
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    HyperGraph.visualize_hypergraph(nx_graph_example, "Graph example",
                                    False, False, False)

    p1 = P1()
    p1.visualize()
    hypergraph_example = p1.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    HyperGraph.visualize_hypergraph(nx_graph_example, "Graph example after P1",
                                    False, False, False)


if __name__ == "__main__":
    sample_visualization()
