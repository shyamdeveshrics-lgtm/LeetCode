class Solution(object):
    def strStr(self, haystack, needle):
        a=haystack.count(needle)
        if a==0:
            return -1
        else:
            for i in range(len(haystack)):
                if (haystack.startswith(needle,i)):
                    return i
                    break