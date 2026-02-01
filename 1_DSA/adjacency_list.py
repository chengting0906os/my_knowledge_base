class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


adj_mapping_list = {
    "A": [],
    "H": [],
}

adj_mapping = {}
edges = [["A", "B"], ["B", "C"], ["D", "E"]]

for src, dst in edges:
    if src not in adj_mapping:
        adj_mapping[src] = []
    if dst not in adj_mapping:
        adj_mapping[dst] = []
    adj_mapping[src].append(dst)
