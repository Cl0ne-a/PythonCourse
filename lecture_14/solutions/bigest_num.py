def find_highest_val(nums) -> int:
    highest = 0
    for num in nums:
        if num > 0 and num > highest:
            highest = num

    return highest


print(find_highest_val([4, 2, 7, 111, 0, -1, 888]))