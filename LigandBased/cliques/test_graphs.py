import networkx as nx
import copy

def complete_graphs() -> list:
    """ Returns a set of complete graphs without repeated labels"""
    G = nx.Graph()
    G.name = "G"
    nodes = [(1, "A"),(2, "N"),(3, "D"),(4, "R")]
    edges = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    labels = [3, 4, 5, 8, 4, 2]
    for node in nodes:
        G.add_node(node[0], feat_type=node[1])
    for ii in range(len(edges)):
        G.add_edge(edges[ii][0], edges[ii][1], distance=labels[ii])
    assert G.number_of_edges() == (G.number_of_nodes() * (G.number_of_nodes() - 1)) / 2 # Condition for complete graphs

    J = nx.Graph()
    J.name = "J" # J is very similar to G. The only difference is the label N is replaced by P
    nodes = [(1, "A"),(2, "P"),(3, "D"),(4, "R")]
    edges = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    for node in nodes:
        J.add_node(node[0], feat_type=node[1])
    for ii in range(len(edges)):   
        J.add_edge(edges[ii][0], edges[ii][1], distance=labels[ii])
    assert J.number_of_edges() == (J.number_of_nodes() * (J.number_of_nodes() - 1)) / 2 # Condition for complete graphs

    H = copy.deepcopy(G) # H is a supergraph of G
    H.name = "H"
    nodes = [(5, "H"), (6, "P")]
    edges = [(1, 5), (1, 6), (2, 5), (2, 6), (3, 5),
            (3, 6), (4, 5), (4, 6), (5, 6)]
    labels = [4, 3, 5, 6, 5, 2, 8, 7, 4]
    for node in nodes:
        H.add_node(node[0], feat_type=node[1])
    for ii in range(len(edges)):
        H.add_edge(edges[ii][0], edges[ii][1], distance=labels[ii], color="black")
    assert H.number_of_edges() == (H.number_of_nodes() * (H.number_of_nodes() - 1)) / 2, f"Graph has {H.number_of_edges()} edges"

    return [G, H, J]

def k4_repeated_labels() -> nx.Graph:
    """ Returns a complete graph with four nodes and repeated node labels"""
    k4 = nx.Graph()
    k4.name = "Graph 1"
    nodes = [(1, "A"),(2, "A"),(3, "D"),(4, "R")]
    # node1, node2, edgelabel
    edges = [(1, 2, 3),(1, 3, 4),(1, 4, 5),(2, 3, 8),(2, 4, 4),(3, 4, 2)]
    for node in nodes:
        k4.add_node(node[0], feat_type=node[1])
    for edge in edges:
        k4.add_edge(edge[0], edge[1], distance=edge[2])
    assert k4.number_of_edges() == (k4.number_of_nodes() * (k4.number_of_nodes() - 1)) / 2 # Condition for complete graphs
    return k4

def k5_repeated_labels() -> nx.Graph:
    """ Returns a complete graph with five nodes and repeated node labels"""
    k5 = nx.Graph()
    k5.name = "Graph 2"
    nodes = [(1, "A"), (2, "R"), (3, "H"), (4, "D"), (5, "H")]
    edges = [(1, 2, 7), (1, 3, 2), (1, 4, 6), (1, 5, 5), (2, 3, 4),
        (2, 4, 3), (2, 5, 5), (3, 4, 8), (3, 5, 5), (4, 5, 4)]
    for node in nodes:
        k5.add_node(node[0], feat_type=node[1])
    for edge in edges:
        k5.add_edge(edge[0], edge[1], distance=edge[2])     
    assert k5.number_of_edges() == (k5.number_of_nodes() * (k5.number_of_nodes() - 1)) / 2 # Condition for complete graphs
    return k5

def k6_repeated_labels() -> nx.Graph:
    """ Returns a complete graph with six nodes and repeated node labels"""
    k6 = nx.Graph()
    k6.name = "Graph 3"
    nodes = [(1, "D"), (2, "R"), (3, "R"), (4, "A"), (5, "D"), (6, "R")]
    edges = [(1, 2, 4),(1, 3, 8),(1, 4, 2),(1, 5, 5),(1, 6, 7),
        (2, 3, 3), (2, 4, 7), (2, 5, 9), (2, 6, 8), (3, 4, 6), (3, 5, 4),
        (3, 6, 3), (4, 5, 5), (4, 6, 2), (5, 6, 3)]
    for node in nodes:
        k6.add_node(node[0], feat_type=node[1])
    for edge in edges:
        k6.add_edge(edge[0], edge[1], distance=edge[2])     
    assert k6.number_of_edges() == (k6.number_of_nodes() * (k6.number_of_nodes() - 1)) / 2 # Condition for complete graphs
    return k6


def k3_single_label() -> nx.Graph:   
    k3 = nx.Graph()
    nodes = [(1, "A"),(2, "A"),(3, "A")]
    edges = [(1, 2, 4),(1, 3, 3),(2, 3, 2)]
    for node in nodes:
        k3.add_node(node[0], feat_type=node[1])
    for edge in edges:
        k3.add_edge(edge[0], edge[1], distance=edge[2])     
    assert k3.number_of_edges() == (k3.number_of_nodes() * (k3.number_of_nodes() - 1)) / 2 # Condition for complete graphs
    return k3

def k4_single_label() -> nx.Graph:   
    k4 = nx.Graph()
    nodes = [(1, "A"),(2, "A"),(3, "A"),(4, "A")]
    edges = [(1, 2, 3), (1, 3, 4), (1, 4, 6), (2, 3, 4), (2, 4, 5), (3, 4, 3)]
    for node in nodes:
        k4.add_node(node[0], feat_type=node[1])
    for edge in edges:
        k4.add_edge(edge[0], edge[1], distance=edge[2])     
    assert k4.number_of_edges() == (k4.number_of_nodes() * (k4.number_of_nodes() - 1)) / 2 # Condition for complete graphs
    return k4
