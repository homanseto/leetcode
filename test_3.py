string_list = ["a", "b","c", "c", "d", "e", "f"]

# Given a string s, find the length of the longest substring without duplicate characters.

# striaght forward

def length_of_longest_substring(s: str) -> int:
    n = len(s)
    max_length = 0
    for start in range(str): # O(N)
        for end in range(start, n): # O(N)
            substring = s[start:end+ 1]
            
            #O(N), A Set in JavaScript (or Python) is a collection of unique elements
            # When you convert a substring (or any iterable) into a Set, the following happens:
            # 1) The substring is iterated over (to extract each character), 2) Each character is added to the Set., 3) If a character is already in the Set, it is ignored (since Set only stores unique elements).
            if len(substring) == len(set(substring)): 
                max_length = max(max_length, len(substring))
    return max_length


def sligning_window(s:str) -> int:
    n = len(s)
    left = 0
    charSet = set()
    max_length = 0  
    if n == 0:
        return max_length
    for right in range(n):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
            charSet.add(s[right])
            max_length = max(max_length, right- left +1)
    return max_length