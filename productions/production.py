from abc import ABC, abstractmethod
from copy import deepcopy

from graph.elements.node import Node
from graph.hypergraph import HyperGraph
from utils import check, visualize_hypergraph


class Production(ABC):
    @property
    @abstractmethod
    def _name(self) -> str:
        """Abstract property that must be implemented in subclasses."""
        pass

    @property
    @abstractmethod
    def _left_side(self) -> HyperGraph:
        """Abstract property that must be implemented in subclasses."""
        pass

    @property
    def _right_side(self) -> HyperGraph:
        graph = deepcopy(self.get_left_side())
        self.apply(graph)
        return graph

    @abstractmethod
    def transform(
        self, graph: HyperGraph, node_map: dict[Node, Node], left_side: HyperGraph
    ) -> (bool, HyperGraph):
        """Abstract method to transform the main graph."""
        pass

    def apply(self, graph: HyperGraph) -> (bool, HyperGraph):
        left_side = self.get_left_side()
        node_map = check(graph, left_side)

        if node_map:
            reversed_node_map = {
                v: k
                for k, v in node_map.items()
                if isinstance(v, Node) and isinstance(k, Node)
            }

            return self.transform(graph.copy(), reversed_node_map, left_side)

        return False, graph.copy()

    def visualize(self) -> None:
        visualize_hypergraph(
            self.get_left_side().parse_hypergraph_to_networkx(),
            f"Left side of production {self._name}",
        )
        visualize_hypergraph(
            self.get_right_side().parse_hypergraph_to_networkx(),
            f"Right side of production {self._name}",
        )

    def get_left_side(self) -> HyperGraph:
        return self._left_side

    def get_right_side(self) -> HyperGraph:
        return self._right_side
