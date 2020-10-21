class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                # 和name中的字母匹配
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                # 和typed中前一个字母匹配
                j += 1
            else:
                return False
        return i == len(name)


def main():
    name = "alex"
    typed = "aaleex"
    solution = Solution()
    print(solution.isLongPressedName(name, typed))


if __name__ == '__main__':
    main()