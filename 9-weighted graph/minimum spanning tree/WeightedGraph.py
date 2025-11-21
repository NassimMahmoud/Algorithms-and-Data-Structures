from MinHeap import MinHeap

class WeightedGraph():
 
    def __init__(self):
        self.vertecis=[]  # [vetex1,vertex2,...]
        self.adjacencies=[] # [(1,2,W1),(2,3,W2),...]
        self.visited=[]
     
    def add_Vertex(self,name):
        if name in self.vertecis:
            return
        else :
         self.vertecis.append(name)
        
    def check_validity(self,Ver1,Ver2):
        if Ver1 in self.vertecis and Ver2 in self.vertecis and Ver1 != Ver2:
            return True
        else :
            raise IndexError
         
    def add_edge(self,Ver1,Ver2,Weight):  # add edge between Vertex1 and Vertex 2
        
        index_Ver1=self.vertecis.index(Ver1)
        index_Ver2=self.vertecis.index(Ver2)

        if self.check_validity(Ver1,Ver2):
            if (Ver1,Ver2,Weight) not in self.adjacencies and (Ver2,Ver1,Weight) not in self.adjacencies:
             self.adjacencies.append((index_Ver1,index_Ver2,Weight))
            else :return
            
    def hasEdge(self, Ver1, Ver2):
        
        for (a,b,W) in self.adjacencies:
            if (Ver1,Ver2)==(a,b) or (Ver1,Ver2)==(b,a):return True
            
        else:return False
        
    def get_edge_weight(self,Ver1,Ver2):
        for (a,b,W) in self.adjacencies:
            if (Ver1,Ver2)==(a,b) or (Ver1,Ver2)==(b,a):return W
            
    def findadjacent(self,index): # self.adjencies=[(1,3,w1),(5,4,w2),(4,1,w2)]
        addjacents=[] 
        for (a,b,Weight) in self.adjacencies:
            if a == index :
                addjacents.append((Weight,a,b))
            elif b==index:
                addjacents.append((Weight,a,b))
            else: continue
        return addjacents
    
    def nVertices(self):
        return len(self.vertecis)
    
    def minimumspannigtree(self, start):
        
        """Prim's algorithm to find Minimum Spanning Tree"""
        
        if start not in self.vertecis: 
            raise IndexError("Start vertex not in graph")
        
        # 1. Initialization
        tree = WeightedGraph() # The resulting MST
        # Set to keep track of vertices already included in the MST
        in_mst = {start}
        tree.add_Vertex(start)
        
        # Min heap to store edges (weight, vertex_to, vertex_from)
        # The key is the weight, the other elements are for context
        edges = MinHeap() 
        
        # 2. Add all initial edges from the start vertex to the heap
        # find all adjencecies and add them to the heap 
        add_to_start=self.findadjacent(self.vertecis.index(start)) #[(w1,a,b),(w2,a,b)]
        
        for w,a,b in add_to_start:
            edges.insert(w, a, b)
            
        # 3. Main loop: Process edges until all vertices are in the MST
        # We stop when the tree has all vertices, or the heap is empty (disconnected graph)
        while not edges.isEmpty() and len(in_mst) < len(self.vertecis):
            

            # Get the minimum weight edge (weight, to_vertex, from_vertex)
            weight, u, v = edges.remove_min() 
            
            u=self.vertecis[u]
            v=self.vertecis[v]
            to_insert = u if u not in in_mst else v # to insert v
            
            
            # This edge leads to a vertex (u) NOT yet in the MST.
            if to_insert not in in_mst:
                # 4. Add the new vertex and the edge to the MST
                in_mst.add(to_insert)
                tree.add_Vertex(to_insert)
                tree.add_edge(v,u, weight) # v is the vertex ALREADY in MST
                
                # 5. Add all edges from the newly added vertex (u) to the heap
                for w,a,b in self.findadjacent(self.vertecis.index(to_insert)): 
                    # Only consider edges leading to vertices not yet in the MST
                    if self.vertecis[a] and self.vertecis[b] in in_mst:
                        continue
                    else : edges.insert(w,a, b)

             
        return tree
    
    
    
    
cc=WeightedGraph()

cc.add_Vertex("A")
cc.add_Vertex("B")
cc.add_Vertex("C")
cc.add_Vertex("D")
cc.add_Vertex("E")
cc.add_Vertex("F")
cc.add_Vertex("G")


cc.add_edge("A","B",3)
cc.add_edge("B","C",8)
cc.add_edge("C","A",29)
cc.add_edge("C","D",2)
cc.add_edge("D","E",2)
cc.add_edge("E","F",4)
cc.add_edge("C","G",8)

print(cc.minimumspannigtree("D").vertecis)

