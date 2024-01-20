def canVisitAllRooms(rooms):
    def dfs(room):
        if room not in visited:
            visited.add(room)
            for key in rooms[room]:
                dfs(key)

    visited = set()
    dfs(0)
    return len(visited) == len(rooms)
