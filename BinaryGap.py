def solution(N):
    max_gap = 0
    current_gap = 0
    # Skip the tailing zero(s) 
    # ex bit of 8 is 1000 so (N //= 2 => is what is called floor division - i.e. 7 // 2 = 3) so 1000 will return 1 skip for 0000 
    while N > 0 and N%2 == 0:
        N //= 2
    while N > 0:
        remainder = N%2
        if remainder == 0:
            current_gap += 1
        else:
            if current_gap != 0:
                max_gap = max(current_gap, max_gap)
                current_gap = 0                
        N //= 2
        print(N)

    return max_gap

print(solution(529))