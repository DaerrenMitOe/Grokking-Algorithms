graph = {}

graph["start"] = {}
graph["start"]["a"] = 10

graph["a"] = {}
graph["a"]["c"] = 20

graph["b"] = {}
graph["b"]["a"] = 1

graph["c"] = {}
graph["c"]["fin"] = 30
graph["c"]["b"] = 1

graph["fin"] = {}


infinity = float("inf")
costs = {}

costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs["fin"] = infinity


parents = {}

parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == "__main__":
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    print(costs)
