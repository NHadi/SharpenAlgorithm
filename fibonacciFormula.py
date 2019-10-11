# Using The Formula to Calculate Fibonacci Numbers
# Fn = {[(√5 + 1)/2] ^ n} / √5
# Reference: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html
# Time Complexity: O(1) 

import math
def solution(n):
    phi = (math.sqrt(5) + 1) / 2        
    fibonacci = math.pow(phi, n) / math.sqrt(5)
    return round(fibonacci)

print(solution(23))