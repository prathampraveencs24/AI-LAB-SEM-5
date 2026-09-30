# 8-Puzzle Problem using Iterative Deepening Search (IDS)

GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)


def print_board(state):
    """Print the puzzle with 0 displayed as a blank space."""

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
    """Generate all possible states."""

    neighbors = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    for dr, dc, move in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            # Move blank
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append((tuple(new_state), move))

    return neighbors


def depth_limited_search(state, depth, path, visited):
    """Depth-Limited DFS."""

    # Goal test
    if state == GOAL_STATE:
        return path

    # Depth limit reached
    if depth == 0:
        return None

    visited.add(state)

    for next_state, move in get_neighbors(state):

        if next_state not in visited:

            result = depth_limited_search(
                next_state,
                depth - 1,
                path + [move],
                visited
            )

            if result is not None:
                return result

    visited.remove(state)

    return None


def iterative_deepening_search(start_state):
    """Iterative Deepening Search."""

    depth = 0

    while True:

        print("Searching at depth:", depth)

        visited = set()

        result = depth_limited_search(
            start_state,
            depth,
            [],
            visited
        )

        if result is not None:
            return result

        depth += 1


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
print("  8-PUZZLE USING IDS ALGORITHM")
print("===================================")

# 0 is used internally for the blank
# but it will NOT be displayed.
start_state = (
    1, 2, 3,
    5, 0, 6,
    4, 7, 8
)
print("\nInitial Puzzle:")
print_board(start_state)

print("Goal Puzzle:")
print_board(GOAL_STATE)

# Solve using IDS
solution = iterative_deepening_search(start_state)

print("\n===================================")
print("Solution Found!")
print("===================================")

print("Moves:", solution)
print("Number of moves:", len(solution))

display_solution(start_state, solution)