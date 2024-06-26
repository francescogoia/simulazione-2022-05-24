import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}
        self._generi = DAO.getAllGenres()

    def _creaGrafo(self, genere):
        self._grafo.clear()
        self._nodes = DAO.getAllNodes(genere)
        self._grafo.add_nodes_from(self._nodes)
        for n in self._nodes:
            self._idMap[n.TrackId] = n
        archi = DAO.getAllEdges(genere, self._idMap)
        for a in archi:
            self._grafo.add_edge(a[0], a[1], weight=a[2])

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def durataMax(self):
        archi = list(self._grafo.edges(data=True))
        archi.sort(key=lambda x: x[2]["weight"], reverse=True)
        durataMax = archi[0][2]["weight"]
        result = []
        for a in archi:
            if a[2]["weight"] == durataMax:
                result.append(a)
        return result

    def handleLista(self, idPartenza, dimensioneMax):
        self._bestPath = []
        self._bestDimensione = 0
        partenza = self._idMap[idPartenza]
        self._connessa = list(nx.node_connected_component(self._grafo, partenza))
        self._ricorsione(partenza, [(partenza, partenza.Bytes)], dimensioneMax, 0)
        return self._bestPath, self._bestDimensione

    def _ricorsione(self, nodo, parziale, dimensioneMax, pos):
        memoriaParziale = self.getMemoriaParziale(parziale)
        if len(parziale) > 0:
            if memoriaParziale < dimensioneMax:
                if len(parziale) > len(self._bestPath):  # and memoriaParziale > self._bestDimensione: sbagliato, conta la lunghezza di parziale
                    self._bestDimensione = memoriaParziale
                    self._bestPath = copy.deepcopy(parziale)
            elif memoriaParziale > dimensioneMax:
                return
        for v in self._connessa[pos:]:
            pos += 1
            if self.filtroNodi(v, parziale):
                dimV = v.Bytes
                parziale.append((v, dimV))
                self._ricorsione(v, parziale, dimensioneMax, pos)
                parziale.pop()

    def filtroNodi(self, v, parziale):
        for a in parziale:
            if a[0] == v:
                return False
        return True

    def filtroArchi(self, n, v, parziale):
        pass

    def getMemoriaParziale(self, parziale):
        totM = 0
        for a in parziale:
            totM += a[0].Bytes
        return totM
