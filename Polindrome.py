def isPalindrome(n):  
    return (n == n[::-1]) 

n = 'hadi'
print(n[:-1])
if (isPalindrome(n)): 
    print("Yes") 
else : 
    print("No") 