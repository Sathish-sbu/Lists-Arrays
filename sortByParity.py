"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

"""
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        i = 0
        j = 1
        n = len(A)
        
        while (i < n and j < n):
            while i < n and A[i] % 2 == 0:
                i += 2
            while j < n and A[j] % 2 != 0:
                j += 2
            
            if (i < n) and (j < n):
                A[i], A[j] = A[j], A[i]
        
        return A
