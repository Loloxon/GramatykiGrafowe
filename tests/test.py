from abc import ABC, abstractmethod


class TestProduction(ABC):

    @abstractmethod
    def test_apply_exact_graph(self):
        pass

    @abstractmethod
    def test_apply_extended_graph(self):
        pass

    @abstractmethod
    def test_apply_invalid_graph_missing_node(self):
        pass

    @abstractmethod
    def test_apply_invalid_graph_missing_edge(self):
        pass

    @abstractmethod
    def test_apply_invalid_graph_invalid_label(self):
        pass
