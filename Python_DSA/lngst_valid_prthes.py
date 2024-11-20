def longest_valid_parentheses(s):
    stack = [-1]  # Initialize stack with -1 to handle edge cases
    max_length = 0  # Variable to store maximum length of valid substring
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)  # Push index of '(' on stack
        else:
            stack.pop()  # Pop last '(' index
            if not stack:
                stack.append(i)  # Push current index as base for future matches
            else:
                # Calculate length of current valid substring
                max_length = max(max_length, i - stack[-1])
    return max_length
# Test function
input_str = "((()"
print(longest_valid_parentheses(input_str))
