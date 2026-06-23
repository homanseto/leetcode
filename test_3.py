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


def sligning_window(s:str) -> int: # total O(n)
    n = len(s)
    left = 0
    charSet = set()
    max_length = 0  
    if n == 0:
        return max_length
    for right in range(n): # O(n)
        while s[right] in charSet: # O(1), average time for set operations 
            charSet.remove(s[left]) # O(1)
            left += 1
        charSet.add(s[right]) #O(1) Add the current character after removing duplicates
        max_length = max(max_length, right- left +1) # O(1) Update max_length once per right
    return max_length

def lengthOfLongestSubstring(self, s: str) -> int:
    left = 0
    right = 0
    cnt = [False for _ in range(26)]
    ans = 0
    while right < len(s):
        # the ord() function returns an integer representing the Unicode code point of a single character.
        # print(ord('A'))  # Output: 65, print(ord('a'))  # Output: 97 , print(ord('b'))  # Output: 98
        while cnt[ord(s[right]) - ord('a')]:
            cnt[ord(s[left]) - ord('a')] = False
            left = left + 1
        cnt[ord(s[right]) - ord('a')] = True
        if right - left + 1 > ans:
            ans = right - left + 1
        right = right + 1