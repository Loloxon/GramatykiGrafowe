from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p1 import P1
from productions.p2 import P2
from productions.p7 import P7
from productions.p8 import P8
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
                         True, True, True, True)

    _, hypergraph_example = p1.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example after P1",
                         True, True, True, True)

    _, hypergraph_example = p2.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example after P1 and P2",
                         True, True, True, True)

    _, hypergraph_example = p2.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example after P1 and 2*P2",
                         False, False, False)

def group_4():
    nodes = [Node(0, 0, False),
             Node(1, 0, False),
             Node(1, 0.5, False),
             Node(1, 1, False),
             Node(0, 1, False),

             Node(0.3, 0.3, False),
             Node(0.7, 0.3, False),
             Node(0.85, 0.5, False),
             Node(0.7, 0.7, False),
             Node(0.3, 0.7, False)]
    edges = [Edge(nodes[0], nodes[1], True),
             Edge(nodes[1], nodes[2], True),
             Edge(nodes[2], nodes[3], True),
             Edge(nodes[3], nodes[4], True),
             Edge(nodes[4], nodes[0], True),

             Edge(nodes[5], nodes[6], False),
             Edge(nodes[6], nodes[7], False),
             Edge(nodes[7], nodes[8], False),
             Edge(nodes[8], nodes[9], False),
             Edge(nodes[9], nodes[5], False),

             Edge(nodes[0], nodes[5], False),
             Edge(nodes[1], nodes[6], False),
             Edge(nodes[2], nodes[7], False),
             Edge(nodes[3], nodes[8], False),
             Edge(nodes[4], nodes[9], False)]
    hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[5], nodes[6]], False),
                  HyperEdge([nodes[1], nodes[2], nodes[6], nodes[7]], False),
                  HyperEdge([nodes[2], nodes[3], nodes[7], nodes[8]], False),
                  HyperEdge([nodes[3], nodes[4], nodes[8], nodes[9]], False),
                  HyperEdge([nodes[4], nodes[0], nodes[9], nodes[5]], False),

                  HyperEdge([nodes[5], nodes[6], nodes[7], nodes[8], nodes[9]], False)]
    hypergraph_example = HyperGraph(nodes, edges, hyperedges)

    p1 = P1()
    p2 = P2()
    p7 = P7()
    p8 = P8()

    _, hypergraph_example = p7.apply_with_predicate(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example", True, True, True, True)
    _, hypergraph_example = p1.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example", True, True, True, True)
    _, hypergraph_example = p7.apply_with_predicate(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example", True, True, True, True)
    _, hypergraph_example = p8.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example", True, True, True, True)
    _, hypergraph_example = p2.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example", True, True, True, True)
    _, hypergraph_example = p1.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example", True, True, True, True)
    _, hypergraph_example = p7.apply_with_predicate(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example", True, True, True, True)
    _, hypergraph_example = p8.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example", True, True, True, True)
    _, hypergraph_example = p2.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example", True, True, True, True)
    _, hypergraph_example = p1.apply(hypergraph_example)
    nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
    visualize_hypergraph(nx_graph_example, "Graph example", True, True, True, True)

if __name__ == "__main__":
    # sample_visualization()
    group_4()
