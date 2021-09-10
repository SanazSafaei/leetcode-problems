class Solution:
    def isValid(self, s: str) -> bool:
        self.special_char = {"{": "}", "[": "]", "(": ")"}

        return self.find_close(s)


    def find_close(self, s):
        l = len(s)
        start = 0
        print(s)
        if not s:
            return True
        if len(s) == 1:
            if s == "{" or s == "[" or s == "(" or s == ")" or s == "]" or s == "}":
                return False

        if (s[0] == ")" or s[0] == "]" or s[0] == "}"):
            return False
        counter = 0
        for i in range(start, l):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                for j in range(i+1, l):
                    if s[j] == s[i]:
                        counter += 1
                        # r = self.find_close(s[j:], True, c)
                        # if not r:
                        #     return False
                        # else:
                        #     counter = 1
                        #     flag = True
                    elif (s[j] == self.special_char.get(s[i])) and counter == 0:
                        if i+1 == j and not (j == l-1):
                                return self.find_close(s[j+1:])
                        elif j == l-1:
                            return self.find_close(s[i+1:j])
                        else:
                            return self.find_close(s[i+1:j]) and self.find_close(s[j+1:])
                    elif (s[j] == self.special_char.get(s[i])):
                        counter = counter - 1

                return False


s = Solution()
print(s.isValid("[({(())}[()])]"))
