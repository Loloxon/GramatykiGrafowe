import matplotlib.pyplot as plt
import networkx as nx

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

        new_edge_1 = Edge(node_1=node_1, node_2=new_node, is_border=edge.is_border)
        new_edge_2 = Edge(node_1=new_node, node_2=node_2, is_border=edge.is_border)
        self.edges.remove(edge)
        self.edges.append(new_edge_1)
        self.edges.append(new_edge_2)

        return new_node

    def parse_hypergraph_to_networkx(self):
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

    def parse_networkx_to_hypergraph(self, G: nx.Graph) -> 'HyperGraph':
        nodes = []
        edges = []
        hyperedges = []

        # Create nodes
        for node, data in G.nodes(data=True):
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
        for node1, node2, data in G.edges(data=True):
            if isinstance(node1, str) and node1.startswith("hyperedge_"):
                # Skip hyperedge nodes (they are not part of regular edges)
                continue

            is_border = data.get('is_border', False)
            label = data.get('label', 'E')
            # Find corresponding nodes in the nodes list
            node1_obj = next(node for node in nodes if node.x == G.nodes[node1]['x'] and node.y == G.nodes[node1]['y'])
            node2_obj = next(node for node in nodes if node.x == G.nodes[node2]['x'] and node.y == G.nodes[node2]['y'])
            edges.append(Edge(node1_obj, node2_obj, is_border, label))

        # Create hyperedges
        for node, data in G.nodes(data=True):
            if isinstance(node, str) and node.startswith("hyperedge_"):
                # This is a hyperedge node, reconstruct the hyperedge
                label = data.get('label', 'Q')
                is_removable = data.get('is_removable', False)
                x = data.get('x', 0)
                y = data.get('y', 0)

                hyperedge_nodes = []
                for neighbor in G.neighbors(node):
                    if not isinstance(neighbor, str):  # Regular node (not a hyperedge node)
                        neighbor_obj = next(
                            n for n in nodes if n.x == G.nodes[neighbor]['x'] and n.y == G.nodes[neighbor]['y'])
                        hyperedge_nodes.append(neighbor_obj)

                hyperedges.append(HyperEdge(hyperedge_nodes, is_removable, label))

        return HyperGraph(nodes, edges, hyperedges)

    def visualize_hypergraph(self, G):
        # Separate regular nodes and hyperedges
        pos = {node: (G.nodes[node]['x'], G.nodes[node]['y']) for node in G.nodes if
               'x' in G.nodes[node] and 'y' in G.nodes[node]}

        labels = nx.get_node_attributes(G, 'label')

        # Separate nodes and hyperedges based on their attributes
        regular_nodes = [node for node in G.nodes if not str(node).startswith("hyperedge_")]
        hyperedge_nodes = [node for node in G.nodes if str(node).startswith("hyperedge_")]

        # Draw regular nodes
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=regular_nodes,
            node_color='lightblue',
            node_size=700,
            label="Nodes"
        )

        # Draw hyperedges
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=hyperedge_nodes,
            node_color='pink',
            node_shape='s',
            node_size=800,
            label="Hyperedges"
        )

        # Draw edges
        nx.draw_networkx_edges(G, pos)

        # Add labels for nodes and edges
        nx.draw_networkx_labels(G, pos, labels=labels)
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.axis('off')

        plt.show()
