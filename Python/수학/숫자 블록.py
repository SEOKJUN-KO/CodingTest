def calculate(n):
    if n == 1:
        return 0
    max_divisor = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if n // i <= 10_000_000:
                return n // i
            max_divisor = max(max_divisor, i)
    if max_divisor <= 10_000_000:
        return max_divisor
    return 1

def solution(begin, end):
    return [calculate(i) for i in range(begin, end+1)]