class Solution:
    def romanToInt(self, s: str) -> int:

        roman_number = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        current = s[0]
        sum = roman_number[s[0]]
        for i in s[1:]:
            if roman_number.get(current) < roman_number.get(i):
                sum = sum + roman_number[i] - 2*roman_number[current]
            else:
                sum = sum + roman_number[i]
            current = i
        return sum


s = Solution()
print(s.romanToInt("IX"))
