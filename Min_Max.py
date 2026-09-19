def read_input():
    n = int(input())
    node_type = {}
    node_value = {}
    for _ in range(n):
        parts = input().split()
        name = parts[0]
        kind = parts[1]
        node_type[name] = kind
        if kind == "TERMINAL":
            node_value[name] = int(parts[2])

    e = int(input())
    children = {}
    for _ in range(e):
        parent, child = input().split()
        children.setdefault(parent, []).append(child)

    root = input().strip()
    return node_type, node_value, children, root


def minimax(node, node_type, node_value, children):
    kind = node_type[node]

    if kind == "TERMINAL":
        return node_value[node], None

    child_scores = []
    for child in children.get(node, []):
        score, _ = minimax(child, node_type, node_value, children)
        child_scores.append((child, score))

    if kind == "MAX":
        best_child, best_score = max(child_scores, key=lambda x: x[1])
    else:  # MIN
        best_child, best_score = min(child_scores, key=lambda x: x[1])

    return best_score, best_child


def main():
    node_type, node_value, children, root = read_input()

    value, best_move = minimax(root, node_type, node_value, children)

    print(f"Minimax value: {value}")
    print(f"Best move for MAX: {best_move}")


if __name__ == "__main__":
    main()