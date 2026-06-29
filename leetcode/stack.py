
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

