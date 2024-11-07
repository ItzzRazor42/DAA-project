import sys

class Graph:

    def __init__(self):
        # Start with an empty adjacency matrix and empty node mapping
        self.V = 0
        self.graph = []
        self.node_mapping = {}

    def add_node(self, node: str):
        if node not in self.node_mapping:
            # Map node name to an index
            self.node_mapping[node] = self.V
            self.V += 1
            
            # Resize the adjacency matrix to accommodate the new node
            for row in self.graph:
                row.append(0)
            self.graph.append([0] * self.V)

    def add_edge(self, node1: str, node2: str, weight: int):
        # Add nodes if they do not already exist
        self.add_node(node1)
        self.add_node(node2)
        
        # Get indices of the nodes from the mapping
        index1 = self.node_mapping[node1]
        index2 = self.node_mapping[node2]
        
        # Add the weight to the adjacency matrix
        self.graph[index1][index2] = weight
        self.graph[index2][index1] = weight  # If the graph is undirected

    def printSolution(self, dist, src, end):
        print(f"Shortest distance from {src} to {end} is {dist[self.node_mapping[end]]}")

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        min_index = -1

        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, src, end):
        if src not in self.node_mapping or end not in self.node_mapping:
            print("One or both of the nodes do not exist in the graph.")
            return
        
        src_index = self.node_mapping[src]
        end_index = self.node_mapping[end]

        dist = [sys.maxsize] * self.V
        dist[src_index] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True

            if x == end_index:
                break

            for y in range(self.V):
                if self.graph[x][y] > 0 and not sptSet[y] and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist, src, end)


# Driver code
if __name__ == "__main__":
    g = Graph()
    adding: bool = True
    options = ["Y", "y", "Yes", "yes"]
    while adding:
        first_node: str = str(input("Input First Node Label: "))
        second_node: str = str(input("Input Second Node Label: "))
        weight: int =  int(input("Input Weight From First Node to Second Node: "))
        g.add_edge(first_node.lower(), second_node.lower(), weight)
        breakOut:str = str(input("Add More Nodes? (Y/N): "))
        if breakOut.lower() not in options:
            adding = False
            
    print("Search Shortest Path\n")

    # Specify start and end nodes
    start_node = str(input("Enter the start node: "))
    end_node = str(input("Enter the end node: "))
    
    g.dijkstra(start_node.lower(), end_node.lower())