from typing import *


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            j = len(s) - i - 1
            s[i], s[j] = s[j], s[i]


def main():
    s = ["H", "a", "n", "n", "a", "h"]
    a = Solution()
    a.reverseString(s)
    print(s)


if __name__ == '__main__':
    main()
