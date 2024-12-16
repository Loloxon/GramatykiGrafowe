import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node


class HyperGraph:
    def __init__(
        self, nodes: list[Node], edges: list[Edge], hyperedges: list[HyperEdge]
    ):
        self.nodes = nodes
        self.edges = edges
        self.hyperedges = hyperedges

    def print(self):
        print("Nodes")
        for n in self.nodes:
            print(str(n))
        print()
        print("Edges")
        for n in self.edges:
            print(str(n))
        print()
        print("HyperEdges")
        for n in self.hyperedges:
            print(str(n))
        print()

    def get_edge_between(self, node_1: Node, node_2: Node):
        for edge in self.edges:
            if (edge.node_1 == node_1 and edge.node_2 == node_2) or (
                edge.node_1 == node_2 and edge.node_2 == node_1
            ):
                return edge
        raise Exception(f"There is no edge between [{node_1}] and [{node_2}]")

    def split_edge(self, node_1: Node, node_2: Node, is_hanging: bool = True) -> Node:
        edge_to_split = self.get_edge_between(node_1, node_2)

        new_x = (node_1.x + node_2.x) / 2
        new_y = (node_1.y + node_2.y) / 2
        new_node = Node(x=new_x, y=new_y, is_hanging=is_hanging)
        self.nodes.append(new_node)

        new_edge_1 = Edge(
            node_1=node_1, node_2=new_node, is_border=edge_to_split.is_border
        )
        new_edge_2 = Edge(
            node_1=new_node, node_2=node_2, is_border=edge_to_split.is_border
        )
        self.edges.remove(edge_to_split)
        self.edges.append(new_edge_1)
        self.edges.append(new_edge_2)

        return new_node

    def create_center_node(self, nodes: list[Node]) -> Node:
        new_x = np.average([node.x for node in nodes]).astype(float)
        new_y = np.average([node.y for node in nodes]).astype(float)
        new_node = Node(x=new_x, y=new_y, is_hanging=False)
        self.nodes.append(new_node)

        return new_node

    def add_edges(
        self, central_node: Node, nodes: list[Node], is_border: bool = False
    ) -> None:
        for node in nodes:
            self.add_edge(central_node, node, is_border=is_border)

        return

    def add_edge(self, node_1: Node, node_2: Node, is_border: bool = False) -> None:
        edge = Edge(node_1=node_1, node_2=node_2, is_border=is_border)
        self.edges.append(edge)

        return

    def add_hyperedge(self, nodes: list[Node], is_removable: bool = False) -> None:
        hyperedge = HyperEdge(nodes=nodes, is_removable=is_removable)
        self.hyperedges.append(hyperedge)

        return

    def remove_hyperedge(self, nodes: list[Node]) -> None:
        hyperedges_copy = list(self.hyperedges)

        for hyperedge in self.hyperedges:
            remove_flag = True
            for node in hyperedge.nodes:
                if node not in nodes:
                    remove_flag = False
                    break
            if (len(hyperedge.nodes) == len(nodes)) and remove_flag:
                hyperedges_copy.remove(hyperedge)

        self.hyperedges = hyperedges_copy

    def parse_hypergraph_to_networkx(self) -> nx.Graph:
        G = nx.Graph()

        # Add all nodes to the graph
        for node in self.nodes:
            G.add_node(
                node,
                x=node.x,
                y=node.y,
                is_hanging=node.is_hanging,
                is_production_relevant=node.is_production_relevant,
                label=node.label,
            )

        # Add all edges to the graph
        for edge in self.edges:
            G.add_edge(
                edge.node_1, edge.node_2, is_border=edge.is_border, label=edge.label
            )

        # Add hyperedges to the graph
        for hyperedge in self.hyperedges:
            # Represent the hyperedge as a special node
            hyperedge_node = f"hyperedge_{id(hyperedge)}"
            G.add_node(
                hyperedge_node,
                label=hyperedge.label,
                is_removable=hyperedge.is_removable,
                x=hyperedge.x,
                y=hyperedge.y,
            )

            # Connect the hyperedge node to all its associated nodes
            for node in hyperedge.nodes:
                G.add_edge(hyperedge_node, node)

        return G
