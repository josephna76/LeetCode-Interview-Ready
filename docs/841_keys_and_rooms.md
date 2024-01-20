# 841. Keys and Rooms

## Problem Description

In the "Keys and Rooms" problem, you are given a list of rooms, where each room is initially locked except for room 0. Each room may contain a set of keys, and each key has the ability to unlock another room. The objective is to determine whether all the rooms can be unlocked and visited.

### Constraints

- The number of rooms is in the range `[2, 1000]`.
- Each room contains a distinct set of keys.
- No room contains a key to itself.

## Examples

### Example 1

**Input:** `rooms = [[1],[2],[3],[]]`  
**Output:** `true`  
**Explanation:**  
Starting from room 0, we can sequentially unlock and enter all other rooms, thus able to visit all rooms.

### Example 2

**Input:** `rooms = [[1,3],[3,0,1],[2],[0]]`  
**Output:** `false`  
**Explanation:**  
We cannot enter room 2 since the only key to this room is inside it. Hence, not all rooms are accessible.

## Approach

The problem can be tackled as a graph traversal issue, where each room is a node and each key represents an edge to another node (room). The solution involves:

- Implementing a Depth-First Search (DFS) starting from room 0.
- Keeping track of visited rooms to avoid revisits and endless loops.
- Checking if the number of visited rooms equals the total number of rooms in the end.

### Algorithm

1. Initialize a `visited` set to keep track of visited rooms.
2. Perform DFS starting from room 0.
   - If a room is visited for the first time, add it to the `visited` set.
   - Recursively visit rooms according to the keys found.
3. After DFS, compare the size of the `visited` set with the total number of rooms. If they are equal, return `true`; otherwise, `false`.

## Solution Code

The Python solution for this problem is as follows:

```python
def canVisitAllRooms(rooms):
    def dfs(room):
        if room not in visited:
            visited.add(room)
            for key in rooms[room]:
                dfs(key)

    visited = set()
    dfs(0)
    return len(visited) == len(rooms)
```

## Complexity Analysis

- **Time Complexity:** O(N), where N is the number of rooms. Each room is visited exactly once in the worst case.
- **Space Complexity:** O(N) for storing the visited set.
