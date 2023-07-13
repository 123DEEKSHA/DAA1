def dijkstra(graph,start):
    distances={node:float('inf')for node in graph}
    distances[start]=0
    heap=[(0,start)]
    
    while heap:
        current_dist,current_node=heapq.heappop(heap)
        if current_dist>distances[current_node]:
            continue
        for neighbor,weight in graph[current_node].item():
            distance=current_dist+weight
            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(heap,(distance,neighbor))
    return distances
def find_optimal_route(graph,start,destination):
    distances=dijkstra(graph,start)
    if distances[destination]==float('inf'):
        return None
    route=[]
    node=destination
    
    while node!=start:
        route.append(node)
        neighbors=graph[node]
        min_distance=float('inf')
        next_node=None
        for neighbor,weight in neighbors.items():
            if distances[neighbor]+weight==distances[node] and distances[neighbor]<min_distance:
                min_distance=distances[neighbor]
                next_node=neighbor
            if next_node is none or next_node in route:
                return none
            node=next_node
            
            route.append(start)
            route.reverse()
            return route
}

start_location='A'
destination_loation='E'
    
optimal_route=find_optimal_route(graph,start_location,destination_location)
    
if optimal_route is none:
    print("no valid route exits from the start to the destination.")
else:
    print("optimal route:",'->'.join(optimal_route))
            
                                     
    
            