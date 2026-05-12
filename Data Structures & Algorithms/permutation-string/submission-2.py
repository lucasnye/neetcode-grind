from collections import Counter
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         ctr = Counter(s1)
#         n = len(s1)
#         substring = {}
#         last_index = None
#         left = 0
#         for i, char in enumerate(s2):
#             if char in ctr:
#                 if ctr[char] > 0:
#                     if last_index is None:
#                         ctr[char] -= 1
#                         substring[char] = i
#                         last_index = i
#                         left = i
#                     elif i == last_index + 1:
#                         ctr[char] -= 1
#                         substring[char] = i
#                         last_index = i
#                 else:
#                     if i == left + len(substring) - 1:
#                         substring[char] = i
#                         last_index = i
#                     else:
#                         while s2[left] == char:
#                             left += 1
#                         substring[char] = i
#                         last_index = i
#             if len(substring) == n:
#                 return True
#         return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_count = Counter()
        
        # Build initial window of size len(s1)
        for i in range(len(s1)):
            window_count[s2[i]] += 1
        
        # Check if initial window matches
        if window_count == s1_count:
            return True
        
        # Slide the window
        for i in range(len(s1), len(s2)):
            # Add new character (right side)
            window_count[s2[i]] += 1
            
            # Remove old character (left side)
            left_char = s2[i - len(s1)]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            # Check if current window matches
            if window_count == s1_count:
                return True
        
        return False