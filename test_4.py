
# Given a string s containing just the characters 
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# constraints 1 <= s.length <= 10^4, s consists of parentheses only '()[]{}'

def validParentheses(s: str) -> bool :
    start_half = ['(','[','{'] 
    end_half = [')',']','}']
    stack = []
    if s[0] in end_half:
        return False
    for p in s:
        if p in start_half:
            stack.append(p)
        else:
            # If stack is empty or the top doesn't match the closing bracket
            if not stack:
                return False
            latest_stack = stack[-1]
            start_index = start_half.index(latest_stack)
            end_index = end_half.index(p)
            if start_index != end_index:
                return False
            remove = stack.pop()
    # If stack is empty, all brackets were matched
    return len(stack) == 0


class Solution:
    def validateBracketsString (self, s: str) -> bool:
        stack = []
        openBrackets = "({["
        closeBrackets = ")}]";
        for c in s:
            if c in openBrackets:
              stack.append(c)
            else:
              for i in range(3):
                if c == closeBrackets[i]:
                  if len(stack) !=0 and stack[-1] == openBrackets[i]:
                    stack.pop()
                  else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Follow up, If it's invalid, return a vali string. Otherwise just return the original string
        
def validParenthesesString(s: str) -> str :
    start_half = ['(','[','{'] 
    end_half = [')',']','}']
    result = []
    stack = []
    for p in s:
        if p in start_half:
            stack.append(p)
            result.append(p)
        else:
            end_index = end_half.index(p)
            add_start = start_half[end_index]
            if not stack:
                result.append(add_start)
                result.append(p)
            else:
                latest_stack = stack[-1]
                start_index = start_half.index(latest_stack)
                if start_index != end_index:
                    result.append(add_start)
                    result.append(p)
                else:
                    remove = stack.pop()
                    result.append(p)
    while len(stack) != 0:
        latest_stack = stack[-1]
        start_index = start_half.index(latest_stack)
        end_value = end_half[start_index]
        result.append(end_value)
        remove = stack.pop()
    # If stack is empty, all brackets were matched
    string_result = "".join(result)
    print(string_result)
    return string_result


def validParenthesesString2(s: str) -> str:
    # Map closing brackets to their matching opening brackets
    matching_pair = {')': '(', ']': '[', '}': '{'}
    # Map opening brackets to their matching closing brackets (for the final cleanup)
    reverse_pair = {'(': ')', '[': ']', '{': '}'}
    
    stack = []
    result = []
    
    for char in s:
        if char in matching_pair.values():  # It's an opening bracket
            stack.append(char)
            result.append(char)
        elif char in matching_pair:  # It's a closing bracket
            expected_open = matching_pair[char]
            
            # If stack is empty or the top doesn't match, we have an invalid state.
            # We fix it by pretending the correct opening bracket was there all along.
            if not stack or stack[-1] != expected_open:
                # Insert the missing opening bracket into our result
                result.append(expected_open)
                # Keep our stack balanced by pushing it to the stack so 'char' can pop it
                stack.append(expected_open)
            
            # Now that the top of the stack definitely matches, we pop it and add the closing bracket
            stack.pop()
            result.append(char)
            
    # If there are leftover unclosed brackets in the stack, close them at the end
    while stack:
        open_bracket = stack.pop()
        result.append(reverse_pair[open_bracket])
    print("".join(result))
    return "".join(result)

validParenthesesString('[(]')
validParenthesesString2('[(]')

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

#Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 

def twosum(nums,  target):
    hashMap = {}
    for i, value in enumerate(nums):
        output = target - value
        if output in hashMap:
            print([hashMap[output], i])
            return [hashMap[output], i]
        hashMap[value] = i
    raise Exception("Cannot find two integer whose sun is target")

# twosum([7,13,13,7,14,8], 23)

# follow up: Could have multiple solution adding up to target. Return all solution sets.
# index cannot beused more than one within the set.
# example : input: [0,1,2,3] target: 3, return [[0,3],[1,2]]

def multiple_two_sum(nums, target):
    result = []
    hashMap = {}
    for i, value in enumerate(nums):
        output = target - value
        if output in hashMap:
            complement_index = hashMap[output].pop() 
            result.append([complement_index, i])
            if not hashMap[output]:
                del hashMap[output]
        else:
            if value not in hashMap:
                hashMap[value] = []
            hashMap[value].append(i)
    print(result)
    return result
        
multiple_two_sum([7,13,13,13,7,7,14,8], 20)


