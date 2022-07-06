import collections
import networkx as nx
import matplotlib.pyplot as plt
import h5py as h5

class DirectedGraph:
    # Construct Directed Graph from List of Vertices and a List of pairs of vertices (Edges) using networkx
    def __init__(self, vertices, edges):
        self.vertices = vertices # List of vertices
        self.edges = edges # List of pairs of vertices (Edges)
        self.graph = nx.DiGraph() # Create a directed graph.
        self.graph.add_nodes_from(vertices) # Add the vertices to the graph.
        self.graph.add_edges_from(edges) # Add edges to the graph.
        self.out_degrees = self.graph.out_degree() # Get the out-degree of each vertex.
        self.in_degrees = self.graph.in_degree() # In-degree is the number of edges pointing towards a vertex.
        self.degree_sequence = sorted([d for n, d in self.graph.degree()], reverse=True) # Degree sequence of the graph (in descending order).
        self.degree_histogram = dict(self.graph.degree())
    
    # Print the number of vertices and edges
    def print_graph(self):
        print('Number of vertices:', len(self.vertices)) # Number of vertices
        print('Number of edges:', len(self.edges)) # Print the number of edges
        
    # Plot Graph - This can be used to validate if it is a directed graph
    def plot_graph(self):
        nx.draw(self.graph, with_labels=True) # Draw the graph
        plt.show() # Display the graph
        plt.savefig('graph_nodes_and_edges.png') # Save the graph as a PNG
    
    # Plot histogram of out-degrees of vertices.
    def plot_out_degrees(self):
        degree_sequence = sorted([d for n, d in self.out_degrees()], reverse=True)  # Degree sequence of the graph.
        degreeCount = collections.Counter(degree_sequence) # Count the number of each degree value in the sequence of degrees.
        deg, cnt = zip(*degreeCount.items()) # Unzip the degree and count values. The zip(*) syntax is used to unzip a list of tuples.

        fig, ax = plt.subplots() # Create a figure and axes object.
        plt.bar(deg, cnt, width=0.80, color='b') # Plot the degree distribution as a bar chart.
        plt.title("Out-Degree Histogram")
        plt.ylabel("Count")
        plt.xlabel("Degree")
        ax.set_xticks([d + 0.4 for d in deg]) # Set the x-axis ticks to be the degree values.
        ax.set_xticklabels(deg) # Set the x-axis tick labels to be the degree values.
        plt.show()
        # Save histogram as PNG
        plt.savefig('out_degree_histogram.png')
    
    # Serialize and deserialize the DirectedGraph to/from HDF5
    def serialize_to_hdf5(self, filename):
        with h5.File(filename, 'w') as f:
            f.create_group('vertices') # Create a group for the vertices.
            f.create_group('edges') # Create a group for the edges.
            [f.create_dataset('vertices/' + str(i), data=v) for i, v in enumerate(self.vertices)] # Create a dataset for each vertex.
            [f.create_dataset('edges/' + str(i), data=e) for i, e in enumerate(self.edges)] # Create a dataset for each edge.
            f.close() # Close the file. This is important to avoid memory leaks and other problems.


    # Deserialize the DirectedGraph from HDF5
    def deserialize_from_hdf5(self, filename):
        with h5.File(filename, 'r') as f:
            # vertices = [f['vertices/']]
            # edges = [f['edges/']]
            # print(vertices)
            # print(edges)
            vertices = f['vertices'].keys() # Get the keys of the vertices group. Keys are the vertex indices. Indices mean the order in which the vertices were added to the graph.
            edges = f['edges'].keys() # Get the keys of the edges group. Keys are the edge indices. Indices mean the order in which the edges were added to the graph.
            print('These are the vertices:', vertices)
            print('These are the edges:',edges)
            f.close() # Close the file. This is important to avoid memory leaks and to avoid file corruption.


# Testing purposes
# Generate random scale free directed graph
G = nx.scale_free_graph(150)

# Get the list of vertices and edges (required for the input to test the modules)
vertices = G.nodes()
edges = G.edges()

# Create a DirectedGraph object from the list of vertices and edges
directed_graph = DirectedGraph(vertices, edges)

# Print the number of vertices and edges
directed_graph.print_graph()

# Print the graph - Not required
directed_graph.plot_graph()

# Plot the histogram of out-degrees of vertices
directed_graph.plot_out_degrees()

# Test serialization
directed_graph.serialize_to_hdf5('directed.h5')

# Test deserialization
test_deserialization = directed_graph.deserialize_from_hdf5('directed.h5')
