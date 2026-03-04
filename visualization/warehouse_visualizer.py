import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# =====================================================
# NODE POSITION GENERATOR
# =====================================================

def make_node_positions_for_layout(
    num_aisles,
    aisle_length,
    n_locs,
    aisle_width,
    opening_between_aisles,
    cross_aisle_width=3.0,
    include_middle_cross=True,
    middle_cross_width=3.0,
):

    middle_y = aisle_length / 2
    pitch = aisle_width + opening_between_aisles
    step_y = aisle_length / n_locs
    xs = [(a - 1) * pitch for a in range(1, num_aisles + 1)]

    pos = {}

    # ---------------- DEPOT ----------------
    depot_x = xs[0] - (aisle_width / 2 + opening_between_aisles * 1.2)
    depot_y = -cross_aisle_width / 2
    pos[("DEPOT", 0)] = (depot_x, depot_y)

    # ---------------- JUNCTIONS ----------------
    for a in range(1, num_aisles + 1):
        pos[(a, "Jb")] = (xs[a - 1], -cross_aisle_width / 2)
        pos[(a, "Jt")] = (xs[a - 1], aisle_length + cross_aisle_width / 2)
        pos[(a, "Jm")] = (xs[a - 1], middle_y)

    # ---------------- FINISH NODES ----------------
    finish_offset = 3.0

    pos[("FLEX", 0)] = (
        xs[2],
        aisle_length + cross_aisle_width/2 + finish_offset
    )

    pos[("FHUM", 0)] = (
        xs[10],
        aisle_length + cross_aisle_width/2 + finish_offset
    )

    # ---------------- CORRIDOR NODES ----------------
    mid_loc = n_locs // 2

    for a in range(1, num_aisles + 1):
        x = xs[a - 1]

        for p in range(1, n_locs + 1):

            if p == mid_loc:
                continue

            y = (p - 0.5) * step_y
            pos[(a, p, "C")] = (x, y)

    # ---------------- SHELF FACES ----------------
    for r in range(1, num_aisles):
        xL = xs[r - 1]
        xR = xs[r]

        x_center = (xL + xR) / 2
        offset = (xR - xL) * 0.15

        for p in range(1, n_locs + 1):
            y = (p - 0.5) * step_y

            pos[(r, p, "L")] = (x_center - offset, y)
            pos[(r, p, "R")] = (x_center + offset, y)

    return pos


# =====================================================
# VISUALIZER
# =====================================================

class WarehouseVisualizer:

    def __init__(
        self,
        G,
        num_aisles,
        aisle_length,
        n_locs,
        aisle_width,
        opening_between_aisles,
        cross_aisle_width=3.0,
        include_middle_cross=True,
        middle_cross_width=3.0,
    ):

        self.G = G
        self.num_aisles = num_aisles
        self.aisle_length = aisle_length
        self.n_locs = n_locs
        self.aisle_width = aisle_width
        self.opening_between_aisles = opening_between_aisles
        self.cross_aisle_width = cross_aisle_width
        self.include_middle_cross = include_middle_cross
        self.middle_cross_width = middle_cross_width

        self.pitch = aisle_width + opening_between_aisles
        self.middle_y = aisle_length / 2
        self.step_y = aisle_length / n_locs
        self.xs = [(a - 1) * self.pitch for a in range(1, num_aisles + 1)]

        self.pos = make_node_positions_for_layout(
            num_aisles,
            aisle_length,
            n_locs,
            aisle_width,
            opening_between_aisles,
            cross_aisle_width,
            include_middle_cross,
            middle_cross_width
        )

    # =================================================
    # DRAW PUBLIC
    # =================================================

    def draw(self, items=None, save_path=None, dpi=300):

        fig, ax = plt.subplots(figsize=(16, 5))

        self._draw_middle_cross(ax)
        self._draw_aisles(ax)
        self._draw_racks(ax)
        self._draw_edges(ax)
        self._draw_nodes(ax)

        if items:
            self._draw_items(ax, items)

        ax.set_title("Warehouse Graph")
        ax.set_aspect("equal")
        ax.axis("off")

        if save_path:
            fig.savefig(save_path, dpi=dpi, bbox_inches="tight")

        plt.show()

    # =================================================
    # INTERNAL DRAWING
    # =================================================

    def _draw_middle_cross(self, ax):

        if not self.include_middle_cross:
            return

        x_min = self.xs[0] - (self.aisle_width/2 + self.opening_between_aisles)
        x_max = self.xs[-1] + (self.aisle_width/2 + self.opening_between_aisles)

        ax.add_patch(Rectangle(
            (x_min, self.middle_y - self.middle_cross_width/2),
            x_max - x_min,
            self.middle_cross_width,
            facecolor="white",
            edgecolor="black",
            linewidth=2
        ))

    def _draw_aisles(self, ax):

        for x in self.xs:

            ax.add_patch(Rectangle(
                (x - self.aisle_width/2, 0),
                self.aisle_width,
                self.middle_y - self.middle_cross_width/2,
                facecolor="white",
                edgecolor="black",
                linewidth=1.5
            ))

            ax.add_patch(Rectangle(
                (x - self.aisle_width/2,
                 self.middle_y + self.middle_cross_width/2),
                self.aisle_width,
                self.aisle_length -
                (self.middle_y + self.middle_cross_width/2),
                facecolor="white",
                edgecolor="black",
                linewidth=1.5
            ))

    def _draw_racks(self, ax):

        for r in range(1, self.num_aisles):

            xL = self.xs[r - 1]
            xR = self.xs[r]
            rack_width = (xR - xL) - self.aisle_width
            rack_x = (xL + xR)/2 - rack_width/2

            ax.add_patch(Rectangle(
                (rack_x, 0),
                rack_width,
                self.middle_y - self.middle_cross_width/2,
                facecolor="#d0d0d0",
                edgecolor="black",
                linewidth=1
            ))

            ax.add_patch(Rectangle(
                (rack_x,
                 self.middle_y + self.middle_cross_width/2),
                rack_width,
                self.aisle_length -
                (self.middle_y + self.middle_cross_width/2),
                facecolor="#d0d0d0",
                edgecolor="black",
                linewidth=1
            ))
    
    def _is_walkable_edge(self, u, v):

        walk_nodes = {"C", "Jb", "Jt", "Jm"}

        if u[0] == "DEPOT" or v[0] == "DEPOT":
            return True

        return (u[-1] in walk_nodes) and (v[-1] in walk_nodes)


    def _is_approach_edge(self, u, v):

        types = {u[-1], v[-1]}
        return ("C" in types) and (("L" in types) or ("R" in types))
    def _draw_edges(self, ax):

        for u, v in self.G.edges():

            if u not in self.pos or v not in self.pos:
                continue

            x1, y1 = self.pos[u]
            x2, y2 = self.pos[v]

            # -------------------------
            # FINISH EDGES (ÖZEL)
            # -------------------------
            if (
                (u == (3, "Jt") and v == ("FLEX", 0)) or
                (v == (3, "Jt") and u == ("FLEX", 0)) or
                (u == (11, "Jt") and v == ("FHUM", 0)) or
                (v == (11, "Jt") and u == ("FHUM", 0))
            ):
                ax.plot(
                    [x1, x2],
                    [y1, y2],
                    color="blue",
                    linewidth=2.5,
                    zorder=5
                )
                continue

            # -------------------------
            # WALKABLE EDGE
            # -------------------------
            if self._is_walkable_edge(u, v):

                ax.plot(
                    [x1, x2],
                    [y1, y2],
                    color="black",
                    linewidth=1.3,
                    alpha=0.7,
                    zorder=1
                )

            # -------------------------
            # APPROACH EDGE
            # -------------------------
            elif self._is_approach_edge(u, v):

                lower = self.middle_y - self.middle_cross_width/2
                upper = self.middle_y + self.middle_cross_width/2

                if (lower <= y1 <= upper) or (lower <= y2 <= upper):
                    continue

                ax.plot(
                    [x1, x2],
                    [y1, y2],
                    linestyle="--",
                    linewidth=1,
                    color="black",
                    alpha=0.6,
                    zorder=2
                )

    def _draw_nodes(self, ax):

        lower = self.middle_y - self.middle_cross_width/2
        upper = self.middle_y + self.middle_cross_width/2

        for n in self.G.nodes():

            if n not in self.pos:
                continue

            x, y = self.pos[n]

            # DEPOT
            if n[0] == "DEPOT":
                ax.scatter([x], [y], s=120, marker="s", color="black")
                ax.text(x, y - 0.6, "DEPOT", ha="center")

            # FINISH NODES
            elif n == ("FLEX", 0):
                ax.scatter([x], [y], s=140, color="blue")
                ax.text(x, y + 0.6, "FLEX_FINISH", ha="center")

            elif n == ("FHUM", 0):
                ax.scatter([x], [y], s=140, color="red")
                ax.text(x, y + 0.6, "HUMAN_FINISH", ha="center")

            # JUNCTION NODES (her zaman çiz)
            elif isinstance(n, tuple) and n[-1] in {"Jb", "Jm", "Jt"}:
                ax.scatter([x], [y], s=25, color="orange")

            # CORRIDOR NODES (middle cross aisle hariç)
            elif isinstance(n, tuple) and n[-1] == "C":

                if lower <= y <= upper:
                    continue  # middle cross aisle içindeyse çizme

                ax.scatter([x], [y], s=10, color="orange")

    def _draw_items(self, ax, items):

        for item in items:

            item_id, r, p, face, _ = item
            node = (r, p, face.upper())

            if node not in self.pos:
                continue

            x, y = self.pos[node]

            ax.scatter([x], [y], s=120, zorder=5)
            ax.text(x, y, f" {item_id}", fontsize=8, va="center")