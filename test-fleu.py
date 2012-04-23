import Graph
import Fleu

E = [[0,1],[1,2],[2,0]]
G = Graph.Graph()
G.initWithEdges(list(E))


for v in G.vertexhash:
    print v, G.adjlist[v], G.reverse[v]

print "Connected components:", G.cc()

for v in G.vertexhash:
    print v, G.adjlist[v], G.reverse[v]
    
print "Fleury's", Fleu.fleurys(G)

for v in G.vertexhash:
    print v, G.adjlist[v], G.reverse[v]
