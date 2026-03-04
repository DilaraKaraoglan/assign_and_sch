import networkx as nx
from routing.time_and_compatibility import pallet_type

class RouteBuilder:

    def __init__(self, graph, depot, item_map):
        self.G = graph
        self.depot = depot
        self.item_map = item_map

    def build_routes(self, pallets, pallet_tsp, assignment_matrix):

        routes = []

        for pallet_idx, pallet in enumerate(pallets):

            assigned_agent = None
            for agent_idx, val in enumerate(assignment_matrix[pallet_idx]):
                if val == 1:
                    assigned_agent = agent_idx
                    break

            segments = []
            prev_node = self.depot

            for node in pallet_tsp[pallet_idx]["route_nodes"]:

                item_id = None
                qty = 0

                for it in pallet["items"]:
                    r, p, face, _ = self.item_map[it["item_id"]]
                    if (r, p, face.upper()) == node:
                        item_id = it["item_id"]
                        qty = it["qty"]
                        break

                if item_id is None:
                    continue

                dist = nx.dijkstra_path_length(
                    self.G,
                    prev_node,
                    node,
                    weight="weight"
                )

                segments.append({
                    "itemId": item_id,
                    "distance": dist,
                    "quantity": qty
                })

                prev_node = node

            routes.append({
                "palletIndex": pallet_idx,
                "assignedAgentId": assigned_agent,
                "palletType": pallet_type(pallet, self.item_map),
                "segments": segments
            })

        return routes