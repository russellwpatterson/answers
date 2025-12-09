class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        longest_dict = {}

        str_len = len(s)

        current_length = 0
        for i in range(0, str_len):
            if i == 0:
                longest_dict[s[i]] = 1
                current_length = 1
            else:
                last_char_ord = ord(s[i - 1])
                current_char_ord = ord(s[i])

                if (current_char_ord - last_char_ord) % 26 != 1:
                    current_length = 1
                else:
                    current_length += 1
            
                longest_dict[s[i]] = max(longest_dict.get(s[i], 0), current_length)

        return sum([n for n in longest_dict.values()])
