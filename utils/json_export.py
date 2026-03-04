# utils/json_export.py

import json
import os


def export_schedule(base_dir, best_schedule, agents, makespan):

    path = os.path.join(base_dir, "best_schedule.json")

    with open(path, "w") as f:
        json.dump({
            "best_schedule": best_schedule,
            "agents": agents,
            "deterministic_makespan": makespan
        }, f, indent=2)

    print("Schedule saved to:", path)