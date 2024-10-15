def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num         # loop 1: total: 4, num: 4
    return total                    # loop 2: total: 13, num: 9
                                    # loop 3: total: 15, num: 2
                                    # loop 4: total: 16, num: 1
result = tally([4, 9, 2, 1])

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])   # loop 1: new_list: [4], idx: 0
    return new_list                  # loop 2: new_list: [4,9], idx: 1
                                     # loop 3: new_list: [4,9,2], idx: 2
result = copy([4, 9, 2, 1])          # loop 4: new_list: [4,9,2,1], idx: 3
                                     # instead of adding the numbers together, this function creates a new list with the same numbers

def increment_all(nums:list[int]) -> list[int]:
    new_list = []                          # loop 1: new_list: [5], value:4
    for value in nums:                     # loop 2: new_list: [5,10], value:9
        new_list.append(value + 1)         # loop 3: new_list: [5,10,3], value:2
    return new_list                        # loop 4: new_list: [5,10,3,2], value:1

result = increment_all([4, 9, 2, 1])