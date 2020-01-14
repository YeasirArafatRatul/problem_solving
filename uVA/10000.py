import collections

def longest_path(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    
    #if you print the whole set here it will make no sense.
    #cz set is not a properly indexed data structure
    for neighbor in graph[start]:
        if neighbor not in visited:
            #if the neighbor vertex is not in the visited set then call the function
            #this time start = neighbour
            depth_first_search(graph, neighbor, visited)
    return visited

if __name__ == "__main__":
    graph = {}
    while True:
        n = int(input())
        if n == 0:
            break
        start = int(input())
        for i in range(n):
            p,q = map(int, input().split())
            if p != 0 and q != 0:
                graph[p]= q
            else:
                longest_path(graph,start)
                break
                
            
        
