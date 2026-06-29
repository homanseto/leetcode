# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

#Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 

def twosum(nums,  target):
    hashMap = {}
    for i, value in enumerate(nums):
        output = target - value
        if output in hashMap:
            print([hashMap[output], i])
            return [hashMap[output], i]
        hashMap[value] = i
    raise Exception("Cannot find two integer whose sun is target")

# twosum([7,13,13,7,14,8], 23)

# follow up: Could have multiple solution adding up to target. Return all solution sets.
# index cannot beused more than one within the set.
# example : input: [0,1,2,3] target: 3, return [[0,3],[1,2]]

def multiple_two_sum(nums, target):
    result = []
    hashMap = {}
    for i, value in enumerate(nums):
        output = target - value
        if output in hashMap:
            complement_index = hashMap[output].pop() 
            result.append([complement_index, i])
            if not hashMap[output]:
                del hashMap[output]
        else:
            if value not in hashMap:
                hashMap[value] = []
            hashMap[value].append(i)
    print(result)
    return result
        
multiple_two_sum([7,13,13,13,7,7,14,8], 20)


