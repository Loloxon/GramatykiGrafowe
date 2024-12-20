from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p1 import P1
from productions.p10 import P10
from productions.p16 import P16
from productions.p2 import P2
from productions.p9 import P9
from utils import visualize_hypergraph


def sample_visualization():
    nodes = [Node(0, 0, False),
             Node(1, 0, False),
             Node(1, 1, False),
             Node(0, 1, False),
             Node(0, 2, False),
             Node(1, 2, False),
             Node(2, 2, False),
             Node(2, 1, False)]
    edges = [Edge(nodes[0], nodes[1], True),
             Edge(nodes[1], nodes[2], True),
             Edge(nodes[2], nodes[3], False),
             Edge(nodes[3], nodes[0], True),
             Edge(nodes[3], nodes[4], True),
             Edge(nodes[4], nodes[5], True),
             Edge(nodes[5], nodes[6], True),
             Edge(nodes[6], nodes[7], True),
             Edge(nodes[7], nodes[2], True),
             Edge(nodes[2], nodes[5], False)]
    hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True),
                  HyperEdge([nodes[2], nodes[3], nodes[4], nodes[5]], True),
                  HyperEdge([nodes[5], nodes[6], nodes[7], nodes[2]], True)]

    p1 = P1()
    p1.visualize()
    p2 = P2()
    p2.visualize()

    hypergraph_example = HyperGraph(nodes, edges, hyperedges)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example",
                         True, True, True)

    _, hypergraph_example = p1.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example after P1",
                         True, True, True)

    _, hypergraph_example = p2.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example after P1 and P2",
                         True, True, True)

    _, hypergraph_example = p2.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example after P1 and 2*P2",
                         False, False, False)


def p9_visualization():
    p9 = P9()
    p9.visualize()

    hypergraph_9 = p9.get_left_side()
    nx_graph_9 = hypergraph_9.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_9, "Graph 9", True, True, True)

    _, hypergraph_9 = p9.apply(hypergraph_9)
    nx_graph_9 = hypergraph_9.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_9, "Graph 9 after P9", True, True, True)

def p10_visualization():
    p10 = P10()
    p10.visualize()

    hypergraph_10 = p10.get_left_side()
    nx_graph_10 = hypergraph_10.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_10, "Graph 10", True, True, True)

    _, hypergraph_10 = p10.apply(hypergraph_10)
    nx_graph_10 = hypergraph_10.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_10, "Graph 10 after P10", True, True, True)

def p16_visualization():
    p16 = P16()
    p16.visualize()

    hypergraph_16 = p16.get_left_side()
    nx_graph_16 = hypergraph_16.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_16, "Graph 16", True, True, True)

    _, hypergraph_16 = p16.apply(hypergraph_16)
    nx_graph_16 = hypergraph_16.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_16, "Graph 16 after P16", True, True, True)


if __name__ == "__main__":
    # sample_visualization()
    p9_visualization()
    p10_visualization()
    p16_visualization()
