# import networkx as nx
# import matplotlib.pyplot as plt
#
# dicGrafo = {
#     "Arad":["Zerind", "Sibiu", "Timisoara"],
#     "Zerind":["Arad", "Oradea"],
#     "Sibiu":["Arad", "Oradea", "Fagaras", "Rimnicu-Vilcea"],
#     "Timisoara": ["Arad", "Lugoj"],
#     "Oradea": ["Zerind", "Sibiu"],
#     "Fagaras": ["Sibiu", "Bucharest"],
#     "Rimnicu-Vilcea": ["Sibiu", "Pitesti", "Craiova"],
#     "Lugoj": ["Timisoara", "Mehadia"],
#     "Bucharest": ["Fagaras", "Pitesti", "Urziceni", "Giurgiu"],
#     "Pitesti": ["Rimnicu-Vilcea", "Bucharest", "Craiova"],
#     "Craiova": ["Rimnicu-Vilcea", "Pitesti", "Dobretu"],
#     "Mehadia": ["Lugoj", "Dobretu"],
#     "Urziceni": ["Bucharest", "Hirsova", "Vaslui"],
#     "Giurgiu": ["Bucharest"],
#     "Dobretu": ["Mehadia", "Craiova"],
#     "Hirsova": ["Urziceni", "Eforie"],
#     "Vaslui": ["Urziceni", "Iasi"],
#     "Eforie": ["Hirsova"],
#     "Iasi": ["Vaslui", "Neamt"],
#     "Neamt": ["Iasi"]
# }
#
# def paint_edges(graph, pos, route, color):
#     """Função auxiliar que pinta as arestas e os pontos de início e destino no grafo"""
#     edges = [(route[n], route[n + 1]) for n in range(len(route) - 1)]
#     nx.draw_networkx_edges(graph, pos=pos, edgelist=edges, edge_color=color, width=2.0)
#     nx.draw_networkx_nodes(graph, pos, nodelist=[route[0], route[-1]], node_size=120, node_color='blue')
#
#
# def get_pos(graph):
#     """Carrega o posicionamento das arestas caso o mesmo exista,
#     caso contrário, é aplicado o layout spring do NetworkX"""
#
#     try:
#         coord = open('./data/coordinates.csv')
#         pos = {}
#         for line in coord:
#             line.replace("\n", "")
#             line = line.split(",")
#             pos[line[0]] = (float(line[1]), float(line[2]))
#
#     except:
#         pos = nx.spring_layout(graph)
#
#     return pos
#
# graph = nx.Graph(nx.to_networkx_graph(dicGrafo))
#
#
# def deep_Search(inicio, fim, marcados=None):
#     if marcados == None:
#         marcado = []
#     else:
#         marcado = marcados
#
#     if inicio not in marcado:
#         marcado.append(inicio)
#
#     for i in dicGrafo[inicio]:
#         if i not in marcado:
#             marcado.append(i)
#             if i == fim:
#                 marcado.append(0)
#                 return marcado
#             if deep_Search(i, fim, marcado)[-1] == 0:
#                 return marcado
#             else:
#                 marcado.remove(i)
#     return marcado
#
#
# def busca_profunda(inicio, fim):
#     caminho = deep_Search(inicio, fim)
#     caminho.pop(-1)
#     return caminho
#
# pos = get_pos(graph)
# nx.draw_networkx_nodes(graph, pos, node_size=40, node_color='lime')
# nx.draw_networkx_edges(graph, pos)
# nx.draw_networkx_labels(graph, pos)
# paint_edges(graph)
# paint_edges(graph, pos, busca_profunda("Bucharest", "Giurgiu"), 'cyan')
# plt.show()
#
#
# print(graph.get_edge_data("Arad", "Zerind"))

lista1 = ["a", "b"]
lista2 = ["a", "c"]

if lista1 == lista2:
    print("iguais")
else:
    print("diferentes")