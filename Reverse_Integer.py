# Example 1:

# Input: x = 123
# Output: 321

# Example 2:

# Input: x = -123
# Output: -321

# Example 3:

# Input: x = 120
# Output: 21


# def reverse(self, x: int) -> int:
#     y=abs(x)
#     r=int(str(y)[::-1])
#     if(x<=(2 ** 31)-1 and r<=(2 ** 31)-1):
#         if(x>=-1*(2 ** 31) and r>=-1*(2 ** 31)):
#             if(x<0):
#                 return -r
#             else:
#                 return r
#         else:
#             return 0


# def reverse(self, x: int) -> int:
#     sign = 1 if x >= 0 else -1
#     s = str(x*sign)
#     res = int(s[::-1])*sign
#     return 0 if(-2**31 > res or res > (2**31)-1) else res

def reverse_signed(num):
    sum=""
    while num>0:
        rem=num%10
        sum+=str(rem)
        num=num//10
    return sum
print(reverse_signed(123))