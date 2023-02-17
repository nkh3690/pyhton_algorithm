COLUMN = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ROW = ['1', '2', '3', '4', '5', '6', '7', '8']


def solution(pos: str):
    x = COLUMN.index(pos[0])
    y = ROW.index(pos[1])
    result = 0

    d = [
        [-1, -2], [1, -2],
        [-2, -1], [-2, 1],
        [2, -1], [2, 1],
        [-1, 2], [1, 2]
    ]

    for i in range(len(d)):
        dx, dy = d[i]

        if 0 <= x + dx <= 7 and 0 <= y + dy <= 7:
            result += 1

    return result
