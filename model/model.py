import networkx as nx
from networkx.algorithms.components import connected_components

from database.DAO import DAO


class Model:

    def __init__(self):
        self.grafo=nx.Graph()
        self.idMap={}

    def buildGraph(self,anno):
        nodi=DAO.getNodes(anno)
        for n in nodi:
            self.idMap[n.CCode]=n
        self.grafo.add_nodes_from(nodi)
        edges=DAO.getEdges(anno,self.idMap)
        for e in edges:
            self.grafo.add_edge(e[0],e[1])

    def getCompConn(self):
        return len(list(connected_components(self.grafo)))

    def getNodes(self):
        stati=[]
        for n in self.grafo.nodes:
            stati.append((n,self.grafo.degree(n)))
        return stati