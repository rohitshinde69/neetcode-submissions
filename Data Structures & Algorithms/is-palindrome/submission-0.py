class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.lower()
        st1=""
        for c in st:
            if c.isalnum():
                st1+=c
        print(st1)
        if st1 == st1[::-1]:
            return True
        else:
            return False
        