# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:15:32 2022

@author: 沈睿朋
"""
#%%
def maxArea(height):
        number = []
        for i in range(len(height)):
            for j in range(len(height)):
                if height[i] < height[j]:
                    number.append(height[i]*abs(i-j))
                else:
                    number.append(height[j]*abs(i-j))
        return print(max(number))
maxArea([1,1])
#%%
class Solution:
    def maxArea(self, height):
        number = []
        for i in range(len(height)):
            for j in range(len(height)):
                if height[i] < height[j]:
                    number.append(height[i]*abs(i-j))
                else:
                    number.append(height[j]*abs(i-j))
        return max(number)