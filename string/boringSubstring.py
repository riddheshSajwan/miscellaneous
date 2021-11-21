'''
Problem Description

Given a string A of lowercase English alphabets. Rearrange the characters of the given string A such that there is no boring substring in A.
A boring substring has the following properties:
Its length is 2.
Both the characters are consecutive, for example - "ab", "cd", "dc", "zy" etc.(If the first character is C then the next character can be either (C+1) or (C-1)).
Return 1 if it possible to rearrange the letters of A such that there are no boring substring in A, else return 0.

Problem Constraints
1 <= |A| <= 105

Input Format
The only argument given is string A.

Output Format
Return 1 if it possible to rearrange the letters of A such that there are no boring substring in A, else return 0.

Example Input
Input 1:
 A ="abcd"
Input 2:
 A = "aab"

Example Output
Output 1:
 1
Output 2:
 0

Example Explanation
Explanation 1:
 String A can be rearranged into "cadb" or "bdac" 
Explanation 2:
 No arrangement of string A can make it free of boring substrings.
 '''
def solve(A):
    li = ["",""]

    for item in sorted(set(A)):
        li[ord(item)%2] += item
    i = 0
    s = "".join(li)
    n = len(s)
    #print(s)
    while i < n-1 and abs(ord(s[i])-ord(s[i+1])) > 1:
        i += 1
    return 1 if i == n-1 else 0

print(solve("abcd"))
