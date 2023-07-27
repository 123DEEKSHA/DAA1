def knapsack_max_profit(weights,cost,capacity):
    num_items =len(weights)
    table = [[0]*(capacity+1)for _ in range(num_items+1)]
    for i in range(1,num_items + 1):
        for j in range(1,capacity + 1):
            if weights[i-1]<=j:
                table[i][j]=max(costs[i-1]+table[i-1] [j-weights[i-1]],table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    selected_items=[]
    total_weights=capacity
    for i in range(num_items,0,-1):
        if table[i] [total_weights]!=table[i-1][total_weights]:
            selected_items.append(i-1)
            total_weights -=weights[i-1]
    return table[num_items][capacity],selected_items

weights=[2,3,4,5]
costs=[10,20,30,40]
capacity=10

max_profit,selected_items=knapsack_max_profit(weights,costs,capacity)

print("maximum profit:",max_profit)
print("selected coffee beans (index):",selected_items)
print("selected coffee beans (weights):",[weights[i] for i in selected_items])
print("selected coffee beans (cost):",[costs[i] for i in selected_items])
        
//maximum profit: 70
selected coffee beans (index): [3, 1, 0]
selected coffee beans (weights): [5, 3, 2]
selected coffee beans (cost): [40, 20, 10]