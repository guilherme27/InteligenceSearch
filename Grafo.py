import heapq, csv
import networkx as nx
import matplotlib.pyplot as plt

'''dicGrafo = {
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
}'''

def create_graph(roat):
    """ Criar grafo """

    cities = open(roat)
    dicGrafo = {}

    for line in cities:
        line = line.replace("\n", "")
        data = line.split(",")
        key = data.pop(0)
        dicGrafo[key] = data

    return dicGrafo

def paint_edges(graph, pos, route, color):
    """Função auxiliar que pinta as arestas e os pontos de início e destino no grafo"""
    edges = [(route[n], route[n + 1]) for n in range(len(route) - 1)]
    nx.draw_networkx_edges(graph, pos=pos, edgelist=edges, edge_color=color, width=2.0)
    nx.draw_networkx_nodes(graph, pos, nodelist=[route[0], route[-1]], node_size=120, node_color='blue')

def get_pos(graph):
    """Carrega o posicionamento das arestas caso o mesmo exista,
    caso contrário, é aplicado o layout spring do NetworkX"""

    try:
        coord = open('./data/coordinates.csv')
        pos = {}
        for line in coord:
            line.replace("\n", "")
            line = line.split(",")
            pos[line[0]] = (float(line[1]), float(line[2]))

    except:
        pos = nx.spring_layout(graph)

    return pos

def plota_largura(grafo_nx, inicio, fim):
    pos = get_pos(grafo_nx)
    nx.draw_networkx_nodes(grafo_nx, pos, node_size=40, node_color='green')
    nx.draw_networkx_edges(grafo_nx, pos)
    nx.draw_networkx_labels(grafo_nx, pos)
    paint_edges(grafo_nx, pos, grafo.busca_em_largura(inicio, fim), 'lime')
    plt.show()

def plota_profundidade(grafo_nx, inicio, fim):
    pos = get_pos(grafo_nx)
    nx.draw_networkx_nodes(grafo_nx, pos, node_size=40, node_color='green')
    nx.draw_networkx_edges(grafo_nx, pos)
    nx.draw_networkx_labels(grafo_nx, pos)
    paint_edges(grafo_nx, pos, grafo.busca_profunda(inicio, fim), 'cyan')
    plt.show()

def plota_A_estrela(grafo_nx, inicio, fim):
    pos = get_pos(grafo_nx)
    nx.draw_networkx_nodes(grafo_nx, pos, node_size=40, node_color='green')
    nx.draw_networkx_edges(grafo_nx, pos)
    nx.draw_networkx_labels(grafo_nx, pos)
    paint_edges(grafo_nx, pos, grafo.a_star_search(inicio, fim), 'red')
    plt.show()

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




    def width_Search(self, inicio, fim, marcado_param=None, fila_param=None):
        """ Width Search"""

        # marcados = [inicio]
        # caminho = []
        # if vertice_at not in marcados:

        # while fila:
        #     vertice = fila.pop(0)
        #     caminho.append(vertice)
        #     for i in self._grafo[vertice]:
        #         if i not in marcados:
        #             marcados.append(i)
        #             fila.append(i)
        #         if vertice == fim:
        #             return caminho

        caminho = []

        if marcado_param == None:
            marcado = []
        else:
            marcado = marcado_param

        if fila_param == None:
            fila = [inicio]
        else:
            fila = fila_param

        if inicio not in caminho:
            caminho.append(inicio)

        if inicio not in marcado:
            marcado.append(inicio)

        vertice = fila.pop(0)

        if self._grafo[vertice] == marcado:
            resultado = grafo.width_Search(vertice, fim, marcado, fila)
            if resultado[-1] == 0:
                return caminho + resultado
            else:
                caminho.remove(vertice)

        for i in self._grafo[vertice]:
            if i not in marcado:
                marcado.append(i)
                caminho.append(i)
                fila.append(i)
                if i == fim:
                    caminho.append(0)
                    return caminho
                else:
                    caminho.remove(i)
                resultado = grafo.width_Search(fila[0], fim, marcado, fila)
                if resultado[-1] == 0:
                    return caminho + resultado

        return caminho

    def busca_em_largura(self, inicio, fim):
        caminho = grafo.width_Search(inicio, fim)
        caminho.pop(-1)
        return caminho

    def deep_Search(self, inicio, fim, marcados=None):
        if marcados == None:
            marcado = []
        else:
            marcado = marcados

        if inicio not in marcado:
            marcado.append(inicio)

        for i in self._grafo[inicio]:
            if i not in marcado:
                marcado.append(i)
                if i == fim:
                    marcado.append(0)
                    return marcado
                if grafo.deep_Search(i, fim, marcado)[-1] == 0:
                    return marcado
                else:
                    marcado.remove(i)
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

dicGrafo = create_graph("data\DicGrafo.csv")

grafo = Grafo(dicGrafo, direcionado=True)
grafo_nx = nx.Graph(nx.to_networkx_graph(dicGrafo))

# alguns desses prints estão agora no arquivo InterfaceGrafica.py
# print("busca em Largura: ", grafo.busca_em_largura("Arad", "Bucharest"))
# print("busca em profundidade: ", grafo.busca_profunda("Arad", "Bucharest"))
# print("busca em profundidade: ", grafo.busca_profunda("Arad", "Bucharest"))
# print("busca em profundidade: ", grafo.busca_profunda("Arad", "Bucharest"))
# print("busca com A*: ", grafo.a_star_search("Arad", "Bucharest"))
# print(grafo._grafo,"\n")
# print(grafo.get_vertices())
# print(grafo.eh_conectado("Ar", "Pi"))
