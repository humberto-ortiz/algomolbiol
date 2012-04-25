import Graph
from copy import deepcopy
from collections import deque

def fleurys(G):

	#Reject the graph if its vertices are not all part of a single CC.
	if G.cc() > 1:
		return "There is no Eulerian path for this graph.1"

	oddSource = -1         #to be used if at least one vertex has odd degree. 
	evenSource = -1        #to be used if all vertices have even degree.
	oddcount = 0           #for counting how many odd-degree vertices there are in the graph.
	
	#Check vertex degrees
	for v in range(0,len(G.adjlist)):
		degree = abs(G.vertexDegree(v) - G.indegree(v))
		if degree == 1:   #if v is semi-balanced.
			oddcount += 1
			
			#Reject the graph if more than two vertices have odd degree.
			if oddcount > 2:
				return "There is no Eulerian path for this graph.2"

			#Initialize oddSource
			if oddSource == -1:
				oddSource = v

		#Store a balanced vertex that will be used as source if all vertices are balanced.
		elif evenSource == -1 and degree == 0:
			evenSource = v

		#Reject the graph if any vertex has a difference between out and in degree greater than 1.
		elif degree > 1:
			return "There is no Eulerian path for this graph.3"

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
			initCCcount = H.cc()             #initial CC count, before edge removal.

			adj = deque(H.adjlist[current])    #to store adjacencies of vertex currently being considered.
			remv_adj = adj.popleft()           #to store the adjacency just removed.
			first_remv = remv_adj              #to remember which was the first adjacency removal attempted.

			H.adjlist[current] = list(adj)     #update H.adjlist to reflect the removed edge.
			found = False                      #to keep track of whether we've found the Eulerian edge or not.

			while not found:
				if H.cc() == initCCcount:   #greedily select for edges that do not increase the amount of CCs when removed.
					eulerPath.append([current, remv_adj])
					current = remv_adj      #select the next vertex in the path
					found = True


				else:  #the removed edge increases the amount of CCs.
					adj.append(remv_adj)
					remv_adj = adj.popleft()   #try the next adjacency.

					if remv_adj == first_remv:  #all edges would increase the amount of CCs, so choose any one.
						eulerPath.append([current, remv_adj])
						current = remv_adj      #select the next vertex in the path
						found = True

	#Fleury's behavior is determined by oddcount.
	if oddcount == 0:
		fleuryTraversal(evenSource)  #choose any vertex with degree > 0 as source.

	else:
		fleuryTraversal(oddSource)  #choose a vertex with odd degree as source.

	return eulerPath



