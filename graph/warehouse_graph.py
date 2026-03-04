# graph/warehouse_graph.py

import networkx as nx


def build_warehouse_graph_for_distances(
    num_aisles,
    aisle_length=28.5,
    n_locs=30,
    opening_between_aisles=3.0,
    aisle_width=5.5,
    DI_O=0.0,
    approach_distance=None,
    include_top_cross=True,
    include_middle_cross=True,
):

    if approach_distance is None:
        approach_distance = aisle_width / 2.0

    step = aisle_length / n_locs
    pitch = opening_between_aisles
    mid_loc = n_locs // 2

    G = nx.DiGraph()
    depot = ("DEPOT", 0)
    G.add_node(depot)

    # Junctions
    for a in range(1, num_aisles + 1):
        G.add_node((a, "Jb"))
        if include_top_cross:
            G.add_node((a, "Jt"))
        if include_middle_cross:
            G.add_node((a, "Jm"))

    def connect_horizontal(tag):
        for a in range(1, num_aisles):
            G.add_edge((a, tag), (a + 1, tag), weight=pitch)
            G.add_edge((a + 1, tag), (a, tag), weight=pitch)

    connect_horizontal("Jb")
    if include_top_cross:
        connect_horizontal("Jt")
    if include_middle_cross:
        connect_horizontal("Jm")

    G.add_edge(depot, (1, "Jb"), weight=DI_O)
    G.add_edge((1, "Jb"), depot, weight=DI_O)

    for a in range(1, num_aisles + 1):

        if a % 2 == 1:
            G.add_edge((a, "Jb"), (a, 1, "C"), weight=step)

            for p in range(1, mid_loc - 1):
                G.add_edge((a, p, "C"), (a, p + 1, "C"), weight=step)

            G.add_edge((a, mid_loc - 1, "C"), (a, "Jm"), weight=step)
            G.add_edge((a, "Jm"), (a, mid_loc + 1, "C"), weight=step)

            for p in range(mid_loc + 1, n_locs):
                G.add_edge((a, p, "C"), (a, p + 1, "C"), weight=step)

            G.add_edge((a, n_locs, "C"), (a, "Jt"), weight=step)

        else:
            G.add_edge((a, "Jt"), (a, n_locs, "C"), weight=step)

            for p in range(n_locs, mid_loc + 1, -1):
                G.add_edge((a, p, "C"), (a, p - 1, "C"), weight=step)

            G.add_edge((a, mid_loc + 1, "C"), (a, "Jm"), weight=step)
            G.add_edge((a, "Jm"), (a, mid_loc - 1, "C"), weight=step)

            for p in range(mid_loc - 1, 1, -1):
                G.add_edge((a, p, "C"), (a, p - 1, "C"), weight=step)

            G.add_edge((a, 1, "C"), (a, "Jb"), weight=step)

    for r in range(1, num_aisles + 1):
        for p in list(range(1, mid_loc)) + list(range(mid_loc + 1, n_locs + 1)):

            G.add_edge((r, p, "L"), (r, p, "C"), weight=approach_distance)
            G.add_edge((r, p, "C"), (r, p, "L"), weight=approach_distance)

            if r < num_aisles:
                G.add_edge((r, p, "R"), (r + 1, p, "C"), weight=approach_distance)
                G.add_edge((r + 1, p, "C"), (r, p, "R"), weight=approach_distance)

    G.add_node(("FLEX", 0))
    G.add_node(("FHUM", 0))

    G.add_edge((3, "Jt"), ("FLEX", 0), weight=3.0)
    G.add_edge(("FLEX", 0), (3, "Jt"), weight=3.0)

    G.add_edge((11, "Jt"), ("FHUM", 0), weight=3.0)
    G.add_edge(("FHUM", 0), (11, "Jt"), weight=3.0)

    return G, depot