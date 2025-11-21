print

import random
class Graph():
    
    def __init__(self):
     self.vertecis=[]  
     self.adjacencies=[] 
     self.stack=[]
     self.queue=[]
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
         
    def add_edge(self,Ver1,Ver2):  # add edge between Vertex1 and Vertex 2
        
        index_Ver1=self.vertecis.index(Ver1)
        index_Ver2=self.vertecis.index(Ver2)

        if self.check_validity(Ver1,Ver2):
            if (Ver1,Ver2) not in self.adjacencies and (Ver1,Ver2) not in self.adjacencies:
             self.adjacencies.append((index_Ver1,index_Ver2))
            else :return
            
    def findadjacent(self,index): # self.adjencies=[(1,3),(5,4),(4,1)]
        addjacents=[] 
        for (a,b) in self.adjacencies:
            if a == index :
                addjacents.append(self.vertecis[b])
            elif b==index:
                addjacents.append(self.vertecis[a])
            else: continue
        return addjacents
                          
    def depth_first(self,name):
        
        index=None
        if name in self.vertecis:
            index=self.vertecis.index(name)
        else:raise IndexError
        
        self.stack.append(name)  
        self.visited.append(name) # [A,B,"F"]
        addjacents=self.findadjacent(index) # ["B","H"]
        
        
        
        for i in addjacents : 
            if i not in self.visited: 
                    self.depth_first(i) 
    
    def breadth_first(self,name):
        
        index=None
        if name in self.vertecis:
            index=self.vertecis.index(name)
        else:raise IndexError
        
        addjacents=self.findadjacent(index) # ["B","C","D","E"]

        if name not in self.visited:
            
            self.queue.append(name)  
            self.visited.append(name) 
            self.visited.extend(addjacents)
            self.queue.extend(addjacents) #[A,B,C,D,E]
            
        def get_first_add(name):
            index=self.vertecis.index(name)
            addjacents=self.findadjacent(index) #[A,F]
            for i in addjacents:
                if i in self.visited:
                    continue
                else: return i
            
        
        temp=addjacents
        
        while  any(temp) : 
            local=[] 
            for i in temp :
                if i is not None :local.append(get_first_add(i))
                else:local.append(None)
            for i in local :
                if i is None:continue
                else:
                    self.queue.append(i) 
                    self.visited.append(i)
            temp=local
            
        return self.queue

    def minimumSpanningTree(self, start):
        
        if start not in self.vertecis:
            raise IndexError("Start vertex not found")

        # Create new graph and add all vertices (so add_edge works by name)
        mst = Graph()
        for v in self.vertecis:
            mst.add_Vertex(v)

        visited = set()

        def dfs(u):
            visited.add(u)
            u_index = self.vertecis.index(u)
            for v in self.findadjacent(u_index):
                if v not in visited:
                    # add edge (u, v) to MST and continue DFS
                    mst.add_edge(u, v)
                    dfs(v)

        dfs(start)
        return mst
            
        
            
            
               
            
    
         
                    
            
        
        
        
vv=Graph()

#adding Vertex
vv.add_Vertex("A")
vv.add_Vertex("B")
vv.add_Vertex("C")
vv.add_Vertex("D")
vv.add_Vertex("E")
vv.add_Vertex("F")
vv.add_Vertex("G")
vv.add_Vertex("H")
vv.add_Vertex("I")





vv.add_edge("A","B") 
vv.add_edge("A","C")
vv.add_edge("A","H")
vv.add_edge("A","E")
vv.add_edge("B","F")
vv.add_edge("F","H")
vv.add_edge("G","A")
vv.add_edge("C","H")

vv.depth_first("F")

print(vv.minimumSpanningTree("F").vertecis)

