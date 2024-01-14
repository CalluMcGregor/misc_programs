class Solution:
    def romanToInt(self, s: str) -> int:
        """"""
        numerals = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = 0
        skip = False
        for index, character in enumerate(s):
            if character in numerals:
                print(f"index: {index}, character: {character}, value: {numerals[character]}")
                if skip:
                    skip = False
                    continue
                if index < len(s) - 1 and s[index:index + 2] == "IV":
                    total += 4
                    skip = True
                elif index < len(s) - 1 and s[index:index + 2] == "IX":
                    total += 9
                    skip = True
                elif index < len(s) - 1 and s[index:index + 2] == "XL":
                    total += 40
                    skip = True
                elif index < len(s) - 1 and s[index:index + 2] == "XC":
                    total += 90
                    skip = True
                elif index < len(s) - 1 and s[index:index + 2] == "CD":
                    total += 400
                    skip = True
                elif index < len(s) - 1 and s[index:index + 2] == "CM":
                    total += 900
                    skip = True
                else:
                    total += numerals[character]        
                
        print(total)

testcase = Solution()
test = testcase.romanToInt("MCMXCIV")