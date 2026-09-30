# 8-Puzzle Problem using Depth-First Search (DFS)

GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)


def print_board(state):
    """Display the puzzle. 0 is shown as a blank."""

    for i in range(0, 9, 3):
        row = []

        for j in range(i, i + 3):
            if state[j] == 0:
                row.append(" ")
            else:
                row.append(str(state[j]))

        print("| " + " | ".join(row) + " |")

    print()


def get_neighbors(state):
    """Generate all possible moves."""

    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    # Up, Down, Left, Right
    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, move in moves:

        new_row = row + dr
        new_col = col + dc

        # Check valid position
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append((tuple(new_state), move))

    return neighbors


def dfs(state, path, visited):
    """Depth-First Search."""

    # Goal test
    if state == GOAL_STATE:
        return path

    # Mark current state as visited
    visited.add(state)

    # Explore neighbors
    for next_state, move in get_neighbors(state):

        if next_state not in visited:

            result = dfs(
                next_state,
                path + [move],
                visited
            )

            if result is not None:
                return result

    return None


def apply_move(state, move):

    for next_state, next_move in get_neighbors(state):

        if next_move == move:
            return next_state

    return state


def display_solution(start_state, solution):

    current_state = start_state

    print("\nInitial State:")
    print_board(current_state)

    for step, move in enumerate(solution, 1):

        current_state = apply_move(current_state, move)

        print("Step", step, ":", move)
        print_board(current_state)


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

print("===================================")
print("     8-PUZZLE USING DFS")
print("===================================")

# 0 represents the blank internally
start_state = (
    1, 2, 3,
    4, 5, 0,
    7, 8, 6
)

print("\nInitial Puzzle:")
print_board(start_state)

print("Goal Puzzle:")
print_board(GOAL_STATE)

# Solve using DFS
visited = set()

solution = dfs(
    start_state,
    [],
    visited
)

# Display result
if solution is not None:

    print("Solution Found!")
    print("Moves:", solution)
    print("Number of moves:", len(solution))

    display_solution(start_state, solution)

else:

    print("No solution found.")