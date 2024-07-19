def getAX(mpimg, plt):
    # Memberikan background map
    img = mpimg.imread("map.png")
    img_height, img_width = img.shape[0], img.shape[1]
    fig, ax = plt.subplots(figsize=(img_width / 100, img_height / 100))
    ax.imshow(img, extent=[0, img_width, 0, img_height])
    return ax


def setup(nx, G, all_pos, pos, main_node, ax):
    nx.draw(
        G,
        all_pos,
        with_labels=False,
        node_color="black",
        node_size=16,
        font_size=8,
        ax=ax,
    )

    nx.draw_networkx_nodes(
        G, pos, nodelist=main_node, node_color="lightblue", node_size=128, ax=ax
    )
    nx.draw_networkx_labels(
        G,
        pos,
        labels=main_node,
        font_size=8,
        font_weight="bold",
        font_family="sans-serif",
        ax=ax,
    )


def k_shortest(nx, graph, start, end, k):
    paths = []
    used_edges = set()

    for _ in range(k):
        try:
            # Temukan jalur terpendek yang tidak menggunakan edge yang sudah digunakan
            shortest_path = nx.shortest_path(graph, start, end)
            paths.append(shortest_path)
            path_edges = list(zip(shortest_path[:-1], shortest_path[1:]))
            used_edges.update(path_edges)

            # Hapus edge yang sudah digunakan dari graf
            for edge in path_edges:
                if graph.has_edge(*edge):
                    graph.remove_edge(*edge)
        except nx.NetworkXNoPath:
            break

        # Restore edges for next iteration
        for edge in path_edges:
            if not graph.has_edge(*edge):
                graph.add_edge(*edge)

    return paths
