class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            j = 0

            while j < len(needle):
                if haystack[i + j] != needle[j]:
                    break
                j += 1

            if j == len(needle):
                return i

        return -1