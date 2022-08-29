

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# num=int(input("Enter any 3 digit no"))
# num1=int(input("Enter any 3 digit no"))
# i=0
# while i<len(num):



# c = l1
# d = l2
# c1=""
# d1=""
# while(c):
#     c1+=str(c.val)
#     c = c.next
# while(d):
#     d1+=str(d.val)
#     d = d.next


# def addTwoNumbers(self, l1, l2, carry = 0):
# 	if not l1 and not l2:
# 		if carry == 1:
# 			return ListNode(carry)
# 		return None
# 	if not l1:
# 		l1 = ListNode(0)
# 	if not l2:
# 		l2 = ListNode(0)
	# val = l1.val + l2.val + carry
	# if val > 9:
	# 	val = val % 10
	# 	carry = 1
	# else:
	# 	carry = 0
	# l1.val = val
	# l1.next = self.addTwoNumbers(l1.next, l2.next, carry)
	# return l1

l1=[2,4,3]
l2=[5,6,4]
i=1
while i>=(-len(l1)):
	print(l1[i],end="")
	i+=1

