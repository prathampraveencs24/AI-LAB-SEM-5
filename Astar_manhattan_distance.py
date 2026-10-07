from heapq import heappush, heappop

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def h_value(state):
    # Manhattan Distance
    distance = 0

    for i in range(9):

        tile = state[i]

        if tile != 0:

            current_row, current_col = divmod(i, 3)

            goal_pos = goal.index(tile)
            goal_row, goal_col = divmod(goal_pos, 3)

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance

def neighbors(state):
    pos = state.index(0)
    row, col = divmod(pos, 3)

    result = []

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:

        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:

            new_pos = r * 3 + c
            new_state = list(state)

            new_state[pos], new_state[new_pos] = \
                new_state[new_pos], new_state[pos]

            result.append(tuple(new_state))

    return result

def print_state(state):
    print(state[:3])
    print(state[3:6])
    print(state[6:])

def astar(start):

    pq = []

    # Initial node
    g = 0
    h = h_value(start)
    f = g + h

    heappush(pq, (f, g, start, [start]))

    visited = set()

    while pq:

        f, g, state, path = heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        print("State:")
        print_state(state)

        print("g(n) =", g)
        print("h(n) =", h_value(state))
        print("f(n) = g(n) + h(n)")
        print("f(n) =", g, "+", h_value(state), "=", f)

        print("-------------------------")

        if state == goal:
            print("Goal reached!")
            return path

        for nxt in neighbors(state):

            if nxt not in visited:

                new_g = g + 1
                new_h = h_value(nxt)
                new_f = new_g + new_h

                print("Child:")
                print_state(nxt)

                print("g(n) =", new_g)
                print("h(n) =", new_h)
                print("f(n) = g(n) + h(n)")
                print("f(n) =", new_g, "+", new_h, "=", new_f)

                print("-------------------------")

                heappush(
                    pq,
                    (new_f, new_g, nxt, path + [nxt])
                )

# Initial state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

path = astar(start)

print("\nSOLUTION PATH:")

for state in path:
    print_state(state)
    print()