class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != val :
                nums[count] = nums[i]
                count

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums.pop(i)

        return len(nums)
        

def removeElement(self, nums: List[int], val: int) -> int:   
        j = 0
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[j] = nums[i]
                j=j+1
        nums = nums[:j]      
        return len(nums)        
        ```
		
		Easy and Simple solution