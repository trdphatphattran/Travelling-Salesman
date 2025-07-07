def tsp_solver(cities, distances, start=None):
    n = len(cities)
    best_path = []
    best_cost = float('inf')

    starts = [start] if start is not None else list(range(n))

    def dfs(path, cost):
        nonlocal best_path, best_cost
        if len(path) == n:
            total = cost + distances[path[-1]][path[0]]
            if total < best_cost:
                best_cost = total
                best_path = path[:]
            return
        for i in range(n):
            if i not in path:
                new_cost = cost + distances[path[-1]][i]
                if new_cost < best_cost:
                    dfs(path + [i], new_cost)

    for s in starts:
        dfs([s], 0)

    return best_path, best_cost
