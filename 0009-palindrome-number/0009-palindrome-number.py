class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        a=x[::-1]
        if a==x:
            return True
        return False