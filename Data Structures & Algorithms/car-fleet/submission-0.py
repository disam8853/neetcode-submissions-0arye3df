class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 3, 4.5, 10, 3
        ary = [[position[i], speed[i]] for i in range(len(speed))]
        ary.sort()
        st = []
        for startPos, speed in ary:
            timeToEnd = (target - startPos) / speed
            while st and st[-1] <= timeToEnd:
                st.pop()
            st.append(timeToEnd)
        return len(st)