def positive_sum(arr):
    solution = []
    for x in arr:
        if x > 0:
            solution.append(x)
        
    return sum(solution)
