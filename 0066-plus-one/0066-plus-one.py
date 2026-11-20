class Solution(object):
    def plusOne(self, digits):
        a=""
        for i in digits:
            a+=str(i)
        a=int(a)+1
        return [int(i) for i in str(a)]