from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        flag = False
        l = 0
        if len(strs) == 1 :
            return strs[0]
        for l in range(0, len(strs[0])):
            letter = strs[0][l]
            for word in strs[:]:
                try:
                    if word[l] != letter:
                        flag = True
                        break
                except:
                    flag = True
                    break
            if flag:
                break
        if l and flag:
            return strs[0][:l]
        elif not flag:
            return strs[0][:l+1]
        return ""



s = Solution()
print(s.longestCommonPrefix(["ab", "a"]))