import Graph
from copy import deepcopy
from collections import deque

def fleurys(G):

	#Reject the graph if its vertices are not all part of a single SCC.
	if G.scc() > 1:
		return "There is no Eulerian path for this graph."

	oddSource = -1         #to be used if at least one vertex has odd degree. 
	evenSource = -1        #to be used if all vertices have even degree.
	oddcount = 0           #for counting how many odd-degree vertices there are in the graph.
	
	#Check vertex degrees
	for v in range(0,len(G.adjlist)):
		degree = G.vertexDegree(v)
		if degree % 2 == 1:   #if degree of v is odd.
			oddcount += 1
			
			#Reject the graph if more than two vertices have odd degree.
			if oddcount > 2:
				return "There is no Eulerian path for this graph."

			#Initialize oddSource
			if oddSource == -1:
				oddSource = v

		#Store a vertex if it has even degree > 0.
		elif degree > 0:
			evenSource = v

	H = deepcopy(G) #make a copy of the graph for internal use.
	eulerPath = []  #to store the edges of the Eulerian path.

	#Count the total edges in the original graph.
	totalEdges = 0
	for i in H.adjlist:
		for j in i:
			totalEdges += 1

	#This function implements Fleury's traversal of the graph.
	def fleuryTraversal(source):

		current = source
		while len(eulerPath) < totalEdges:
			initSCCcount = H.scc()             #initial SCC count, before edge removal.
			
			adj = deque(H.adjlist[current])    #to store adjacencies of vertex currently being considered.
			remv_adj = adj.popleft()           #to store the adjacency just removed.
			first_remv = remv_adj              #to remember which was the first adjacency removal attempted.

			H.adjlist[current] = list(adj)     #update H.adjlist to reflect the removed edge.
			found = False                      #to keep track of whether we've found the Eulerian edge or not.

			while not found:
				if H.scc() == initSCCcount:   #greedily select for edges that do not increase the amount of SCCs when removed.
					eulerPath.append([current, remv_adj])
					current = remv_adj      #select the next vertex in the path
					found = True


				else:  #the removed edge increases the amount of SCCs.
					adj.append(remv_adj)
					remv_adj = adj.popleft()   #try the next adjacency.

					if remv_adj == first_remv:  #all edges would increase the amount of SCCs, so choose any one.
						eulerPath.append([current, remv_adj])
						current = remv_adj      #select the next vertex in the path
						found = True

	#Fleury's behavior is determined by oddcount.
	if oddcount == 0:
		fleuryTraversal(evenSource)  #choose any vertex with degree > 0 as source.

	else:
		fleuryTraversal(oddSource)  #choose a vertex with odd degree as source.

	return eulerPath



