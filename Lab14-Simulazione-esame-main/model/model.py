import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self.grafo = nx.DiGraph()

        self._listChromosome = []
        self._listConnectedGenes = []
        self._listGenes = []
        self.idMap = {}

    def build_graph(self):
        self.grafo.clear()
        self._nodes = DAO.getAllChromosomes()
        self.grafo.add_nodes_from(self._nodes)

        self._listGenes = DAO.getAllGenes()
        for gene in self._listGenes:
            self.idMap[gene.GeneID] = gene.Chromosome

        self._listConnectedGenes = DAO.getAllConnectedGenes()
        for e in self._listConnectedGenes:
            cr1 = e[0]
            cr2 = e[1]
            peso = e[4]
            if cr1 in self.grafo.nodes and cr2 in self.grafo.nodes:
                if self.grafo.has_edge(cr1, cr2):
                    self.grafo[cr1][cr2]['weight'] += peso
                else:
                    self.grafo.add_edge(cr1, cr2, weight=peso)

    def get_min_weight(self):
        min = 1000000
        for e in self.grafo.edges():
            peso = self.grafo[e[0]][e[1]]["weight"]
            if peso < min:
                min = peso
        return min

    def get_max_weight(self):
        max = -100
        for e in self.grafo.edges():
            peso = self.grafo[e[0]][e[1]]["weight"]
            if peso > max:
                max = peso
        return max

    def count_edges(self, t):
        count_bigger = 0
        count_smaller = 0
        for x in self.grafo.edges():
            if self.grafo[x[0]][x[1]]["weight"] > t:
                count_bigger += 1
            elif self.grafo[x[0]][x[1]]["weight"] < t:
                count_smaller += 1
        return count_bigger, count_smaller

    def get_num_of_nodes(self):
        return self.grafo.number_of_nodes()

    def get_num_of_edges(self):
        return self.grafo.number_of_edges()