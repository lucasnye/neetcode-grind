from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = Counter()
        max_length = max_freq = 0
        left = right = 0

        for i, char in enumerate(s):
            # 1. Add s[right] to window
            right = i
            char_count[char] += 1
            # 2. Update max_freq
            max_freq = char_count.most_common(1)[0][1]
            # 3. Check if window is valid
            while (right - left + 1 - max_freq) > k:
                char_count[s[left]] -= 1
                left += 1
                max_freq = char_count.most_common(1)[0][1]
            # 4. If invalid, shrink from left
            # 5. Update max_length
            max_length = max(max_length, right - left + 1)
        return max_length