# routing/tsp_solver.py

import itertools
import networkx as nx


class PalletTSPSolver:
#Solves for a single pallet by minimizing shortest-path travel distance under aisle constraints.
    def __init__(self, graph, depot, item_map):
        self.G = graph
        self.depot = depot
        self.item_map = item_map
        
    #Computes the optimal visiting order of pallet items and returns the route with its total distance.
    def solve(self, pallet):

        def pallet_type(pallet):
            weights = {self.item_map[it["item_id"]][3] for it in pallet["items"]}
            return "HUMAN_ONLY" if 0 in weights else "FLEXIBLE"

        ptype = pallet_type(pallet)
        finish_node = ("FHUM", 0) if ptype == "HUMAN_ONLY" else ("FLEX", 0)

        item_nodes = []
        aisle_lookup = {}

        # Build list of unique item nodes and their corresponding aisles
        for it in pallet["items"]:
            rack, pos, face, _ = self.item_map[it["item_id"]]
            real_aisle = rack if face.upper() == "L" else rack + 1 
            node = (rack, pos, face.upper())
            item_nodes.append(node)
            aisle_lookup[node] = real_aisle

        item_nodes = list(dict.fromkeys(item_nodes))

        best_distance = float("inf")
        best_route = None

        # Generate all permutations of item nodes and evaluate their total travel distance while respecting aisle constraints
        for perm in itertools.permutations(item_nodes):

            aisles = [aisle_lookup[n] for n in perm]
            if any(aisles[i] > aisles[i + 1] for i in range(len(aisles) - 1)):
                continue

            total = 0
            current = self.depot

            total += nx.dijkstra_path_length(self.G, current, perm[0], weight="weight")
            current = perm[0]

            for i in range(1, len(perm)):
                total += nx.dijkstra_path_length(self.G, current, perm[i], weight="weight")
                current = perm[i]

            total += nx.dijkstra_path_length(self.G, current, finish_node, weight="weight")
            
            # Update best route if current distance has a shorter total distance
            if total < best_distance:
                best_distance = total
                best_route = perm

        return {
            "route_nodes": list(best_route),
            "distance": best_distance
        }