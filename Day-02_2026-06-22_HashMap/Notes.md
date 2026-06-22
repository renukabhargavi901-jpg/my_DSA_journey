# Day 02 Notes

## HashMap

- Stores key-value pairs
- Average lookup: O(1)

## Two Sum

Idea:
- For each element, find its complement:
  target - nums[i]

- If complement exists in HashMap:
  return indices

- Otherwise store current value and index

Time Complexity: O(n)
Space Complexity: O(n)