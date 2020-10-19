import typing


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        temps = ""
        tempt = ""
        for i in S:
            if i == '#' and temps != "":
                temps = temps[:-1]
            elif i != '#':
                temps += i
        for j in T:
            if j == '#' and tempt != "":
                tempt = tempt[:-1]
            elif j != '#':
                tempt += j
        if temps == tempt:
            return True
        else:
            return False


def main():
    S = "cb##"
    T = "c#d#"
    solution = Solution()
    print(solution.backspaceCompare(S, T))


if __name__ == '__main__':
    main()
