# 散列表_1 -- 原始有向无环图
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['end'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = {}

# 散列表_2 -- 开销图（存储从起点到每个节点的开销）（会更新）
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = infinity

# 散列图_3 -- 存储父节点（会更新）
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

# 需要一个数组记录处理过的节点
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < cost[n]:
            cost[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)