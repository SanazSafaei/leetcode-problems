class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x<0 :
        #     return False

        x = str(x)
        half = int(len(x)/2)
        length = len(x)
        if length == 1:
            return True
        elif length%2 ==0:
            print(half, x[0:half] , x[:half-1:-1])
            return True if x[0:half] == x[:half-1:-1] else False
        print("---",half, x[0:half+1] , x[:half-1:-1])
        return True if x[0:half+1] == x[:half-1:-1] else False


s = Solution()

print(s.isPalindrome(-1))