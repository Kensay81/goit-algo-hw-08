import heapq

def minimum_cost(cables):
    if not cables:
        return 0
    
    # Convert the list into a heap
    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        # Extract the two shortest cables
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Calculate the cost to connect them
        cost = first + second
        total_cost += cost
        
        # Insert the combined cable back into the heap
        heapq.heappush(cables, cost)
        
    return total_cost

# Example usage
cables1 = [4, 3, 2, 6]
cables2 = [1, 2, 5, 10, 35, 89]

print(f"Minimum cost to connect cables {cables1}: {minimum_cost(cables1)}")
print(f"Minimum cost to connect cables {cables2}: {minimum_cost(cables2)}")
