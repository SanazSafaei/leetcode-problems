from typing import BinaryIO



class Solution:
    def reverse(self, x: int) -> int:
        # x_str = str(x) # is now a string
        if x < 0:
            y = str(x)[1:][::-1]
            # while y[0] == '0':
            #     y = y[1:]
            x = 0-int(y)
            if x < -2**31:
                return 0
            return x
        else:
            y = int(str(x)[::-1])
            if y > (2**31)-1:
                return 0
            return y

s = Solution()
print(s.reverse(7))