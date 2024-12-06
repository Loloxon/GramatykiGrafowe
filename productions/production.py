from abc import ABC, abstractmethod

import networkx as nx

from graph.elements.node import Node
from graph.hypergraph import HyperGraph


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
    @abstractmethod
    def _right_side(self) -> HyperGraph:
        """Abstract property that must be implemented in subclasses."""
        pass

    @abstractmethod
    def transform(self, graph: HyperGraph, node_map: dict[Node, Node], left_side: HyperGraph) -> (bool, HyperGraph):
        """Abstract method to transform the main graph."""
        pass

    def apply(self, graph: HyperGraph) -> (bool, HyperGraph):
        left_side = self.get_left_side()
        node_map = self.check(graph, left_side)

        if node_map:
            reversed_node_map = {v: k for k, v in node_map.items() if isinstance(v, Node) and isinstance(k, Node)}

            return self.transform(graph, reversed_node_map, left_side)

        return False, graph

    def visualize(self) -> None:
        HyperGraph.visualize_hypergraph(self.get_left_side().parse_hypergraph_to_networkx(),
                                        f"Left side of production {self._name}")
        HyperGraph.visualize_hypergraph(self.get_right_side().parse_hypergraph_to_networkx(),
                                        f"Right side of production {self._name}")

    def get_left_side(self) -> HyperGraph:
        return self._left_side

    def get_right_side(self) -> HyperGraph:
        return self._right_side

    @staticmethod
    def check(graph: HyperGraph, subgraph: HyperGraph) -> bool | dict:
        return Production._find_subgraph(graph, subgraph)

    @staticmethod
    def _find_subgraph(graph: HyperGraph, subgraph: HyperGraph) -> bool | dict:
        """Abstract method to check if the production can be applied."""
        matcher = nx.algorithms.isomorphism.GraphMatcher(
            graph.parse_hypergraph_to_networkx(),
            subgraph.parse_hypergraph_to_networkx(),
            node_match=Production._node_match)

        try:
            return next(matcher.subgraph_isomorphisms_iter())
        except StopIteration:
            return False

    @staticmethod
    def _node_match(v_self, v_left):
        return ("label" in v_self.keys() and "label" in v_left.keys() and v_self["label"] == v_left["label"]) and \
            (("is_hanging" in v_self.keys() and "is_hanging" in v_left.keys() and v_self["is_hanging"] == v_left[
                "is_hanging"]
              ) or (
                     "is_production_relevant" in v_left.keys() and not v_left["is_production_relevant"]
             )) or \
            ("is_removable" in v_self.keys() and "is_removable" in v_left.keys() and v_self["is_removable"] ==
             v_left["is_removable"])
