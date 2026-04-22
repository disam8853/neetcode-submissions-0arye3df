class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = []
        stack = []
        def dfs(remain):
            nonlocal ans, temp, stack
            if len(temp) == n * 2:
                ans.append("".join(temp))
                return
            if stack:
                temp.append(')')
                stack.pop()
                dfs(remain)
                temp.pop()
                stack.append('(')
            if remain > 0:
                temp.append('(')
                stack.append('(')
                dfs(remain - 1)
                temp.pop()
                stack.pop()
        dfs(n)
        return ans