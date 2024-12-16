from graph.elements.node import Node


class Edge:
    def __init__(self, node_1: Node, node_2: Node, is_border: bool, label: str = "E"):
        """
        Initializes an Edge object.

        Args:
            node_1 (Node): The first Node object connected by this edge.
            node_2 (Node): The second Node object connected by this edge.
            is_border (bool): A boolean attribute representing "border" property of the edge.
            label (str, optional): A label for the edge. Defaults to "E".
        """
        self.node_1 = node_1
        self.node_2 = node_2
        self.is_border = is_border
        self.label = label

    def __str__(self):
        string = (
            f"Edge: [{self.node_1}] - [{self.node_2}], {self.is_border} ({self.label})"
        )
        return string
