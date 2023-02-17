from typing import List

INF = int(1e9)


def solution(n, m, arrays: List[List[int]]):
    result = 0

    for i in range(0, n):
        num = INF
        for j in range(0, m):
            num = min(num, arrays[i][j])
        result = max(result, num)

    return result
