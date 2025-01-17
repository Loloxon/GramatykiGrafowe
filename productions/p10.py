from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.production import Production


class P10(Production):
    @property
    def _name(self) -> str:
        return "P10"

    @property
    def _left_side(self) -> HyperGraph:
        nodes = [
            Node(0, 0, False),  # 1
            Node(1, 0, False),  # 2
            Node(1.5, 0.5, False),  # 5
            Node(1, 1, False),  # 3
            Node(0, 1, False),  # 4
            Node(0.5, 0, True)  # 6 - hanging node
        ]
        edges = [
            Edge(nodes[0], nodes[5], True),  # 1-6
            Edge(nodes[5], nodes[1], True),  # 6-2
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
        return HyperGraph(
            nodes=nodes,
            edges=edges,
            hyperedges=hyperedges
        )

    @property
    def _right_side(self) -> HyperGraph:
        nodes = [
            Node(0, 0, False),  # 1
            Node(0.5, 0, False),  # 6 - old hanging
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
            Edge(nodes[0], nodes[1], True),  # 1-6
            Edge(nodes[1], nodes[2], True),  # 6-2
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
        return HyperGraph(
            nodes=nodes,
            edges=edges,
            hyperedges=hyperedges
        )

    def transform(self, graph: HyperGraph, node_map: dict[Node, Node], left_side: HyperGraph) -> (bool, HyperGraph):
        node_1 = node_map[left_side.nodes[5]]

        node_2 = graph.split_edge(
            node_map[left_side.nodes[1]],
            node_map[left_side.nodes[2]],
            not graph.get_edge_between(node_map[left_side.nodes[1]], node_map[left_side.nodes[2]]).is_border
        )

        node_3 = graph.split_edge(
            node_map[left_side.nodes[2]],
            node_map[left_side.nodes[3]],
            not graph.get_edge_between(node_map[left_side.nodes[2]], node_map[left_side.nodes[3]]).is_border
        )

        node_4 = graph.split_edge(
            node_map[left_side.nodes[3]],
            node_map[left_side.nodes[4]],
            not graph.get_edge_between(node_map[left_side.nodes[3]], node_map[left_side.nodes[4]]).is_border
        )

        node_5 = graph.split_edge(
            node_map[left_side.nodes[4]],
            node_map[left_side.nodes[0]],
            not graph.get_edge_between(node_map[left_side.nodes[4]], node_map[left_side.nodes[0]]).is_border
        )

        graph.remove_hyperedge(list(filter(lambda x: not x.is_hanging, list(node_map.values()))))
        node_center = graph.create_center_node(list(filter(lambda x: not x.is_hanging, list(node_map.values()))))

        graph.add_edge(node_1, node_center)
        graph.add_edge(node_2, node_center)
        graph.add_edge(node_3, node_center)
        graph.add_edge(node_4, node_center)
        graph.add_edge(node_5, node_center)

        graph.add_hyperedge([node_1, node_5, node_map[left_side.nodes[0]], node_center], False)
        graph.add_hyperedge([node_1, node_2, node_map[left_side.nodes[1]], node_center], False)
        graph.add_hyperedge([node_2, node_3, node_map[left_side.nodes[2]], node_center], False)
        graph.add_hyperedge([node_3, node_4, node_map[left_side.nodes[3]], node_center], False)
        graph.add_hyperedge([node_4, node_5, node_map[left_side.nodes[4]], node_center], False)

        node_1.is_hanging = not node_1.is_hanging

        return True, graph