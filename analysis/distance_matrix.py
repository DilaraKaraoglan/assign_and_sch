# analysis/distance_matrix.py

import networkx as nx


def item_id_to_node(item_id, item_map):
    r, p, face, _ = item_map[item_id]
    return (r, p, face.upper())


def build_distance_matrix(G, depot, item_ids, item_map):

    finish_nodes = [("FLEX", 0), ("FHUM", 0)]

    labels = ["DEPOT"] + item_ids + ["FLEX_FINISH", "HUMAN_FINISH"]

    nodes = (
        [depot]
        + [item_id_to_node(i, item_map) for i in item_ids]
        + finish_nodes
    )

    N = len(nodes)
    D = [[0.0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        lengths = nx.single_source_dijkstra_path_length(
            G,
            nodes[i],
            weight="weight"
        )

        for j in range(N):
            if i != j:
                D[i][j] = lengths.get(nodes[j], float("inf"))

    return labels, D