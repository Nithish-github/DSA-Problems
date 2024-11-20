# Definition
Kadane's Algorithm is an efficient method to find the maximum sum of a contiguous subarray in an array of integers. It works by iterating through the array, maintaining a running sum of the current subarray, and updating the maximum sum encountered so far. 

If the running sum becomes negative, it is reset to zero, as starting fresh from the next element may yield a higher sum. Its time complexity is O(n).

### Problem Maximum Subarray Sum is best suitable example for this.


# The Main Syntax for this Approch is given below
    maxProfit = 0
    best = 0
    for num in profit:
        maxProfit = max(num,maxProfit+num)
        best = max(best,maxProfit)
        
    return best


### It is Greedy | DP | Involves the combination of Sliding window and Two Pointer Concept

### Video sourec : https://youtu.be/AHZpyENo7k4?si=HUcowqDJupq8KiR2