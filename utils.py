from random import choice

import networkx as nx
from matplotlib import pyplot as plt

from graph.elements.edge import Edge
from graph.elements.hyperedge import HyperEdge
from graph.elements.node import Node
from graph.hypergraph import HyperGraph


def equals(graph1: HyperGraph, graph2: HyperGraph) -> bool:
    return check(graph1, graph2) and check(graph2, graph1)


def check(graph: HyperGraph, subgraph: HyperGraph) -> bool | dict:
    return find_subgraph(graph, subgraph)


def find_subgraph(graph: HyperGraph, subgraph: HyperGraph) -> bool | dict:
    found_subgraphs = find_subgraphs(graph, subgraph)
    return choice(found_subgraphs) if len(found_subgraphs) > 0 else False


def find_subgraphs(graph: HyperGraph, subgraph: HyperGraph) -> list[dict]:
    matcher = nx.algorithms.isomorphism.GraphMatcher(
        graph.parse_hypergraph_to_networkx(),
        subgraph.parse_hypergraph_to_networkx(),
        node_match=node_match
    )

    return list(matcher.subgraph_isomorphisms_iter())


def node_match(v_self, v_left):
    return ("label" in v_self.keys() and "label" in v_left.keys() and v_self["label"] == v_left["label"]) and \
        (("is_hanging" in v_self.keys() and "is_hanging" in v_left.keys() and v_self["is_hanging"] == v_left[
            "is_hanging"]
          ) or (
                 "is_production_relevant" in v_left.keys() and not v_left["is_production_relevant"]
         )) or \
        ("is_removable" in v_self.keys() and "is_removable" in v_left.keys() and v_self["is_removable"] ==
         v_left["is_removable"])


def visualize_hypergraph(graph: nx.Graph, title: str,
                         display_properties: bool = True,
                         display_nodes: bool = True,
                         display_labels: bool = True):
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

    if display_nodes:
        if display_properties:
            # Draw hanging nodes without borders
            nx.draw_networkx_nodes(
                graph,
                pos,
                nodelist=regular_nodes_hanging,
                node_color='lightblue',
                edgecolors='none',  # No border
                node_size=400
            )

            # Draw non-hanging nodes with borders
            nx.draw_networkx_nodes(
                graph,
                pos,
                nodelist=regular_nodes_not_hanging,
                node_color='lightblue',
                edgecolors='black',
                linewidths=2,
                node_size=400
            )

            # Draw removable hyperedges without borders
            nx.draw_networkx_nodes(
                graph,
                pos,
                nodelist=hyperedge_nodes_removable,
                node_color='pink',
                node_shape='s',
                node_size=400
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
                node_size=400
            )
        else:
            nx.draw_networkx_nodes(
                graph,
                pos,
                nodelist=regular_nodes_hanging,
                node_color='lightblue',
                edgecolors='black',
                linewidths=2,
                node_size=400,
                label="Non-Hanging Nodes"
            )
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

            nx.draw_networkx_nodes(
                graph,
                pos,
                nodelist=hyperedge_nodes_removable,
                node_color='pink',
                edgecolors='black',
                linewidths=2,
                node_shape='s',
                node_size=400,
                label="Hyperedges"
            )
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

    if display_properties:
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
    else:
        nx.draw_networkx_edges(
            graph,
            pos,
            edgelist=border_edges,
            style="solid",
            width=2,
            edge_color="black"
        )
        nx.draw_networkx_edges(
            graph,
            pos,
            edgelist=non_border_edges,
            style="solid",
            width=2,
            edge_color="black"
        )

    if display_nodes:
        # Draw edges to hyperedge node (solid, grey)
        nx.draw_networkx_edges(
            graph,
            pos,
            edgelist=inside_edges,
            style="solid",
            width=1,
            edge_color="grey"
        )

    # Add labels for nodes and edges
    if display_labels:
        nx.draw_networkx_labels(graph, pos, labels=labels)
        edge_labels = nx.get_edge_attributes(graph, 'label')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.gca().set_aspect('equal')
    plt.axis('off')
    plt.title(title)

    plt.show()


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
            node for node in nodes if node.x == nx_graph.nodes[node1]['x'] and node.y == nx_graph.nodes[node1]['y']
        )
        node2_obj = next(
            node for node in nodes if node.x == nx_graph.nodes[node2]['x'] and node.y == nx_graph.nodes[node2]['y']
        )
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
                            n.x == nx_graph.nodes[neighbor]['x'] and n.y == nx_graph.nodes[neighbor]['y']
                        )
                    hyperedge_nodes.append(neighbor_obj)

            hyperedges.append(HyperEdge(hyperedge_nodes, is_removable, label))

    return HyperGraph(nodes, edges, hyperedges)
