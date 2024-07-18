import networkx as nx
import matplotlib.pyplot as plt

# Membuat graf tidak berarah
G = nx.Graph()

# Menambah simpul
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

# Menambah tepi
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "A")
G.add_edge("C", "D")
G.add_edge("D", "A")
G.add_edge("E", "C")

# Visualisasi graf
nx.draw(G, with_labels=True)
plt.show()
