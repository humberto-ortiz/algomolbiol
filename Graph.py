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
        self.reverse=[]
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
                        self.reverse.append([])
            #   Fills in the adjacency list
		self.adjlist[self.a19merhash[source]].append(self.a19merhash[sink])
                self.reverse[self.a19merhash[sink]].append(self.a19merhash[source])
                
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
            self.reverse.append([])                
        #       Filling the adjacency list
        for i in range(0,len(EdgesList)):
            self.adjlist[self.a19merhash[EdgesList[i][0]]].append(self.a19merhash[EdgesList[i][1]])
            self.reverse[self.a19merhash[EdgesList[i][1]]].append(self.a19merhash[EdgesList[i][0]])
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

    def indegree(self, vertex):
        "Compute the indegree of the given VERTEX."
        return len(self.reverse[vertex])
    
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
    # for find all the vertex that can be reach from a given source vertex s.
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
        return visited
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # Breadth-First Search Reverse Method: This methos apply a breadth-first 
    # search  for find all the vertex that can be reach from a given source 
    # vertex s, but traversing the graph in reverse direction.
    # Input: 
    #   s <the source vertex.>
    # Output:
    #   visited <a list with the verxter that can be reach from the source.>
    #       
    # Last update(03/28/2012) 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def bfsr(self,s):
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
            for v in self.reverse[u]:
                if (color[v] == 'W'):
                    color[v] = 'G'
                    distance[v] = distance[u]+1
                    predecessor[v] = u
                    Q.append(v)
            color[u] = 'B'
            visited.append(u);
        return visited
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # Breadth-First Search Bi-directional Method: This methos apply a 
    # breadth-first search for find all the vertex that can be reach from a 
    # given source vertex s, but traversing the graph in both directions.
    # Input: 
    #   s <the source vertex.>
    # Output:
    #   visited <a list with the verxter that can be reach from the source.>
    #           
    # Last update(03/28/2012) 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def bfsbd(self,s):
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
            bothdirection = self.reverse[u]
            bothdirection.extend(self.adjlist[u])
            bothdirection = list(set(bothdirection))
            for v in bothdirection:
                if (color[v] == 'W'):
                    color[v] = 'G'
                    distance[v] = distance[u]+1
                    predecessor[v] = u
                    Q.append(v)
            color[u] = 'B'
            visited.append(u);
        return visited
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # Conected Components Method: This methos find the numeber of connected 
    # components in the graph.
    # 
    # Input: 
    #    <none>
    # Output:
    #   count <the number of connected componentes in the graph>
    #           
    # Last update(03/28/2012) 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    def cc(self):
        count = 0 
        color=[]
        def paint(v):
            color[v] = 'B'
            return
        for i in range(0,len(self.vertexhash)):
            color.append('W')
        while color.count('W'):
            visited = self.bfsbd(color.index('W'))
            map(paint,visited)
            count = count + 1
        return count

    def transposed(self):
        transposed = {i:[] for i in range(len(self.vertexhash))}
        for vertex in range(len(self.vertexhash)):
            for neighbor in self.adjlist[vertex]:
                transposed[neighbor].append(vertex)
        return transposed

    def finishorder(self, order):
        for v in set(order):
            order.remove(v)
        return order

    def scc(self):
        def dfs(vertex,neighbors,whole):
            visited = []
            def dfsaux(vertex):
                def dfsrec(vertex):
                    visited.append(vertex)
                    collect=[]
                    for neighbor in neighbors[vertex]:
                        if neighbor not in visited:
                            collect.append(neighbor)
                            collect += dfsrec(neighbor)
                            collect.append(neighbor)
                    return collect
                result = [vertex]
                result += dfsrec(vertex)
                result.append(vertex)
                if whole:
                    rest = list(set(neighbors.keys()).difference(result))
                    while rest:
                        result.append(rest[0])
                        result += dfsrec(rest[0])
                        result.append(rest[0])
                        rest = list(set(neighbors.keys()).difference(result))
                return result
            return dfsaux(vertex)
        adjacencies = {i:self.adjlist[i] for i in range(len(self.adjlist))}
        S = self.finishorder(dfs(0,adjacencies,True))
        transposed = self.transposed()
        components=0
        while S: 
            v=S.pop()
            component=list(set(dfs(v,transposed,False)))
            for vertex in component:
                if vertex in S:
                    S.remove(vertex)
                for adjacency in transposed.itervalues():
                    if vertex in adjacency:
                        adjacency.remove(vertex)
            components += 1
        return components
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
    Edges = [["two","zero"],["two","one"],["three","two"],["three","one"],["fourth","three"],["fourth","two"],["five","three"],["five","fourth"],["six","seven"],["seven","eigth"],["nine","ten"]];
    Components = [['c','g'],['g','f'],['f','g'],['h','h'],['d','h'],['c','d'],['d','c'],['g','h'],['a','b'],['b','c'],['b','f'],['e','f'],['b','e'],['e','a']]
   
    G.initWithEdges(list(Edges))
    print G.adjlist
    print G.reverse
    for v in G.vertexhash:
        print v
        print G.bfsbd(G.a19merhash[v])
    print G.cc()
    #G.createCytoscapeFile("test.sif");
    print "Outdegrees?", G.vertexDegrees()
    print "Indegrees", [G.indegree(vertex) for vertex in range(len(G.vertexhash))]
        
    print "Debug"
    #for vertex in G.a19merhash.values(): print vertex, G.adjlist[vertex],G.transposed()[vertex]
    print "Strongly Connected Components", G.scc()
    ## read a small test sequence database.
    #G.initWithSeqReads("test.fasta", "fasta")
    #print len(G.vertexhash)
    #print G.components()
