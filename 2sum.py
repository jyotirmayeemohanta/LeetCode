
def twoSum(nums,target):
     h={}
     for i in range(len(nums)):
          if nums[i] in h:
               return [h[nums[i]],i]
          else:
              h[target-nums[i]]=i
list=[3,2,4]
target=6
print(twoSum(list,target))


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
