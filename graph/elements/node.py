class Node:
    def __init__(self, x: float, y: float, is_hanging: bool, label: str = "V"):
        """
        Initializes a Node object.

        Args:
            x (float): The x-coordinate of the node in a 2D space.
            y (float): The y-coordinate of the node in a 2D space.
            is_hanging (bool): A boolean attribute representing "hanging node" a property (true means node is hanging).
            label (str, optional): A label for the node. Defaults to "V".
        """
        self.x = x
        self.y = y
        self.is_hanging = is_hanging
        self.label = label

    def __str__(self):
        string = f"Node: {self.x} {self.y}, {self.is_hanging} ({self.label})"
        return string
