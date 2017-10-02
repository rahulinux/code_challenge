#!/usr/bin/env python 

"""
## Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

nums = [3,2,3]
target = 6

# Approach #1 (Brute Force) 
# The brute force approach is simple. Loop through each element x and find if there is another value that equals to target 
# Nested for loop compare all O(n^2)

def bruteforce_twosum(nums,target):
    for i in range(0,len(nums)):
        for k in range(1,len(nums)):
            if i != k: 
              # print i,k
              if (nums[i] + nums[k]) == target:
                return [i,k]

print bruteforce_twosum(nums,target)


# Approach #2 (One-pass Hash ) 
# While we iterate and inserting elements into the hash table, 
# we also look back to check if current element's complement already exists in the table. 
# If it exists, we have found a solution and return immediately.
def hash_twosum(nums,target):
        h = {}
        for i in range(len(nums)):
           if nums[i] in h:
               return [h[nums[i]],i]
           h[target - nums[i]] = i
           
           
           
print hash_twosum(nums,target)
