from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p1 import P1
from productions.p2 import P2
from utils import visualize_hypergraph


def sample_visualization():
    nodes = [
        Node(0, 0, False),
        Node(1, 0, False),
        Node(1, 1, False),
        Node(0, 1, False),
        Node(0, 2, False),
        Node(1, 2, False),
        Node(2, 2, False),
        Node(2, 1, False),
    ]
    edges = [
        Edge(nodes[0], nodes[1], True),
        Edge(nodes[1], nodes[2], True),
        Edge(nodes[2], nodes[3], True),
        Edge(nodes[3], nodes[0], True),
        Edge(nodes[3], nodes[4], True),
        Edge(nodes[4], nodes[5], True),
        Edge(nodes[5], nodes[6], True),
        Edge(nodes[6], nodes[7], True),
        Edge(nodes[7], nodes[2], True),
        Edge(nodes[2], nodes[5], True),
    ]
    hyperedges = [
        HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True),
        HyperEdge([nodes[2], nodes[3], nodes[4], nodes[5]], True),
        HyperEdge([nodes[5], nodes[6], nodes[7], nodes[2]], True),
    ]

    p1 = P1()
    p1.visualize()
    p2 = P2()
    p2.visualize()

    hypergraph_example = HyperGraph(nodes, edges, hyperedges)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example", True, True, True)

    _, hypergraph_example = p1.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example after P1", True, True, True)

    _, hypergraph_example = p2.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(
        nx_graph_example, "Graph example after P1 and P2", True, True, True
    )

    _, hypergraph_example = p2.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(
        nx_graph_example, "Graph example after P1 and 2*P2", True, True, True
    )


if __name__ == "__main__":
    sample_visualization()
