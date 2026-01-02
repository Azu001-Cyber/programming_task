
"""
Docstring for main
Problem: solve for longest substring without repeating characters,
Given a string 's', find the length of the longest substring without duplicate characters

Approach: The idea is to use two pointers (left and right) to represent a window of characters, 
and expand/shrink the window while keeping track of unique characters.

Steps:
1. initialize:
left = 0 (start of window)
right = 0 (end of window)
max_length = 0
a set 'seen' to store chars in the current window.

2. Expand right:
if s[right] is not in 'seen', add it to the set and update max_length.
if s[right] is already in 'seen', remove chars from the left until the duplicate is gone

3. continue until right reaches the end of the string
"""

def solve_for_substring(s:str) -> str:

    seen = set()  # set variables
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:  # 
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
    
text = solve_for_substring('abcabcbb')
print(text)