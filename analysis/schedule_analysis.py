# analysis/schedule_analysis.py

from collections import defaultdict


def pretty_print_schedule(best_schedule):

    agents = defaultdict(list)

    for s in best_schedule:
        agents[s["agentId"]].append(s)

    for agent_id in sorted(agents.keys()):

        print(f"\nAGENT {agent_id}")
        print("-" * 50)

        agent_segments = sorted(
            agents[agent_id],
            key=lambda x: x["start"]
        )

        for seg in agent_segments:

            duration = seg["end"] - seg["start"]

            print(
                f"P{seg['palletIndex']} | "
                f"{seg['itemId']} | "
                f"{seg['start']:.2f} → {seg['end']:.2f} | "
                f"Dur: {duration:.2f} | "
                f"Wait: {seg['waitingTime']:.2f}"
            )


def item_conflict_analysis(best_schedule):

    items = defaultdict(list)

    for s in best_schedule:
        items[s["itemId"]].append(s)

    for item, segments in items.items():
        if len(segments) > 1:
            print(f"\nITEM {item} conflict:")
            for seg in segments:
                print(
                    f"Agent {seg['agentId']} "
                    f"{seg['start']:.2f} → {seg['end']:.2f}"
                )
                
def print_waiting_summary(best_schedule):

    print("\n WAITING SUMMARY \n")

    waiting_segments = [
        s for s in best_schedule
        if s.get("waitingTime", 0) > 0
    ]

    if not waiting_segments:
        print("No waiting detected.")
        return

    for seg in waiting_segments:
        print(
            f"Agent {seg['agentId']} "
            f"waited {seg['waitingTime']:.2f}s "
            f"for item {seg['itemId']} "
            f"(Pallet {seg['palletIndex']})"
        )

    print("\n------------\n")