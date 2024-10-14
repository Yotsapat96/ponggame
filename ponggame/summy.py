# dict = {
#     "I": 1,
#     "V": 5,
#     "x": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
#  }
#
# s = "LVIII"
# num = 0
# for i in range(len(s) - 1):
#     if dict[s[i+1]] > dict[s[i]]:
#         num -= dict[s[i]]
#     # if equal just plus
#     else:
#         num += dict[s[i]]
#
# num += dict[s[len(s) - 1]]
#
# print(num)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            "I": 1,
            "V": 5,
            "x": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        num = 0
        for i in range(len(s) - 1):
            if dict[s[i+1]] > dict[s[i]]:
                num -= dict[s[i]]
            # if equal just plus
            else:
                num += dict[s[i]]

        num += dict[s[len(s) - 1]]
        return num