import collections

def breadth_first_search(graph, root):
    #take two data structure one is queue for inputting all vertices
    #and one set for visited vertices
    
    queue = collections.deque([root])
    visited_vertices = set()
    #input the root as the first visited vertex
    visited_vertices.add(root)
    
    while queue:
        #popleft is a method of queue module to pop the left element(head) of queue 
        vertex = queue.popleft()
        print(queue)
        #neighbour is the values of each key in the dict "graph"
        #that means for key/vertex 0 the value/neighbor will be 1,2
        for neighbor in graph[vertex]:
            
            #check if the visited vertex is already in the queue or not:
            if neighbor not in visited_vertices: 
                visited_vertices.add(neighbor) 
                queue.append(neighbor)
    return visited_vertices



                
if __name__ == '__main__':

    #keys of the dictionary are the vertex and
    #value(list) are the adjucent nodes of that vertex
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2,4], 4:[4,0]}

    #calling the function and passing the argument "graph" and it's root '0"
    #when you are passing the root arugument make sure that
    #there is at least a single path
    #connected with every node

    result = breadth_first_search(graph,0)
    print("Visited Vertices:",result)
