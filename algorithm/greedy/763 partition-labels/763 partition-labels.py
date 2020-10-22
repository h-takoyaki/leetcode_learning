from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # 存储某个字母对应地最后一个序号
        dic = {s: index for index, s in enumerate(S)}
        num = 0
        result = []
        j = dic[S[0]]

        for i in range(len(S)):
            num += 1
            if dic[S[i]] > j:
                j = dic[S[i]]
            if i == j:
                result.append(num)
                num = 0
        return result


# class Solution:
#     def partitionLabels(self, S: str) -> List[int]:
#         res = list()
#         r = -1
#         while r + 1 < len(S):
#             l = r + 1
#             for r in range(len(S) - 1, l-1, -1):
#                 if S[r] == S[l]:
#                     break
#             tempL = l
#             while tempL < r:
#                 if S[tempL] in S[r + 1:len(S)]:
#                     for tempR in range(len(S)-1, r-1, -1):
#                         if S[tempR] == S[tempL]:
#                             r = tempR
#                             break
#                 tempL += 1
#             res.append(r-l+1)
#         return res


def main():
    S = "ababcbacadefegdehijhklij"
    # S = "caedbdedda"
    # S = "aebbedaddc"
    # S = "qiejxqfnqceocmy"
    solution = Solution()
    print(solution.partitionLabels(S))


if __name__ == '__main__':
    main()
