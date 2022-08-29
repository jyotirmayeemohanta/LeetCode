def longestCommonPrefix(strs):
        answer=''
        # index of the string, start with 0
        i=0
		# loop will continue until i<min_len
        len_list=[len(s) for s in strs]
        min_len=min(len_list)

        while i<min_len:
            check_list=[s[i] for s in strs]
			# if the set of the check list is 1, it means the alphabets are all same
            if len((check_list))==1:
            
             return strs[0][i] 
			# else stop the loop
            else: break
            i=i+1
             
strs=["dog","racecar","car"]
print(longestCommonPrefix(strs))
          
