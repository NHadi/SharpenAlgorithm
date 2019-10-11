# Using The Golden Ratio to Calculate Fibonacci Numbers
# Example: 8 × φ = 8 × 1.618034... = 12.94427... = 13 (rounded)
import math
def solution(n):
    phi_1 = (math.sqrt(5) + 1) / 2    
    phi_2 = (math.sqrt(5) - 1) / 2      
    f = (math.pow(phi_1, n) - math.pow(phi_2, n)) / math.sqrt(5)
    return round(f)

print(solution(8))