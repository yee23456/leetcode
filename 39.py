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
    b = [sum(a[j:i+1]) for j in range(i+1)]
print(b)
#%%
def combinationSum(candidates, target):
    function = []
    if target in candidates:
        function.append([target])
    for i in range(len(candidates)):
        if [sum(a[j:i+1]) for j in range(i+1)] == target:
            
            
#%%