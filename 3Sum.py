
# def threeSum(self, nums,sums):
#     nums.sort()
#     res = []
#     for i in range(0,len(nums)):
   #      l = i+1
   #      r = len(nums)-1
   #      x = nums[i]
   #      while l<r:
   #          summ = x + nums[l] + nums[r]
   #          if summ == 0:
   #              if [x,nums[l],nums[r]] not in res:
   #                  res.append([x,nums[l],nums[r]])
   #              l+=1
   #              r-=1
   #          elif summ > 0:
   #              r-=1
   #          else:
   #                  l+=1
   #  return res


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:

# Input: nums = []
# Output: []

# Example 3:

# Input: nums = [0]
# Output: []

j=input("enter")
if j=="()" or j=="[]" or j=="{}" :
   print("True")
else:
   print("False")

