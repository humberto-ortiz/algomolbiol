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
    #
    #    
    def initWithSeqReads(file,type):
        return 'not implemented yet'
    #
    #
    #    
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
    # Create a file tha can be imported to cytoscape for visualise the graph
    #                
    def createCytoscapeFile(self,filepath):
        #       Will print in standar output, but when finished to the filepath
        for vout in range(0,len(self.adjlist)):
            for vin in self.adjlist[vout]:
                print self.vertexhash[vout]," predecessor ",self.vertexhash[vin]
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # Breadth-First Search Method: This methos apply a breadth-first search 
    # for find all the vertex that canbe reach from a given source vertex s.
    # Input: 
    #   s the source vertex
    # Output:
    #   [color,distance,predecessor]
    #       color is a list with labels in the nodes that can be reached 
    #        from s.
    #             'B' for visited reachable.
    #             'W' not visited not reachable.
    #       distance is a list with distance of the index vertex to the 
    #        source () means infinity.
    #       predecessor is a list with the predecessor of the index vertex.
    #        NIL if no predecessor.
    # Last update(03/28/2012) 
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    def bfs(self,s):
        color=[]
        distance=[]
        predecessor=[]
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
        return [color,distance,predecessor]


# # # # # # # # # # # # # # # # # # # # # # # # # # 
#   _____        _     ______                     #
#  |_   _|      | |   |___  /                     #
#    | | ___ ___| |_     / /   ___  _ __   ___    # 
#    | |/ _ | __| __|   / /   / _ \| '_ \ / _ \   #
#    | |  __|__ \ |_  ./ /___| (_) | | | |  __/   #
#    \_/\___|___/\__| \_____/ \___/|_| |_|\___|   #
# # # # # # # # # # # # # # # # # # # # # # # # # # 

G = Graph()
Edges = [["two","zero"],["two","one"],["three","two"],["three","one"],["fourth","three"],["fourth","two"],["five","three"],["five","fourth"]];
G.initWithEdges(list(Edges))
for v in G.vertexhash:
    print G.bfs(G.a19merhash[v])
G.createCytoscapeFile("dummy")
