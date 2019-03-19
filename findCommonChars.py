"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 
"""

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        count = dict()
        res = list()
        for i in range(len(A)):
            for each in A[i]:
                t = [0] * len(A)
                if each in count.keys():
                    count[each][i] += 1 
                else:
                    t[i] = 1
                    count[each] = t
        
        for key in count.keys():
            presence = count[key]
            if min(presence) != 0:
                res.extend([key] * min(presence))
        
        return res
