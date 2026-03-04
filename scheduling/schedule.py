# scheduling/deterministic_schedule.py

def build_route_based_schedule(routes, agents):

    schedule = []

    agent_map = {a["id"]: a for a in agents}
    agent_time = {a["id"]: 0.0 for a in agents}

    routes_by_agent = {}

    for r in routes:
        aid = r["assignedAgentId"]
        if aid is None:
            continue
        routes_by_agent.setdefault(aid, []).append(r)

    for aid, agent_routes in routes_by_agent.items():

        agent_info = agent_map[aid]
        speed = agent_info["speed"]
        pick_time = agent_info["pickTime"]

        for route in agent_routes:

            pallet_idx = route["palletIndex"]

            for seg in route["segments"]:

                travel_time = seg["distance"] / speed
                picking_time = seg["quantity"] * pick_time
                total_duration = travel_time + picking_time

                start_time = agent_time[aid]
                end_time = start_time + total_duration

                schedule.append({
                    "agent": aid,
                    "agentType": agent_info["type"],
                    "palletIndex": pallet_idx,
                    "itemId": seg["itemId"],
                    "start": start_time,
                    "end": end_time,
                    "waitingTime": 0.0
                })

                agent_time[aid] = end_time

    return schedule