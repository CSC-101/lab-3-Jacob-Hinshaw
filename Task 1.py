more = [x + 1 for x in [1,2,3,4]]    # 2,3,4,5
print()                              # [2,3,4,5]

def square(n:int) -> int:
    return n * n                          # 1,2,3,4

squares = [square(x) for x in [1,2,3,4]]  # [1,4,9,16] They are the squares of the numbers recorded above
print()

def check(n:int) -> bool:
    return n > 2                           # 0 -> false, 1 -> false, 2 -> false, 3 -> true, 4 -> true

answer = [x for x in range(5) if check(x)] # answer: [3,4]
print()

def inc(m:int) -> int:
    return m + 1                           # 3 -> 4, 4 -> 5

def check(n:int) -> bool:
    return n > 2                           # 0 -> false, 1 -> false, 2 -> false, 3 -> true, 4 -> true

answer = [inc(x) for x in range(5) if check(x)]  # answer: [4,5]
print()