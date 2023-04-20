class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = dict()
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for path in new_paths:
                    paths.append(path)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortestpath = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortestpath is None or len(sp) < len(shortestpath):
                        shortestpath = sp
        return shortestpath





if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris','Dubai'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto')
    ]
    route_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"

    # print(f"Path b/w {start} and {end}",route_graph.get_paths(start, end))
    print(f"Shortest b/w {start} and {end}", route_graph.get_shortest_path(start, end))
