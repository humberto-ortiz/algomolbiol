from Bio import SeqIO
#
# Class Description Comming Soon
#
class Graph:
    """A simple Graph class"""
    #    
    # This method create the empty members of the class
    #    
    def __init__(self):
        self.vertexhash = []
        self.a19merhash={}
        self.adjlist=[]
        
    #    
    # Method maps vertices to an index and viceversa, and fills and adjacency list
    # of overlapping vertices, using sequence reads from a file.
    #    
    def initWithSeqReads(self,file,type):
        k = 20      # Edge size, vertex size is k-1
    	for record in SeqIO.parse(file, type):
	    for i in range(0, len(record) - (k-2)):
	        edgeseq = str(record[i:i+k].seq)
		source = edgeseq[:k-1]
		sink = edgeseq[1:]
		for vertex in [source, sink]:
		    if vertex not in self.a19merhash:
                    #   For each new vertex, maps the vertex to a unique index and appends
                    #   an empty list to the adjacency list
		        self.a19merhash[vertex] = len(self.a19merhash)
			self.vertexhash.append(vertex)
			self.adjlist.append([])
            #   Fills in the adjacency list
		self.adjlist[self.a19merhash[source]].append(self.a19merhash[sink])

    def initWithFile(file):
        return 'not implemented yet'
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # This method initialize the graph members with the edges and vertex in 
    # the EdgesList.
    # Input:
    #   EdgesList is a list that contain a list for each edges in the graph.
    #     Example [["V1","V2"],["V2","V3"]] for the graph V1->V2->V3.
    # Output: none
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         
    def initWithEdges(self,EdgesList):
        for i in range(0,len(EdgesList)):
            for e in EdgesList[i]:
                if  not(e in self.a19merhash):
                    if (not(len(self.a19merhash))):
                        self.a19merhash[e] = 0
                        self.vertexhash.append(e)
                    else:
                        self.a19merhash[e] = len(self.a19merhash)
                        self.vertexhash.append(e)
        #       Filling the adjacency list with empty list
        for i in range(0,len(self.a19merhash)):
            self.adjlist.append([])                
        #       Filling the adjacency list
        for i in range(0,len(EdgesList)):
            self.adjlist[self.a19merhash[EdgesList[i][0]]].append(self.a19merhash[EdgesList[i][1]])
    #
    # Return a list with the degree of each vertex
    #                
    def vertexDegrees(self):
        degrees = [];
        for i in range(0,len(self.adjlist)):
            degrees.append(len(self.adjlist[i]))
        return degrees
    
    #
    # Return a the degree of the input vertex
    #                
    def vertexDegree(self,vertex):
        return len(self.adjlist[vertex])
    
    #
    # Create a file tha can be imported to cytoscape for visualise the graph
    #                
    def createCytoscapeFile(self,filepath):
        OutFile = open(filepath,'w')
        for vout in range(0,len(self.adjlist)):
            for vin in self.adjlist[vout]:
                OutFile.write(self.vertexhash[vout]+" predecessor "+self.vertexhash[vin]+"\n") 
        OutFile.close()
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # Breadth-First Search Method: This methos apply a breadth-first search 
    # for find all the vertex that canbe reach from a given source vertex s.
    # Input: 
    #   s <the source vertex.>
    # Output:
    #   visited <a list with the verxter that can be reach from the source.>
    #       
    # Last update(03/28/2012) 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def bfs(self,s):
        color=[]
        distance=[]
        predecessor=[]
        visited = []        
        for i in range(0,len(self.vertexhash)):
            color.append('W')
            distance.append(())
            predecessor.append('NIL')
        color[s] = 'G'
        distance[s] = 0
        predecessor[s] = 'NIL'
        Q = []
        Q.append(s)
        while (len(Q) != 0):
            u = Q.pop(0)
            for v in self.adjlist[u]:
                if (color[v] == 'W'):
                    color[v] = 'G'
                    distance[v] = distance[u]+1
                    predecessor[v] = u
                    Q.append(v)
            color[u] = 'B'
            visited.append(u);
        return visited#[color,distance,predecessor]
    def components(self):
        def known(here):
            visited=[]
            def knownaux(vertices, visited):
                neigbours=[]
                for vertex in vertices:
                    for neighbour in self.adjlist[vertex]:
                        if neighbour not in visited:
                            neighbours.append(neighbour)
                if neighbours:
                    return knownaux(neighbours, visited.append(neighbours))
                else:
                    return visited
            return knownaux([here],visited)
        def componentaux(vertices):
            if vertices:
                return 1+componentaux(list(set(vertices).difference(known(vertices[0]))))
            else:
                return 0
        return componentaux(self.vertexhash)

# # # # # # # # # # # # # # # # # # # # # # # # # # 
#   _____        _     ______                     #
#  |_   _|      | |   |___  /                     #
#    | | ___ ___| |_     / /   ___  _ __   ___    # 
#    | |/ _ | __| __|   / /   / _ \| '_ \ / _ \   #
#    | |  __|__ \ |_  ./ /___| (_) | | | |  __/   #
#    \_/\___|___/\__| \_____/ \___/|_| |_|\___|   #
# # # # # # # # # # # # # # # # # # # # # # # # # # 

if __name__ == '__main__':
    G = Graph()
    Edges = [["two","zero"],["two","one"],["three","two"],["three","one"],["fourth","three"],["fourth","two"],["five","three"],["five","fourth"]];
    G.initWithEdges(list(Edges))
    for v in G.vertexhash:
        print G.bfs(G.a19merhash[v])

    G.createCytoscapeFile("test.sif");
    print G.vertexDegrees()

    ## read a small test sequence database.
    G.initWithSeqReads("test.fasta", "fasta")
    print len(G.vertexhash)
    print G.components()
