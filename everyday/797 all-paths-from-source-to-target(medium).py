"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-paths-from-source-to-target
"""
from typing import *
from functools import lru_cache
from collections import deque

# class Solution:
#     # 记忆化dfs
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         n = len(graph)

#         @lru_cache(None)
#         def dfs(node):
#             if node == n - 1:
#                 return [[n - 1]]
#             ans = []
#             for nxt in graph[node]:
#                 for res in dfs(nxt):
#                     ans.append([node] + res)
#             return ans
        
#         return dfs(0)

# class Solution:
#     # bfs
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         n = len(graph)
#         q = deque([[0]])
#         ans = []
#         while q:
#             path = q.popleft()
#             if path[-1] == n - 1:
#                 ans.append(path)
#                 continue
#             for nxt in graph[path[-1]]:
#                 q.append(path + [nxt])
#         return ans


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        result = []

        def dfs(node, path):
            path.append(node)
            if node == n-1:
                 result.append(path)
                 return
            for nxt in graph[node]:
               dfs(nxt, list(path))
        
        dfs(0, [])
        return result



sol = Solution()
result = sol.allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]])
print(result)