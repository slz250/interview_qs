class Solution(object):
    def longest_valid_parentheses_s(self, s):
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            pop_idx = len(stack) - 1
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop(pop_idx)
                if len(stack) == 0:
                    stack.append(i)
                else:
                    top_idx = stack[pop_idx-1]
                    max_len = max(max_len, i - top_idx)
        return max_len

    def longest_valid_parentheses_wes(self, s):
        left, right, max_len = 0, 0, 0
        for ele in s:
            if ele == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, left * 2)
            elif right > left:
                left, right = 0, 0

        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_len = max(max_len, left * 2)
            elif right < left:
                left, right = 0, 0

        return max_len

    def longest_valid_parentheses_sr(self, s):
        pass

