# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longestCommonPrefix(strs):
    answer=''
    i=0
    len_list=[len(s) for s in strs]
    min_len=min(len_list)

    while i<min_len:
        check_list=[s[i] for s in strs]
        if len(set(check_list))==1:
            return strs[0][:i]
            
        else: break
        i=i+1

    # return strs[0][:i]
print(longestCommonPrefix(["dog","racecar","car"]))



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer=''
        # index of the string, start with 0
        i=0
		# loop will continue until i<min_len
        len_list=[len(s) for s in strs]
        min_len=min(len_list)

        while i<min_len:
            check_list=[s[i] for s in strs]
			# if the set of the check list is 1, it means the alphabets are all same
            if len(set(check_list))==1: i+=1
			# else stop the loop
            else: break
            

        return strs[0][:i]
  

