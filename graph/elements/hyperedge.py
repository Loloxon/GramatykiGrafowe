import numpy as np

from graph.elements.node import Node


class HyperEdge:
    def __init__(self, nodes: list[Node], is_removable: bool, label: str = "Q"):
        """
        Initializes a HyperEdge object.

        Args:
            nodes (list[Node]): A list of Node objects that are part of this hyperedge.
            is_removable (bool): A boolean attribute representing a property of the hyperedge (e.g., whether it satisfies a condition).
            label (str, optional): A label for the hyperedge. Defaults to "Q".
        """
        self.nodes = nodes
        self.is_removable = is_removable
        self.label = label
        self.x = np.average([node.x for node in self.nodes]).astype(float)
        self.y = np.average([node.y for node in self.nodes]).astype(float)

    def __str__(self):
        string = f"HyperEdge: {self.x}.{self.y}, {self.is_removable} ({self.label}):  -  "
        for node in self.nodes:
            string += f"{node}, "
        return string
