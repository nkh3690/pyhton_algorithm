from typing import List


def solution(m: int, k: int, arr: List[int]) -> int:
    arr.sort()

    first = arr[len(arr) - 1]
    second = arr[len(arr) - 2]
    result = 0

    for i in range(1, m + 1):
        if i % (k + 1) == 0:
            result += second
        else:
            result += first

    return result
