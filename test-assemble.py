import Graph

G = Graph.Graph()

G.initWithSeqReads("tiny.fasta", "fasta")


eulerian =  G.fleurys()

seq = ""

firstseq = G.vertexhash[eulerian[0][0]]

seq += firstseq

secondseq = G.vertexhash[eulerian[0][1]][-1]

seq += secondseq

for vertexpair in eulerian[1:]:
    seq += G.vertexhash[vertexpair[1]][-1]

print seq

#for v in G.vertexhash:
#    print v, G.adjlist[G.a19merhash[v]], G.reverse[G.a19merhash[v]]

