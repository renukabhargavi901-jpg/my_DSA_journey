# Day 01 Notes

## HashMap
- Stores key-value pairs
- Average lookup: O(1)
- Used for frequency counting

## Prefix Sum
- prefix[i] = sum of elements from 0 to i
- Subarray Sum = prefix[j] - prefix[i-1]

### Subarray Sum Equals K
- Store prefix sums in a HashMap
- Check if (current_prefix - k) exists
- Count frequencies

## Counting Sort
- Count frequency of each value
- Traverse from smallest to largest
- Time Complexity: O(n + maxValue)

### Maximum Ice Cream Bars
- Use Counting Sort
- Buy cheapest ice creams first
- Greedy approach