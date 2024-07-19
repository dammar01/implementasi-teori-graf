import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from setup import setup, k_shortest, getAX
from data import all_pos, all_edges, pos

# Membuat graf tidak berarah
G = nx.Graph()
G.add_edges_from(all_edges)
main_node = {node: node for node in pos}
ax = getAX(mpimg, plt)
setup(nx, G, all_pos, pos, main_node, ax)


# Contoh penggunaan: menemukan 3 jalur terpendek dari node 'A' ke node 'E'
start_node = "A"
end_node = "O"
k = 3

# Buat salinan graf untuk menemukan jalur unik
G_copy = G.copy()
path_unique = k_shortest(nx, G_copy, start_node, end_node, k)
print(f"{k} Jalur terpendek unik dari {start_node} ke {end_node}: {path_unique}")

# Menyoroti jalur opsi dengan warna biru
for i, path in enumerate(path_unique[1:], start=1):
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(
        G,
        all_pos,
        edgelist=path_edges,
        edge_color="b",
        width=2,
        ax=ax,
        label=f"Option Path {i}",
    )


# Menyoroti jalur terdekat dengan warna merah
if path_unique:
    shortest_path = path_unique[0]
    shortest_path_edges = list(zip(shortest_path, shortest_path[1:]))
    nx.draw_networkx_edges(
        G,
        all_pos,
        edgelist=shortest_path_edges,
        edge_color="r",
        width=2,
        ax=ax,
        label="Shortest Path",
    )

# Menampilkan plot
plt.legend()
plt.show()
