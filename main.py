from __future__ import annotations
from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.p1 import P1
from productions.p5 import P5
from productions.p7 import P7
from productions.p8 import P8
from productions.p16 import P16
from productions.p9 import P9
from productions.p2 import P2
from productions.p3 import P3
from tests.test_p1 import TestP1
from utils import visualize_hypergraph


def sample_visualization():
        nodes = [Node(0, 0, False),
                 Node(4, 0, False),
                 Node(4, 4, False),
                 Node(0, 4, False),
                 Node(4, 2, False),
                 Node(1, 1, False),
                 Node(2.5, 1, False),
                 Node(3.5, 2, False),
                 Node(2.5, 3, False),
                 Node(1, 3, False),

                #  Node(2,2,False),
                #  Node(1,2,False),
                #  Node(1.75,1,False),
                #  Node(3,1.5,False),
                #  Node(3,2.5,False),
                #  Node(1.75,3,False),

                 ]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[4], True),
                 Edge(nodes[4], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True),
                 Edge(nodes[0], nodes[5], True),
                 Edge(nodes[6], nodes[1], True),
                 Edge(nodes[7], nodes[4], True),
                 Edge(nodes[8], nodes[2], True),
                 Edge(nodes[9], nodes[3], True),
                 Edge(nodes[5], nodes[6], True),
                 Edge(nodes[6], nodes[7], True),
                 Edge(nodes[7], nodes[8], True),
                 Edge(nodes[8], nodes[9], True),
                 Edge(nodes[9], nodes[5], True),

                #  Edge(nodes[10], nodes[11], True),
                #  Edge(nodes[10], nodes[12], True),
                #  Edge(nodes[10], nodes[13], True),
                #  Edge(nodes[10], nodes[14], True),
                #  Edge(nodes[10], nodes[15], True),


                 ]
        hyperedges = [
                HyperEdge(
                [nodes[5], nodes[6], nodes[7], nodes[8], nodes[9]],
                False,
                label="P"
        ),
        HyperEdge(
                [nodes[2], nodes[4], nodes[7], nodes[8]],
                False),
        HyperEdge(
                [nodes[1], nodes[4], nodes[7], nodes[6]],
                False,)

        ]

        p16 = P16()
        p9 = P9()
        p7 = P7()
        p8 = P8()
        p2 = P2()
        p3 = P3()
        # p5.visualize()
        # p6 = P6()
        # p6.visualize()

        hypergraph_example = HyperGraph(nodes, edges, hyperedges)
        nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_example, "Graph example",
                                        True, True, True)

        _, hypergraph_example = p16.apply(hypergraph_example)
        nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_example, "Graph example after P16",
                                        True, True, True)
        
        _, hypergraph_example = p9.apply(hypergraph_example)
        nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_example, "Graph example after P9",
                                        True, True, True)
        
        _, hypergraph_example = p7.apply(hypergraph_example)
        nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_example, "Graph example after P7",
                                        True, True, True)
        
        _, hypergraph_example = p8.apply(hypergraph_example)
        nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_example, "Graph example after P8",
                                        True, True, True)
        _, hypergraph_example = p8.apply(hypergraph_example)
        nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
        visualize_hypergraph(nx_graph_example, "Graph example after P8",
                                        True, True, True)

        # _, hypergraph_example = p2.apply(hypergraph_example)
        # nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
        # visualize_hypergraph(nx_graph_example, "Graph example after P2",
        #                                 True, True, True)
        
        # _, hypergraph_example = p3.apply(hypergraph_example)
        # nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
        # visualize_hypergraph(nx_graph_example, "Graph example after P3",
        #                                 True, True, True)

#     _, hypergraph_example = p6.apply(hypergraph_example)
#     nx_graph_example = hypergraph_example.parse_hypergraph_to_networkx()
#     visualize_hypergraph(nx_graph_example, "Graph example after P5 and P6",
#                                     True, True, True)



if __name__ == "__main__":
#     x = TestP1()
#     x.test_apply_exact_graph()
#     x.test_apply_extended_graph()
#     x.test_apply_invalid_graph_invalid_label()
#     x.test_apply_invalid_graph_missing_edge()
#     x.test_apply_invalid_graph_missing_node()
        sample_visualization()
