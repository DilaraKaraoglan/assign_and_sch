# analysis/plots.py

import matplotlib.pyplot as plt


def plot_best_schedule(schedule, agents, save_path=None, dpi=300):

    fig, ax = plt.subplots(figsize=(16, 7))

    y_pos = {a["id"]: i for i, a in enumerate(agents)}

    for seg in schedule:

        aid = seg["agent"]
        start = seg["start"]
        end = seg["end"]
        duration = end - start

        item = seg["itemId"]

        if item == "RD":
            color = "#d9d9d9"
            label = "RD"
        else:
            color = plt.cm.tab20(hash(item) % 20)
            label = item

        ax.barh(
            y=y_pos[aid],
            width=duration,
            left=start,
            height=0.7,
            color=color,
            edgecolor="black",
            linewidth=1
        )

        ax.text(
            start + duration/2,
            y_pos[aid],
            label,
            ha="center",
            va="center",
            fontsize=8,
            color="white" if item != "RD" else "black"
        )

    ax.set_yticks(list(y_pos.values()))
    ax.set_yticklabels(
        [f"Agent {a['id']} ({a['type']})" for a in agents]
    )

    ax.set_xlabel("Time (seconds)")
    ax.set_title("Best Schedule")
    ax.grid(True, axis="x", linestyle="--", alpha=0.4)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=dpi, bbox_inches="tight")

    plt.show()


def plot_energy_report(human_energy_dict, makespan, avg_energy):

    agent_ids = sorted(human_energy_dict.keys())
    energies = [human_energy_dict[i] for i in agent_ids]

    fig, ax = plt.subplots(figsize=(10,6))

    bars = ax.bar(agent_ids, energies)

    ax.set_xlabel("Human Agent ID")
    ax.set_ylabel("Energy")
    ax.set_title("Human Energy Consumption")

    fig.text(
        0.5,
        -0.05,
        f"Makespan: {makespan:.2f} sec | Avg Energy: {avg_energy:.2f}",
        ha="center"
    )

    plt.tight_layout()
    plt.show()
    
def plot_completion_times(completion_dict, agents, makespan=None, save_path=None):

    agent_type_map = {a["id"]: a["type"] for a in agents}

    agent_ids = sorted(completion_dict.keys())
    completion_times = [completion_dict[i] for i in agent_ids]

    colors = [
        "steelblue" if agent_type_map[i] == "human" else "darkorange"
        for i in agent_ids
    ]

    fig, ax = plt.subplots(figsize=(12, 6))

    bars = ax.bar(agent_ids, completion_times,
                  color=colors,
                  edgecolor="black")

    ax.set_xlabel("Agent ID")
    ax.set_ylabel("Completion Time (sec)")
    ax.set_title("Completion Time per Agent")

    ax.set_xticks(agent_ids)
    ax.set_xticklabels([str(i) for i in agent_ids])

    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{height:.0f}",
            ha="center",
            va="bottom",
            fontsize=9
        )

    if makespan is not None:
        fig.text(
            0.5,
            -0.05,
            f"Makespan: {makespan:.2f} sec",
            ha="center",
            fontsize=11
        )

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()