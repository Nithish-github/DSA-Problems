# The Main Syntax for this Approch is given below
    maxProfit = 0
    best = 0
    for num in profit:
        maxProfit = max(num,maxProfit+num)
        best = max(best,maxProfit)
        
    return best


### It is Greedy | DP | Involves the combination of Sliding window and Two Pointer Concept