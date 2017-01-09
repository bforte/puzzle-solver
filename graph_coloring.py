import random
# from a gist by eliasdorneles (https://github.com/eliasdorneles)

PALETTE = ('#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462',
           '#b3de69', '#fccde5', '#d9d9d9', '#bc80bd', '#ccebc5', '#ffed6f')

def generate_dot(graph, colors=None, palette=PALETTE):
    assert len(set(colors.values())) <= len(palette), (
        "Too few colors in the palette")

    edges = []
    for node, adjacents in graph.items():
        for n in adjacents:
            if not ((node, n) in edges or (n, node) in edges):
                edges.append((node, n))

    return colors

def try_coloring(graph, num_colors):
    """Try coloring a graph using given maximum number of colors
    >>> grafo = {
    ...     'A': ['B', 'C'],
    ...     'B': ['A'],
    ...     'C': ['A'],
    ... }
    >>> try_coloring(grafo, 1)
    >>> try_coloring(grafo, 2)
    {'A': 0, 'C': 1, 'B': 1}
    """
    assert num_colors > 0, "Invalid number of colors: %s" % num_colors
    colors = {}

    def neighbors_have_different_colors(nodes, color):
        return all(color != colors.get(n) for n in nodes)

    for node, adjacents in graph.items():

        found_color = False

        for color in range(num_colors):
            if neighbors_have_different_colors(adjacents, color):
                found_color = True
                colors[node] = color
                break

        if not found_color:
            return None

    return colors


def find_graph_colors(graph):
    for num_colors in range(1, len(graph)):
        colors = try_coloring(graph, num_colors)
        if colors:
            return colors

def get_random_palette():
    random_palette = list(PALETTE)
    random.shuffle(random_palette)
    return random_palette
