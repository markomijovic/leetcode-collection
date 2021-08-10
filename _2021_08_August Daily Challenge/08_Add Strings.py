"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        n1 = len(num1)
        n2 = len(num2)

        if n1 >= n2:
            s1 = num1
            s2 = num2
        else:
            s1 = num2
            n1 = len(num2)
            s2 = num1
            n2 = len(num1)
        N = n2 - n1

        i1 = 0
        i2 = 0
        ans = ""

        for i in range(n1-1, -1, -1):
            i1 += int(s1[i])
            if i+N >= 0:
                i2 = int(s2[i+N])
            else:
                i2 = 0
            val = (i1+i2) % 10
            ans = "".join((str(val), ans))
            if (i1+i2) >= 10:
                i1 = 1
                if i == 0:
                    ans = "".join((str(i1), ans))
            else:
                i1 = 0
        return ans
