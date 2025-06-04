from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self._idMap = {}

    def fillDD_year(self):
        lista_anni = DAO.getAllYear()
        return lista_anni

    def fillDD_shape(self, anno):
        lista_forme = DAO.getShape(anno)
        return lista_forme

    def creoGrafo(self, anno, shape):
        # pulisco il grafo
        self._grafo.clear()

        # creo i nodi e li aggiungo
        lista_nodi = DAO.getNodes(anno, shape)
        #self._grafo.add_nodes_from(lista_nodi)
        for l in lista_nodi:
            self._grafo.add_node(l)
            self._idMap[l.id] = l

        # creo gli archi (grafo orientato)
        lista_archi = DAO.getEdges(anno, shape)
        for a in lista_archi:
            if (a[2] < a[3]):
                self._grafo.add_edge(self._idMap[a[0]], self._idMap[a[1]])
            else:
                self._grafo.add_edge(self._idMap[a[1]], self._idMap[a[0]])

    def graphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def getCompConn(self):
        lista_compCon = list(nx.weakly_connected_components(self._grafo))
        return len(lista_compCon)

    def getMaxCompConn(self):
        lista_compCon = list(nx.weakly_connected_components(self._grafo))
        list_max = max(lista_compCon, key=len)
        return len(list_max), list_max