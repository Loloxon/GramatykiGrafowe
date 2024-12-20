from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from productions.production import Production


class P3(Production):
    @property
    def _name(self) -> str:
        return "P3"

    @property
    def _left_side(self) -> HyperGraph:
        nodes = [Node(0, 0, False),
                 Node(1, 0, False),
                 Node(1, 1, False),
                 Node(0, 1, False),
                 Node(1, 0.5, True),
                 Node(0.5, 0, True)]
        edges = [Edge(nodes[0], nodes[5], True),
                 Edge(nodes[5], nodes[1], True),
                 Edge(nodes[1], nodes[4], True),
                 Edge(nodes[4], nodes[2], True),
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
        nodes = [Node(0, 0, False),
                 Node(0.5, 0, False),
                 Node(1, 0, False),
                 Node(0, 0.5, True),
                 Node(0.5, 0.5, False),
                 Node(1, 0.5, False),
                 Node(0, 1, False),
                 Node(0.5, 1, True),
                 Node(1, 1, False)]
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

    def transform(self, graph: HyperGraph, node_map: dict[Node, Node], left_side: HyperGraph) -> (bool, HyperGraph):
        node_1 = node_map[left_side.nodes[5]]
        node_2 = node_map[left_side.nodes[4]]
        node_3 = graph.split_edge(node_map[left_side.nodes[2]],
                                  node_map[left_side.nodes[3]],
                                  graph.get_edge_between(node_map[left_side.nodes[2]],
                                                         node_map[left_side.nodes[3]]).is_border)
        node_4 = graph.split_edge(node_map[left_side.nodes[3]],
                                  node_map[left_side.nodes[0]],
                                  graph.get_edge_between(node_map[left_side.nodes[3]],
                                                         node_map[left_side.nodes[0]]).is_border)

        graph.remove_hyperedge(list(filter(lambda x: not x.is_hanging, list(node_map.values()))))
        node_center = graph.create_center_node(list(filter(lambda x: not x.is_hanging, list(node_map.values()))))

        graph.add_edge(node_1, node_center)
        graph.add_edge(node_2, node_center)
        graph.add_edge(node_3, node_center)
        graph.add_edge(node_4, node_center)

        graph.add_hyperedge([node_1, node_2, node_map[left_side.nodes[1]], node_center])
        graph.add_hyperedge([node_2, node_3, node_map[left_side.nodes[2]], node_center])
        graph.add_hyperedge([node_3, node_4, node_map[left_side.nodes[3]], node_center])
        graph.add_hyperedge([node_4, node_1, node_map[left_side.nodes[0]], node_center])

        node_1.is_hanging = not node_1.is_hanging
        node_2.is_hanging = not node_2.is_hanging

        return True, graph
