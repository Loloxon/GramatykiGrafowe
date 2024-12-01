from graph.hypergraph import HyperGraph
from production import Production


class P1(Production):
    @property
    def _left_side(self) -> HyperGraph:
        return HyperGraph(
            nodes=None,   # TODO
            edges=None,   # TODO
            hyperedges=None  # TODO
        )

    @property
    def _right_side(self) -> HyperGraph:
        return HyperGraph(
            nodes=None,  # TODO
            edges=None,  # TODO
            hyperedges=None  # TODO
        )

    def apply(self, graph: HyperGraph) -> HyperGraph:
        pass
