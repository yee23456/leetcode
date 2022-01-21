# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:59:10 2022

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

@author: 沈睿朋
"""
#%%
a = [2,3,6,7]
for i in range(len(a)):
    b = [a[j:i+1] for j in range(i+1)]
    print(b)
#%%
# candidates = [2,3,6,7]
# target = 7
# result = []
# candidates.sort()
# def dfs(candidates, target, path):
#     if target == 0:
#         result.append(path)
#     elif not candidates or target < candidates[0]:
#         return
#     else:
#         for i,c in enumerate(candidates):
#             dfs(candidates[i:], target -c, path+[c])
#             print(candidates[i:])
# dfs(candidates, target, [])
# print(result)
            
#%% 深度優先搜尋 DFS 上網查到別人寫出來的
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def dfs(candidates, target, path):
            if target == 0:
                result.append(path)
            elif not candidates or target < candidates[0]:
                return
            else:
                for i,c in enumerate(candidates):
                    dfs(candidates[i:], target -c, path+[c])
        dfs(candidates, target, [])
        return result