def solution(n: int, k: int) -> int:
    result = 0

    while n > 1:
        if n % k == 0:
            n /= k
        else:
            n -= 1
        result += 1

    return result
