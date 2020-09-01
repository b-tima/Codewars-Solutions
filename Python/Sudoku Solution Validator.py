def valid_container(container):
    numbers = [x for x in range(1, 10)]
    for n in container:
        if n not in numbers:
            return False
        numbers.remove(n)
    return len(numbers) == 0

def valid_solution(board):
    # Horizontal
    for h in board:
        if not valid_container(h):
            return False
    # Vertical
    for i in range(9):
        v = [h[i] for h in board]
        if not valid_container(v):
            return False
    # Box
    for i in range(3):
        for j in range(3):
            b = [board[3*i+k][3*j+m] for k in range(3) for m in range(3)]
            if not valid_container(b):
                return False
    return True