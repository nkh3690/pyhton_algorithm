NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
LAND, SEA, VISITED = 0, 1, 2
COORD_X = [0, -1, 0, 1]
COORD_Y = [-1, 0, 1, 0]


def turn_left(dir: int) -> int:
    dir = dir + 1
    if dir > WEST:
        dir = NORTH

    return dir


def is_can_go(x: int, y: int, field: list[list[int]]) -> bool:
    if field[y][x] == LAND:
        return True
    else:
        return False


def solution(x: int, y: int, dir: int, field: list[list[int]]) -> int:
    field[y][x] = VISITED
    visited_count = 1
    turn_count = 0

    while True:
        dir = turn_left(dir)
        turn_count += 1
        dx = x + COORD_X[dir]
        dy = y + COORD_Y[dir]

        if is_can_go(dx, dy, field):
            field[dy][dx] = VISITED
            x, y = dx, dy
            visited_count += 1
            turn_count = 1
            continue

        if turn_count > 3:
            dx = x - COORD_X[dir]
            dy = y - COORD_Y[dir]

            if is_can_go(dx, dy, field):
                x, y = dx, dy
            else:
                break

    return visited_count
