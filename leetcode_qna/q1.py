'''1. Two Sum
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Question Link: https://leetcode.com/problem-list/w0f2z5yj/ '''

#Solution1:
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i,j]

#Solution2:
seen = {}

for i in range(len(nums)):
    needed = target - nums[i]

    if needed in seen:
        return [seen[needed], i]

    seen[nums[i]] = i

          
# Output:
# [0,1]