class Solution:
    def encode(self, strs: List[str]) -> str:
        out = ""
        for i in strs:
            l = len(i)
            out += str(len(i)) + '#' + i 
        return out

    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j + 1 + length
        # result, i = [], 0
        # length = ''
        # element = ''

        # while i < len(s):
        #     length = str(length)
        #     while s[i].isdigit():
        #         length += s[i]
        #         if s[i+1] == '#':
        #             length = int(length)
        #             i += 1
        #         i += 1
        #     while length != 0:
        #         element += s[i]
        #         i += 1
        #         length -= 1
        #     result.append(element)
        #     element = ''

        return result