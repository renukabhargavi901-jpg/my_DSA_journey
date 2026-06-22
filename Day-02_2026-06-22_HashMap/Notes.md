# Day 02 Notes

## Two Sum

### Idea
- Store number and its index in a HashMap.
- For each number, calculate:
  
  complement = target - num

- If complement exists in HashMap, return the indices.
- Otherwise store the current number.

### Complexity
- Time: O(n)
- Space: O(n)

---

## Maximum Number of Balloons

### Observation
To form the word:

balloon

Required frequencies:

b -> 1
a -> 1
l -> 2
o -> 2
n -> 1

### Approach

1. Count the frequency of each character in the given string.
2. Check how many times each required character is available.
3. Since:
   - 'l' is needed twice → freq['l'] // 2
   - 'o' is needed twice → freq['o'] // 2
4. The answer is the minimum among:

min(
    freq['b'],
    freq['a'],
    freq['l'] // 2,
    freq['o'] // 2,
    freq['n']
)

### Example

text = "loonbalxballpoon"

Frequency:

b -> 2
a -> 2
l -> 4
o -> 4
n -> 2

Possible balloons:

b -> 2
a -> 2
l -> 4//2 = 2
o -> 4//2 = 2
n -> 2

Answer = min(2,2,2,2,2) = 2

### Complexity

- Time: O(n)
- Space: O(1)

### Pattern

When the problem asks:
- Count characters
- Check occurrences
- Form a word/string from letters

Think:

✅ HashMap / Frequency Counting