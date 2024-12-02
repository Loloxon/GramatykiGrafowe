import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node


class HyperGraph:
    def __init__(self, nodes: list[Node], edges: list[Edge], hyperedges: list[HyperEdge]):
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

    def split_edge(self, edge: Edge) -> Node:
        node_1 = edge.node_1
        node_2 = edge.node_2
        new_x = (node_1.x + node_2.x) / 2
        new_y = (node_1.y + node_2.y) / 2
        new_node = Node(x=new_x, y=new_y, is_hanging=True)
        self.nodes.append(new_node)

        new_edge_1 = Edge(node_1=node_1, node_2=new_node, is_border=edge.is_border)
        new_edge_2 = Edge(node_1=new_node, node_2=node_2, is_border=edge.is_border)
        self.edges.remove(edge)
        self.edges.append(new_edge_1)
        self.edges.append(new_edge_2)

        return new_node

    def create_center_node(self, nodes: list[Node]) -> Node:
        new_x = np.average([node.x for node in nodes]).astype(float)
        new_y = np.average([node.y for node in nodes]).astype(float)
        new_node = Node(x=new_x, y=new_y, is_hanging=False)
        self.nodes.append(new_node)

        return new_node

    def create_edges(self, central_node: Node, nodes: list[Node], is_border: bool = False) -> None:
        for node in nodes:
            edge = Edge(node_1=central_node, node_2=node, is_border=is_border)
            self.edges.append(edge)

        return

    def parse_hypergraph_to_networkx(self) -> nx.Graph:
        G = nx.Graph()

        # Add all nodes to the graph
        for node in self.nodes:
            G.add_node(
                node,
                x=node.x,
                y=node.y,
                is_hanging=node.is_hanging,
                label=node.label
            )

        # Add all edges to the graph
        for edge in self.edges:
            G.add_edge(
                edge.node_1,
                edge.node_2,
                is_border=edge.is_border,
                label=edge.label
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
                y=hyperedge.y
            )

            # Connect the hyperedge node to all its associated nodes
            for node in hyperedge.nodes:
                G.add_edge(
                    hyperedge_node,
                    node
                )

        return G

    @staticmethod
    def parse_networkx_to_hypergraph(nx_graph: nx.Graph) -> 'HyperGraph':
        nodes = []
        edges = []
        hyperedges = []

        # Create nodes
        for node, data in nx_graph.nodes(data=True):
            if isinstance(node, str) and node.startswith("hyperedge_"):
                # This is a hyperedge node
                continue

            # Regular node
            x = data.get('x', 0)
            y = data.get('y', 0)
            is_hanging = data.get('is_hanging', False)
            label = data.get('label', 'V')
            nodes.append(Node(x, y, is_hanging, label))

        # Create edges
        for node1, node2, data in nx_graph.edges(data=True):
            if isinstance(node1, str) and node1.startswith("hyperedge_"):
                # Skip hyperedge nodes (they are not part of regular edges)
                continue

            is_border = data.get('is_border', False)
            label = data.get('label', 'E')
            # Find corresponding nodes in the nodes list
            node1_obj = next(
                node for node in nodes if node.x == nx_graph.nodes[node1]['x'] and node.y == nx_graph.nodes[node1]['y'])
            node2_obj = next(
                node for node in nodes if node.x == nx_graph.nodes[node2]['x'] and node.y == nx_graph.nodes[node2]['y'])
            edges.append(Edge(node1_obj, node2_obj, is_border, label))

        # Create hyperedges
        for node, data in nx_graph.nodes(data=True):
            if isinstance(node, str) and node.startswith("hyperedge_"):
                # This is a hyperedge node, reconstruct the hyperedge
                label = data.get('label', 'Q')
                is_removable = data.get('is_removable', False)

                hyperedge_nodes = []
                for neighbor in nx_graph.neighbors(node):
                    if not isinstance(neighbor, str):  # Regular node (not a hyperedge node)
                        neighbor_obj = next(
                            n for n in nodes if
                            n.x == nx_graph.nodes[neighbor]['x'] and n.y == nx_graph.nodes[neighbor]['y'])
                        hyperedge_nodes.append(neighbor_obj)

                hyperedges.append(HyperEdge(hyperedge_nodes, is_removable, label))

        return HyperGraph(nodes, edges, hyperedges)

    @staticmethod
    def visualize_hypergraph(graph: nx.Graph, title: str):
        """
        Visualizes a hypergraph based on their attributes.

        1. **Nodes**:
            - **Hanging Nodes** (`is_hanging=True`) doesn't have border
            - **Non-Hanging Nodes** (`is_hanging=False`) have border

        2. **Hyperedges**:
            - **Removable Hyperedges** (`is_removable=True`) doesn't have border
            - **Non-Removable Hyperedges** (`is_removable=False`) have border

        3. **Edges**:
            - **Border Edges** (`is_border=True`) has solid black line
            - **Non-Border Edges** (`is_border=False`) has dotted black line
            - **Inside Edges** (No `is_border` attribute - edges for hyperedges): has solid grey line
        """

        # Separate regular nodes and hyperedges
        pos = {node: (graph.nodes[node]['x'], graph.nodes[node]['y']) for node in graph.nodes if
               'x' in graph.nodes[node] and 'y' in graph.nodes[node]}

        labels = nx.get_node_attributes(graph, 'label')

        # Separate regular nodes and hyperedges
        regular_nodes = [node for node in graph.nodes if not str(node).startswith("hyperedge_")]
        hyperedge_nodes = [node for node in graph.nodes if str(node).startswith("hyperedge_")]

        # Further separate regular nodes into hanging and non-hanging
        regular_nodes_hanging = [node for node in regular_nodes if graph.nodes[node].get('is_hanging')]
        regular_nodes_not_hanging = [node for node in regular_nodes if not graph.nodes[node].get('is_hanging')]

        hyperedge_nodes_removable = [node for node in hyperedge_nodes if graph.nodes[node].get('is_removable')]
        hyperedge_nodes_not_removable = [node for node in hyperedge_nodes if not graph.nodes[node].get('is_removable')]

        # Draw hanging nodes without borders
        nx.draw_networkx_nodes(
            graph,
            pos,
            nodelist=regular_nodes_hanging,
            node_color='lightblue',
            edgecolors='none',  # No border
            node_size=400,
            label="Hanging Nodes"
        )

        # Draw non-hanging nodes with borders
        nx.draw_networkx_nodes(
            graph,
            pos,
            nodelist=regular_nodes_not_hanging,
            node_color='lightblue',
            edgecolors='black',
            linewidths=2,
            node_size=400,
            label="Non-Hanging Nodes"
        )

        # Draw removable hyperedges without borders
        nx.draw_networkx_nodes(
            graph,
            pos,
            nodelist=hyperedge_nodes_removable,
            node_color='pink',
            node_shape='s',
            node_size=400,
            label="Hyperedges"
        )

        # Draw non-removable hyperedges with borders
        nx.draw_networkx_nodes(
            graph,
            pos,
            nodelist=hyperedge_nodes_not_removable,
            node_color='pink',
            edgecolors='black',
            linewidths=2,
            node_shape='s',
            node_size=400,
            label="Hyperedges"
        )

        # Draw edges
        border_edges = [(u, v) for u, v in graph.edges if
                        'is_border' in graph.edges[u, v] and graph.edges[u, v].get('is_border')]
        non_border_edges = [(u, v) for u, v in graph.edges if
                            'is_border' in graph.edges[u, v] and not graph.edges[u, v].get('is_border')]
        inside_edges = [(u, v) for u, v in graph.edges if 'is_border' not in graph.edges[u, v]]

        # Draw border edges (solid)
        nx.draw_networkx_edges(
            graph,
            pos,
            edgelist=border_edges,
            style="solid",
            width=2,
            edge_color="black"
        )

        # Draw non-border edges (dotted)
        nx.draw_networkx_edges(
            graph,
            pos,
            edgelist=non_border_edges,
            style="dotted",
            width=2,
            edge_color="black"
        )

        # Draw non-border edges (dotted)
        nx.draw_networkx_edges(
            graph,
            pos,
            edgelist=inside_edges,
            style="solid",
            width=1,
            edge_color="grey"
        )

        # Add labels for nodes and edges
        nx.draw_networkx_labels(graph, pos, labels=labels)
        edge_labels = nx.get_edge_attributes(graph, 'label')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
        plt.axis('off')
        plt.title(title)

        plt.show()
