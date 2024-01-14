def sum_func(nums):
    total = sum(nums)
    return total

def reverse_func(nums):
    nums.sort(reverse=True)
    return nums

def return_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    evens.sort()
    return evens

def remove_dupes(nums):
    uniques = []
    for num in nums:
        if num not in uniques:
            uniques.append(num)
    uniques.sort()
    return uniques        

my_list = [1, 2, 3, 4, 2, 6, 2, 4, 2]

print(f"sum_func: {sum_func(my_list)}")

print(f"reverse_func: {reverse_func(my_list)}")

print(f"return_evens: {return_evens(my_list)}")

print(f"remove_dupes: {remove_dupes(my_list)}")