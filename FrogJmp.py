def solution(X, Y, D):
    distance = Y - X        
    if distance % D == 0:
        return distance//D
    else:
        return distance//D + 1

print(solution(10, 90, 30))        