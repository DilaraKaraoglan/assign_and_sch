import matplotlib
matplotlib.use("TkAgg")
from analysis.schedule_analysis import item_conflict_analysis, pretty_print_schedule,print_waiting_summary
from config import Config
from graph.warehouse_graph import build_warehouse_graph_for_distances
from data.build_data import build_item_map, build_pallets, build_agents, build_search_time
from routing.tsp_solver import PalletTSPSolver
from routing.time_and_compatibility import (
    pallet_agent_compatibility,
    build_time_matrix
)
from assignment.assignment_client import AssignmentClient
from assignment.scheduler_client import SchedulerClient
from scheduling.route_builder import RouteBuilder
from collections import defaultdict
import analysis.plots as plots
from utils.json_export import export_schedule
import os
from visualization.warehouse_visualizer import WarehouseVisualizer


def convert_assignment_matrix_to_dict(matrix):

    agent_trips = defaultdict(list)

    for pallet_idx, row in enumerate(matrix):
        for agent_idx, val in enumerate(row):
            if val == 1:
                agent_trips[agent_idx].append(pallet_idx)

    return dict(agent_trips)
def main():

    # Graph
    G, depot = build_warehouse_graph_for_distances(
        Config.NUM_AISLES,
        Config.AISLE_LENGTH,
        Config.N_LOCS,
        Config.OPENING_BETWEEN_AISLES,
        Config.AISLE_WIDTH,
        Config.DEPOT_DISTANCE
    )

    item_map = build_item_map()
    pallets = build_pallets()
    agents = build_agents()
    search_time = build_search_time()

    # TSP
    tsp_solver = PalletTSPSolver(G, depot, item_map)

    pallet_tsp = {
        idx: tsp_solver.solve(pallet)
        for idx, pallet in enumerate(pallets)
    }

    # Assignment input
    a_matrix = pallet_agent_compatibility(pallets, agents, item_map)
    t_matrix = build_time_matrix(pallets, pallet_tsp, agents, search_time)

    model_input = {
        "numItems": len(pallets),
        "numAgents": len(agents),
        "a": a_matrix,
        "t": t_matrix
    }

    assignment_client = AssignmentClient(Config.API_BASE_URL)
    assignment_result = assignment_client.solve(model_input)
    print("\n     ASSIGNMENT RESULT     \n")

    for agent in agents:
        aid = agent["id"]
        atype = agent["type"]

        print(f"Agent {aid} ({atype})")

        assigned = False
        for pallet_idx, row in enumerate(assignment_result["x"]):
            if row[aid] == 1:
                assigned = True
                print(f"  → Pallet {pallets[pallet_idx]['pallet_id']}")

        if not assigned:
            print("  (no assigned pallets)")

        print()
    
    print("Cmax:", assignment_result["cmax"])
    
    # Build scheduler input
    route_builder = RouteBuilder(G, depot, item_map)
    routes = route_builder.build_routes(
        pallets,
        pallet_tsp,
        assignment_result["x"]
    )

    assignment_dict = convert_assignment_matrix_to_dict(
        assignment_result["x"]
    )

    scheduler_input = {
        "agents": agents,
        "routes": routes,
        "assignment": assignment_dict,   
        "iterations": Config.SCHEDULER_ITERATIONS,
        "itemWeight": {
            item_id: values[3]
            for item_id, values in item_map.items()
        }
    }
    
    scheduler_client = SchedulerClient(Config.API_BASE_URL)
    scheduler_result = scheduler_client.solve(scheduler_input)
    best_schedule = scheduler_result["bestSchedule"]

    schedule = [
        {
            "agent": s["agentId"],
            "agentType": s["agentType"],
            "palletIndex": s["palletIndex"],
            "itemId": s["itemId"],
            "start": s["start"],
            "end": s["end"],
            "waitingTime": s.get("waitingTime", 0.0)
        }
        for s in best_schedule
    ]
    print("Makespan:", scheduler_result["makespan"])
    print("Average Human Energy:", scheduler_result["averageHumanEnergy"])

    plots.plot_best_schedule(schedule, agents)

    energy_dict = scheduler_result["humanEnergyPerAgent"]
    makespan = scheduler_result["makespan"]
    avg_energy = scheduler_result["averageHumanEnergy"]

    plots.plot_energy_report(energy_dict, makespan, avg_energy)
        
    def extract_completion_times(schedule):
        completion = {}
        for seg in schedule:
            aid = seg["agent"]
            completion[aid] = max(
                completion.get(aid, 0),
                seg["end"]
            )
        return completion

    completion_dict = extract_completion_times(schedule)

    plots.plot_completion_times(completion_dict, agents, makespan)
    

    pretty_print_schedule(best_schedule)
    
    print_waiting_summary(best_schedule)

    #item_conflict_analysis(best_schedule)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))

    export_schedule(
        base_dir,
        best_schedule,
        agents,
        makespan
    )
    items_for_plot = [
        (item_id, *values)
        for item_id, values in item_map.items()
    ]

    visualizer = WarehouseVisualizer(
        G,
        num_aisles=Config.NUM_AISLES,
        aisle_length=Config.AISLE_LENGTH,
        n_locs=Config.N_LOCS,
        aisle_width=Config.AISLE_WIDTH,
        opening_between_aisles=Config.OPENING_BETWEEN_AISLES,
    )

    visualizer.draw(
        items=items_for_plot,
        save_path="warehouse_layout.png"
    )
            
    print("Current Working Directory:", os.getcwd())    
    
    
if __name__ == "__main__":
    main()