
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = dict()
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = end


    def get_path(self, start, end, paths = []):
        paths = paths + [start]
        if start == end:
            return [paths]
        if start not in self.graph_dict:
            return None


routes = [
    ('Mumbai', 'Paris'),
    ('Paris', 'New York'),
    ('New York', 'Toronto')
]
route = Graph(routes)

start = 'Mumbai'
end = 'Mumbai'

print(f"Path {start} and {end}", route.get_path(start, end))