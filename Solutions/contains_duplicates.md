# Contains Duplicates

The function correctly identifies whether an integer array contains any duplicate values. Here are the results for the provided test cases:

- For the array `[1, 2, 3, 1]`, the result is `True` because the value `1` appears twice.
- For the array `[1, 2, 3, 4]`, the result is `False` because all elements are distinct.
- For the array `[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]`, the result is `True` because there are multiple duplicates present in the array

```python
def contains_duplicate(nums):
    # Use a set to track unique elements
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test cases
test_cases = [
    [1, 2, 3, 1], # True, because 1 appears twice
    [1, 2, 3, 4], # False, all elements are distinct
    [1,1,1,3,3,4,3,2,4,2] # True, multiple duplicates
]

results = [contains_duplicate(tc) for tc in test_cases]
results
```
