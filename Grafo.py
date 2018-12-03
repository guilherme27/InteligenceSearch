import heapq, csv

dicGrafo = {
    "Arad":["Zerind", "Sibiu", "Timisoara"],
    "Zerind":["Arad", "Oradea"],
    "Sibiu":["Arad", "Oradea", "Fagaras", "Rimnicu-Vilcea"],
    "Timisoara": ["Arad", "Lugoj"],
    "Oradea": ["Zerind", "Sibiu"],
    "Fagaras": ["Sibiu", "Bucharest"],
    "Rimnicu-Vilcea": ["Sibiu", "Pitesti", "Craiova"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Bucharest": ["Fagaras", "Pitesti", "Urziceni", "Giurgiu"],
    "Pitesti": ["Rimnicu-Vilcea", "Bucharest", "Craiova"],
    "Craiova": ["Rimnicu-Vilcea", "Pitesti", "Dobretu"],
    "Mehadia": ["Lugoj", "Dobretu"],
    "Urziceni": ["Bucharest", "Hirsova", "Vaslui"],
    "Giurgiu": ["Bucharest"],
    "Dobretu": ["Mehadia", "Craiova"],
    "Hirsova": ["Urziceni", "Eforie"],
    "Vaslui": ["Urziceni", "Iasi"],
    "Eforie": ["Hirsova"],
    "Iasi": ["Vaslui", "Neamt"],
    "Neamt": ["Iasi"]
}

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class Grafo(object):
    """ Implementação básica de um grafo. """

    def __init__(self, grafo, direcionado=False):
        self._grafo = grafo  # defaultdict(set)
        # self._direcionado = direcionado
        # self.adiciona_arestas(arestas)

    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """

        return list(self._grafo.keys())

    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """

        return [(k, v) for k in self._grafo.keys() for v in self._grafo[k]]

    def get_neighbors(self, vertice):
        return self._grafo[vertice]

    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo. """

        for u, v in arestas:
            self.adiciona(u, v)

    def adiciona(self, u, v):
        """ Adiciona uma ligação (aresta) entre os nodos 'u' e 'v'. """

        self._grafo[u].add(v)
        if not self._direcionado:
            self._grafo[v].add(u)

    def eh_conectado(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """

        return u in self._grafo and v in self._grafo[u]

    def create_graph(self, roat):
        """ Criar grafo """

        cities = open(roat)


        for line in cities:
            list = []
            data = line.split(",")
            key = data.pop(0)
            list.append(data)
            dicGrafo[key] = list


    def busca_em_Largu(self, inicio, fim):
        """ Width Search"""

        marcados = [inicio]
        fila = [inicio]
        caminho = []
        # if vertice_at not in marcados:

        while fila:
            vertice = fila.pop(0)
            caminho.append(vertice)
            for i in self._grafo[vertice]:
                if i not in marcados:
                    marcados.append(i)
                    fila.append(i)
                if vertice == fim:
                    return caminho


    def deep_Search(self, inicio, fim, marcados = []):
        marcado = marcados

        if inicio not in marcado:
            marcado.append(inicio)

        for i in self._grafo[inicio]:
            if i not in marcados:
                marcados.append(i)
                if i == fim:
                    marcado.append(0)
                    return marcado
                if grafo.deep_Search(i, fim, marcado)[-1] == 0:
                    return marcado
        return marcado

    def busca_profunda(self, inicio, fim):
        caminho = grafo.deep_Search(inicio, fim)
        caminho.pop(-1)
        return caminho

    def cost(self, inicial, final):
        with open('data\edges2.csv', 'r') as distancia_arestas:
            reader = csv.reader(distancia_arestas)
            for linha in reader:
                if linha[0] == inicial:
                    if linha[1] == final:
                        return int(linha[2])
                elif linha[1] == inicial:
                    if linha[0] == final:
                        return int(linha[2])
        return 0

    def heuristica(self, inicial, final):
        with open('data\Heuristic2.csv', 'r') as distancia_arestas:
            reader = csv.reader(distancia_arestas)
            lista_linhas = list(reader)
            for linha in range(len(lista_linhas)):
                if lista_linhas[linha][0] == inicial:
                    for coluna in range(len(lista_linhas[0])):
                        if lista_linhas[0][coluna] == final:
                            if lista_linhas[linha][coluna] != "":
                                return lista_linhas[linha][coluna]
                            else:
                                return lista_linhas[coluna][linha]
        return 0

    def a_star_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in grafo.get_neighbors(current):
                new_cost = cost_so_far[current] + grafo.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + float(self.heuristica(goal, next))
                    frontier.put(next, priority)
                    came_from[next] = current

        return list(came_from.keys())#, cost_so_far    # <-- descomente este trecho, caso queira exibir também os custos do caminho


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._grafo))


grafo = Grafo(dicGrafo, direcionado=True)


# alguns desses prints estão agora no arquivo InterfaceGrafica.py
# print("busca em Largura: ", grafo.busca_em_Largu("Arad", "Bucharest"))
# print("busca em profundidade: ", grafo.busca_profunda("Arad", "Bucharest"))
# print("busca com A*: ", grafo.a_star_search("Arad", "Bucharest"))
# print(grafo._grafo,"\n")
# print(grafo.get_vertices())
# print(grafo.eh_conectado("Ar", "Pi"))
