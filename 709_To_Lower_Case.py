#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        for i in range(len(str)):
            if ord('A') <= ord(str[i]) <= ord('Z'):
                str = str.replace(str[i], chr(ord('a') + (ord(str[i]) - ord('A'))))
        return str

# More python
class Solution:
    def toLowerCase(self, str):
        return str.lower()
