# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:15:32 2022

@author: 沈睿朋
"""
#%%
def maxArea(height):
        number = []
        for i in height:
            for j in height:
                if i < j:
                    number.append(i*abs(height.index(j)-height.index(i)))
                elif i > j:
                    number.append(j*abs(height.index(j)-height.index(i)))
                else:
                    pass
        return print(max(number))
maxArea([1,8,6,2,5,4,8,3,7])
#%%
class Solution:
    def maxArea(self, height):
        number = []
        for i in height:
            for j in height:
                if i < j:
                    number.append(i*abs(height.index(j)-height.index(i)))
                elif i > j:
                    number.append(j*abs(height.index(j)-height.index(i)))
                else:
                    pass
        return max(number)
                    