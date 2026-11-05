class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        return sum(all(abs(a - b) > d for b in arr2) for a in arr1)