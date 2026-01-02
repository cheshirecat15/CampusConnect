import networkx as nx
from networkx.algorithms.community import louvain_communities

def detect_communities(G):
    """
    Detects communities using the Louvain algorithm.
    Returns a list of sets (each set = one community).
    """
    communities = louvain_communities(G, weight="weight")
    return communities
