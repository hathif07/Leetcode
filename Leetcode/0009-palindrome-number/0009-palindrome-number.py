class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted_number = 0
        while x > reverted_number:
            # Extract last digit, append to reversed
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
            
        # Even: x == reverted; Odd: x == reverted // 10
        return x == reverted_number or x == reverted_number // 10