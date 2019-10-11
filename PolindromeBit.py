# function to reverse bits of a number 
def reverseBits(n) : 
    rev = 0
    while (n > 0): 
        rev = rev << 1
        if (n & 1 == 1) : 
            rev = rev ^ 1
        n = n >> 1
    return rev 
      
def isPalindrome(n): 
    rev = reverseBits(n)   
    return (n == rev) 


n = 11
if (isPalindrome(n)): 
    print("Yes") 
else : 
    print("No") 