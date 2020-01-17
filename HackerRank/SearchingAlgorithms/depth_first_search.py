def depth_first_search(graph, start, visited=None):
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
graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

result = depth_first_search(graph, '0')


#this may give you different answers each time, the reason behind it is
#set has no index value,so it retrieves  the data randomly
#but all the answers are correct
