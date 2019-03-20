"""
We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

"""

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = [None] * len(queries)
        evensum = sum([x for x in A if abs(x) % 2 == 0])
        
        for i in range(0, len(queries)):
            val = queries[i][0]
            index = queries[i][1]
            cval = A[index]
            nval = cval + val
            A[index] = nval
            
            if nval % 2 != 0:
                if cval % 2 == 0:
                    evensum -= cval
            else:
                if cval % 2 == 0:
                    evensum -= cval
                    evensum += nval
                else:
                    evensum += nval
                
            res[i] = evensum
            
        return res
