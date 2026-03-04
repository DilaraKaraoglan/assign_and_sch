# routing/time_and_compatibility.py

def pallet_type(pallet, item_map):
    weights = {item_map[it["item_id"]][3] for it in pallet["items"]}
    return "HUMAN_ONLY" if 0 in weights else "FLEXIBLE"


def pallet_agent_compatibility(pallets, agents, item_map):

    matrix = []

    for pallet in pallets:
        ptype = pallet_type(pallet, item_map)
        row = []

        for ag in agents:
            if ptype == "HUMAN_ONLY":
                row.append(1 if ag["type"] == "human" else 0)
            else:
                row.append(1)

        matrix.append(row)

    return matrix


def pallet_total_time(pallet, tsp_result, agent, search_time):

    walk_time = tsp_result["distance"] / agent["speed"]

    service_time = sum(
        it["qty"] * (agent["pickTime"] + search_time[agent["type"]])
        for it in pallet["items"]
    )

    return round(walk_time + service_time, 2)


def build_time_matrix(pallets, pallet_tsp, agents, search_time):

    matrix = []

    for i, pallet in enumerate(pallets):
        row = []
        for ag in agents:
            row.append(
                pallet_total_time(
                    pallet,
                    pallet_tsp[i],
                    ag,
                    search_time
                )
            )
        matrix.append(row)

    return matrix