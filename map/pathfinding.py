from map.hexutils import neighbors, hex_distance
import heapq

def a_star(tilemap, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        for nxt in neighbors(current):
            tile = tilemap.get_tile(nxt)
            if tile is None or not tile.passable:
                continue

            tentative_g = g_score[current] + tile.cost

            if tentative_g < g_score.get(nxt, float("inf")):
                came_from[nxt] = current
                g_score[nxt] = tentative_g
                priority = tentative_g + hex_distance(nxt, goal)
                heapq.heappush(open_set, (priority, nxt))

    return None

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
