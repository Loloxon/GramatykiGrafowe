from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.production import Production


class P13(Production):
    @property
    def _name(self) -> str:
        return "P13"

    @property
    def _left_side(self) -> HyperGraph:
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
            Edge(nodes[6], nodes[0], True),  # 7 - 1
        ]
        hyperedges = [
            HyperEdge(
                [nodes[0], nodes[1], nodes[4], nodes[2], nodes[3]], True, label="P"
            )
        ]
        return HyperGraph(nodes=nodes, edges=edges, hyperedges=hyperedges)

    @property
    def _right_side(self) -> HyperGraph:
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
            )
        ]
        return HyperGraph(nodes=nodes, edges=edges, hyperedges=hyperedges)

    def transform(
        self, graph: HyperGraph, node_map: dict[Node, Node], left_side: HyperGraph
    ) -> (bool, HyperGraph):
        node_mapper = lambda i: node_map[left_side.nodes[i - 1]]

        node_5_3 = graph.split_edge(
            node_mapper(5),
            node_mapper(3),
            not graph.get_edge_between(node_mapper(5), node_mapper(3)).is_border,
        )
        node_2_5 = graph.split_edge(
            node_mapper(2),
            node_mapper(5),
            not graph.get_edge_between(node_mapper(2), node_mapper(5)).is_border,
        )

        graph.remove_hyperedge([node_mapper(i) for i in [1, 2, 5, 3, 4]])

        node_center = graph.create_center_node(
            [node_mapper(6), node_2_5, node_5_3, node_mapper(8), node_mapper(7)]
        )

        graph.add_edge(node_mapper(6), node_center)
        graph.add_edge(node_2_5, node_center)
        graph.add_edge(node_5_3, node_center)
        graph.add_edge(node_mapper(8), node_center)
        graph.add_edge(node_mapper(7), node_center)

        graph.add_hyperedge([
            node_mapper(1), node_mapper(6), node_center, node_mapper(7)
        ])
        graph.add_hyperedge([
            node_mapper(6), node_mapper(2), node_2_5, node_center
        ])
        graph.add_hyperedge([
            node_2_5, node_mapper(5), node_5_3, node_center
        ])
        graph.add_hyperedge([
            node_5_3, node_mapper(3), node_mapper(8), node_center
        ])
        graph.add_hyperedge([
            node_mapper(8), node_mapper(4), node_mapper(7), node_center
        ])

        node_mapper(6).is_hanging = False
        node_mapper(7).is_hanging = False
        node_mapper(8).is_hanging = False

        return True, graph
