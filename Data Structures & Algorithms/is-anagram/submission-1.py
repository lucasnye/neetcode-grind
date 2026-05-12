class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # chars = []
        # for char in s:
        #     chars.append(char)
        # for char in t:
        #     chars.remove(char)

        chars = {}
        for char in s:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
        for bloop in t:
            if bloop in chars:
                chars[bloop] -= 1
                if chars[bloop] == 0:
                    del chars[bloop]
            else:
                return False
        for meep in chars:
            if chars[meep] != 0:
                return False
        return True