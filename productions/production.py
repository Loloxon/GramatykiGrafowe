from abc import ABC, abstractmethod

import networkx as nx

from graph.hypergraph import HyperGraph


class Production(ABC):
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
    def apply(self, graph: HyperGraph) -> HyperGraph:
        """Abstract method to apply the production."""
        pass

    def check(self, graph: HyperGraph) -> bool | dict:
        return Production.find_subgraph(graph, self._left_side)

    def get_left_side(self) -> HyperGraph:
        return self._left_side

    def get_right_side(self) -> HyperGraph:
        return self._right_side

    @staticmethod
    def find_subgraph(graph: HyperGraph, subgraph: HyperGraph) -> bool | dict:
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
            ("is_hanging" in v_self.keys() and "is_hanging" in v_left.keys() and v_self["is_hanging"] == v_left[
                "is_hanging"]) or \
            ("is_removable" in v_self.keys() and "is_removable" in v_left.keys() and v_self["is_removable"] ==
             v_left["is_removable"])
