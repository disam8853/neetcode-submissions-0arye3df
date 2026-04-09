class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if is_number(t):
                st.append(int(t))
                continue
            b, a = st.pop(), st.pop()
            if t == '+':
                st.append(a + b)
            elif t == '-':
                st.append(a - b)
            elif t == '*':
                st.append(a * b)
            elif t == '/':
                st.append(int(a/b))
        return st[-1]
def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False