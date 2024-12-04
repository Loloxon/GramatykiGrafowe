from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.production import Production


class P1(Production):
    @property
    def _name(self) -> str:
        return "P1"

    @property
    def _left_side(self) -> HyperGraph:
        nodes = [Node(0, 0, False, "V"),
                 Node(1, 0, False, "V"),
                 Node(1, 1, False, "V"),
                 Node(0, 1, False, "V")]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[2], nodes[3], True),
                 Edge(nodes[3], nodes[0], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[2], nodes[3]], True)]
        return HyperGraph(
            nodes=nodes,
            edges=edges,
            hyperedges=hyperedges
        )

    @property
    def _right_side(self) -> HyperGraph:
        nodes = [Node(0, 0, False, "V"),
                 Node(0.5, 0, True, "V"),
                 Node(1, 0, False, "V"),
                 Node(0, 0.5, True, "V"),
                 Node(0.5, 0.5, False, "V"),
                 Node(1, 0.5, True, "V"),
                 Node(0, 1, False, "V"),
                 Node(0.5, 1, True, "V"),
                 Node(1, 1, False, "V")]
        edges = [Edge(nodes[0], nodes[1], True),
                 Edge(nodes[1], nodes[2], True),
                 Edge(nodes[3], nodes[4], False),
                 Edge(nodes[4], nodes[5], False),
                 Edge(nodes[6], nodes[7], True),
                 Edge(nodes[7], nodes[8], True),

                 Edge(nodes[0], nodes[3], True),
                 Edge(nodes[3], nodes[6], True),
                 Edge(nodes[1], nodes[4], False),
                 Edge(nodes[4], nodes[7], False),
                 Edge(nodes[2], nodes[5], True),
                 Edge(nodes[5], nodes[8], True)]
        hyperedges = [HyperEdge([nodes[0], nodes[1], nodes[3], nodes[4]], False),
                      HyperEdge([nodes[1], nodes[2], nodes[4], nodes[5]], False),
                      HyperEdge([nodes[3], nodes[4], nodes[6], nodes[7]], False),
                      HyperEdge([nodes[4], nodes[5], nodes[7], nodes[8]], False)]
        return HyperGraph(
            nodes=nodes,
            edges=edges,
            hyperedges=hyperedges
        )

    def apply(self, graph: HyperGraph) -> HyperGraph | None:
        left_side = self.get_left_side()
        node_map = self.check(graph, left_side)

        if node_map:
            reversed_node_map = {v: k for k, v in node_map.items() if isinstance(v, Node) and isinstance(k, Node)}

            node_1 = graph.split_edge_if_exist(reversed_node_map[left_side.nodes[0]], reversed_node_map[left_side.nodes[1]], True)
            node_2 = graph.split_edge_if_exist(reversed_node_map[left_side.nodes[1]], reversed_node_map[left_side.nodes[2]], True)
            node_3 = graph.split_edge_if_exist(reversed_node_map[left_side.nodes[2]], reversed_node_map[left_side.nodes[3]], True)
            node_4 = graph.split_edge_if_exist(reversed_node_map[left_side.nodes[3]], reversed_node_map[left_side.nodes[0]], True)

            graph.remove_hyperedge(list(reversed_node_map.values()))
            node_center = graph.create_center_node(list(map(lambda x: reversed_node_map[x], left_side.nodes)))

            graph.add_edge(node_1, node_center)
            graph.add_edge(node_2, node_center)
            graph.add_edge(node_3, node_center)
            graph.add_edge(node_4, node_center)

            graph.add_hyperedge([node_1, node_2, reversed_node_map[left_side.nodes[1]], node_center])
            graph.add_hyperedge([node_2, node_3, reversed_node_map[left_side.nodes[2]], node_center])
            graph.add_hyperedge([node_3, node_4, reversed_node_map[left_side.nodes[3]], node_center])
            graph.add_hyperedge([node_4, node_1, reversed_node_map[left_side.nodes[0]], node_center])

            return graph
        return None
