'''
SIXLETS
Problem Description

Given a array of integers A of size N and an integer B.

Return number of non-empty subsequences of A of size B having sum <= 1000.



Problem Constraints
1 <= N <= 20

1 <= A[i] <= 1000

1 <= B <= N



Input Format
The first argument given is the integer array A.

The second argument given is the integer B.



Output Format
Return number of subsequences of A of size B having sum <= 1000.



Example Input
Input 1:

    A = [1, 2, 8]
    B = 2
Input 2:

    A = [5, 17, 1000, 11]
    B = 4


Example Output
Output 1:

3
Output 2:

0


Example Explanation
Explanation 1:

 {1, 2}, {1, 8}, {2, 8}
Explanation 1:

 No valid subsequence
 '''

def solve(A, B):
    n = len(A)
    def _solve(_seq,_size,_sum,idx):
        _res = 0
        if _size == B:
            return 1 if _sum <= 1000 else 0
        for i in range(idx,n):
            _res += _solve(_seq+[A[i]],_size+1,_sum+A[i],i+1)
        return _res
    return _solve([],0,0,0)

print(solve([1, 2, 8], 2))
                