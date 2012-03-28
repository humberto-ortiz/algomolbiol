#Testing Build
print "Hello World"

#testing classes
class Graph:
    """A simple Graph class"""
    vertexhash = []
    a19merhash={}
    adjlist=[]
    def __init__(self):
        self.vertexhash = []
        self.a19merhash={}
        self.adjlist=[]
    def initWithSeqReads(file,type):
        return 'not implemented yet'
    def initWithFile(file):
        return 'not implemented yet'
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

        
#       Fill the adjacency list with empty list
        for i in range(0,len(self.a19merhash)):
            self.adjlist.append([])                
#       Filling the adjacency list
        for i in range(0,len(EdgesList)):
            self.adjlist[self.a19merhash[EdgesList[i][0]]].append(self.a19merhash[EdgesList[i][1]])
                
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
#           for test and print the visited vertex
            print self.vertexhash[u]
        return [color,distance,predecessor]


G = Graph()
Edges = [["two","zero"],["two","one"],["three","two"],["three","one"],["fourth","three"],["fourth","two"],["five","three"],["five","fourth"]];
G.initWithEdges(list(Edges))
for v in G.vertexhash:
    print G.bfs(G.a19merhash[v])
