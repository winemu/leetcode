#!/usr/bin/python

# leetcode003.py

"""
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    def lengthOfLongstSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        strRet = strTmp =""
        while(i < n):
            if(s[i] not in strTmp):
                strTmp = strTmp + s[i]
            else:
                if(len(strRet) < len(strTmp)):
                    strRet = strTmp
                strTmp = s[i]
            i += 1
        return(strRet)

str="pwwkew"
sol = Solution()
i=sol.lengthOfLongstSubstring(str)
print(i)

