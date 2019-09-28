# 目的は各都市が繋がっている隣町を明らかにしたい

from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V')  # グラフの節点の型


class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]
        # Edgeは[u, v]で表されるので self._edges は[[u1, v1], [u2, v2],....]となる

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)  # グラフの節点の個数を算出

    @property
    def edge_count(self) -> int:
        # Listのそれぞれの辺の本数をsumで合計とする
        return sum(map(len, self._edges))  # グラフの辺の数を算出

    # 追加して節点のIndexを返す関数
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])  # 節点が一つ追加されたら辺のリストも一つ増える
        return self.vertex_count - 1  # Indexは0始まりだから

    # 一つの辺は二つの節点をもつ。無向グラフなので辺の両側を追加する
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)  # Edgeは[u(始点), v(終点)]で表せる。始点にまずedgeを追加
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    #  節点から辺を追加する
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)  # [1,2,3]という配列がある時、[1,2,3].index(1) -> 2となる
        v: int = self._vertices.index(second)
        #  uとvは節点のインデックス
        self.add_edge_by_indices(u, v)

    def vertex_at(self, index: int) -> V:
        # 節点のインデックスを参照して節点Vを求める
        return self._vertices[index]

    #  節点のIndexを求める
    def index_of(self, vertex: V) -> int:
        return self._vertices.index[vertex]

    #  あるIndexの節点が連結している節点を全て求める
    def neighbors_for_index(self, index: int) -> List[V]:
        # 指定の節点に繋がっているvの節点を全て求める
        # 下記の記法はmapがvertex_atを引数 e.v に行うという記法
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc


if __name__ == "__main__":
    # test basic Graph construction
    city_graph: Graph[str] = Graph(
        ["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston", "New York", "Atlanta",
         "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")

    print(city_graph)
